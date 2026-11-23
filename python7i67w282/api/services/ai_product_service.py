# coding:utf-8
import re


RISK_WORDS = [
    "诈骗",
    "转账",
    "押金",
    "身份证",
    "银行卡",
    "密码",
    "验证码",
    "私下交易",
    "先款",
]

CATEGORY_KEYWORDS = {
    "数码": ["耳机", "手机", "电脑", "平板", "充电器", "键盘", "鼠标", "相机"],
    "学习用品": ["书", "教材", "笔记", "资料", "计算器", "文具"],
    "生活用品": ["水杯", "雨伞", "饭卡", "校园卡", "钥匙", "背包", "衣服"],
    "运动户外": ["自行车", "球", "球拍", "哑铃", "滑板"],
    "美妆服饰": ["口红", "护肤", "外套", "鞋", "帽子"],
}


def clean_text(value):
    if value is None:
        return ""
    value = re.sub(r"<[^>]+>", " ", str(value))
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def infer_category(text):
    text = clean_text(text)
    for category, words in CATEGORY_KEYWORDS.items():
        if any(word in text for word in words):
            return category
    return "其他"


def extract_keywords(text):
    text = clean_text(text)
    chunks = re.findall(r"[\u4e00-\u9fa5A-Za-z0-9]{2,}", text)
    stop_words = set(["一个", "这个", "那个", "商品", "物品", "描述", "地点", "校园", "需要", "希望"])
    keywords = []
    for chunk in chunks:
        if chunk not in stop_words and chunk not in keywords:
            keywords.append(chunk)
        if len(keywords) >= 8:
            break
    return keywords


def price_suggestion(text, category, price=None):
    try:
        if price not in [None, ""]:
            price_num = int(float(price))
            return {
                "min": max(1, int(price_num * 0.85)),
                "max": int(price_num * 1.1),
                "reason": "按用户填写价格给出可议价区间，避免发布价过高影响成交。",
            }
    except Exception:
        pass

    defaults = {
        "数码": (50, 300),
        "学习用品": (10, 80),
        "生活用品": (5, 60),
        "运动户外": (30, 250),
        "美妆服饰": (10, 120),
        "其他": (10, 100),
    }
    low, high = defaults.get(category, defaults["其他"])
    return {"min": low, "max": high, "reason": "按校园二手常见品类给出默认参考价，发布前需人工确认。"}


def moderate_text(text, sensitive_words=None):
    text = clean_text(text)
    sensitive_words = [clean_text(item) for item in (sensitive_words or []) if clean_text(item)]
    hits = []
    for word in sensitive_words + RISK_WORDS:
        if word and word in text and word not in hits:
            hits.append(word)

    privacy_patterns = [
        (r"1[3-9]\d{9}", "手机号"),
        (r"\d{15}|\d{17}[\dXx]", "身份证号"),
        (r"\d{6}", "疑似验证码/取件码"),
    ]
    for pattern, label in privacy_patterns:
        if re.search(pattern, text) and label not in hits:
            hits.append(label)

    if any(word in hits for word in ["诈骗", "银行卡", "密码", "验证码", "身份证号"]):
        level = "high"
        action = "block_or_review"
    elif hits:
        level = "medium"
        action = "manual_review"
    else:
        level = "low"
        action = "pass"

    return {
        "riskLevel": level,
        "action": action,
        "hits": hits,
        "summary": "发现需复核内容：{}".format("、".join(hits)) if hits else "未发现明显违规或隐私风险。",
        "guardrails": [
            "模型只做风险提示，不自动认定交易或认领真实性。",
            "涉及身份、付款、取件码的信息需脱敏后展示。",
            "高风险内容进入人工审核，不直接发布。",
        ],
    }


def generate_listing(payload, sensitive_words=None):
    payload = payload or {}
    raw_text = clean_text(" ".join([
        payload.get("shangpinmingcheng", ""),
        payload.get("wupinmingcheng", ""),
        payload.get("pinpai", ""),
        payload.get("guige", ""),
        payload.get("miaoshu", ""),
        payload.get("wupinxiangqing", ""),
        payload.get("jiaoyidizhi", ""),
        payload.get("shiqudidian", ""),
    ]))
    keywords = extract_keywords(raw_text)
    category = payload.get("shangpinleixing") or payload.get("wupinleixing") or infer_category(raw_text)
    item_name = payload.get("shangpinmingcheng") or payload.get("wupinmingcheng") or (keywords[0] if keywords else "校园物品")
    scene = payload.get("scene", "secondhand")
    is_lost = scene == "lostfound"

    if is_lost:
        title = payload.get("biaoti") or "【失物招领】{}待认领".format(item_name)
        description = payload.get("wupinxiangqing") or "在{}拾到{}，物品特征：{}。请认领人描述关键特征并出示相关凭证。".format(
            payload.get("shiqudidian") or "校园内",
            item_name,
            "、".join(keywords[1:4]) if len(keywords) > 1 else "外观、时间、地点"
        )
        result = {
            "title": title,
            "category": category,
            "description": description,
            "verifyQuestions": [
                "请说明遗失的大致时间和地点。",
                "请描述物品外观、品牌或特殊标记。",
                "如涉及证件或校园卡，请提供脱敏后的证明信息。",
            ],
        }
    else:
        price = price_suggestion(raw_text, category, payload.get("jiage"))
        title = payload.get("shangpinmingcheng") or "{}转让".format(item_name)
        description = payload.get("miaoshu") or "{}，适合校内自取。成色和配件请以实物为准，建议当面验货后交易。".format(
            "、".join(keywords) if keywords else item_name
        )
        result = {
            "title": title,
            "category": category,
            "description": description,
            "priceSuggestion": price,
            "tradeTips": [
                "建议校内公共区域当面交易。",
                "不要提前支付押金或透露验证码。",
                "商品状态、配件和瑕疵需在描述中说明。",
            ],
        }

    result["keywords"] = keywords
    result["moderation"] = moderate_text(raw_text, sensitive_words)
    result["modelBoundary"] = "当前结果为 AI 辅助草稿，发布前必须由用户确认；价格、归属权和交易安全不由模型担保。"
    return result


def token_set(record, fields):
    text = " ".join([clean_text(record.get(field, "")) for field in fields])
    return set(extract_keywords(text))


def related_tokens(left, right):
    related = set(left).intersection(set(right))
    for l_token in left:
        for r_token in right:
            if l_token and r_token and (l_token in r_token or r_token in l_token):
                related.add(l_token if len(l_token) <= len(r_token) else r_token)
                continue
            common_chars = set(l_token).intersection(set(r_token))
            if len(common_chars) >= 2:
                related.add(l_token if len(l_token) <= len(r_token) else r_token)
    return related


def match_lostfound(lost_items, claims, query=""):
    query_tokens = set(extract_keywords(query))
    results = []
    for lost in lost_items:
        lost_tokens = token_set(lost, ["biaoti", "wupinmingcheng", "wupinleixing", "wupinxiangqing", "shiqudidian"])
        for claim in claims:
            claim_tokens = token_set(claim, ["biaoti", "wupinmingcheng", "wupinleixing", "renlingren", "shouji"])
            query_overlap = related_tokens(query_tokens, lost_tokens.union(claim_tokens)) if query_tokens else set()
            if query_tokens and not query_overlap:
                continue
            overlap = related_tokens(lost_tokens, claim_tokens)
            base = len(overlap) * 18
            if query_overlap:
                base += len(query_overlap) * 20
            if clean_text(lost.get("wupinmingcheng")) and lost.get("wupinmingcheng") == claim.get("wupinmingcheng"):
                base += 30
            if clean_text(lost.get("wupinleixing")) and lost.get("wupinleixing") == claim.get("wupinleixing"):
                base += 15
            score = min(99, base)
            if score >= 15:
                reason_parts = []
                if query_overlap:
                    reason_parts.append("描述匹配：{}".format("、".join(list(query_overlap)[:5])))
                if overlap:
                    reason_parts.append("失物与认领重合：{}".format("、".join(list(overlap)[:5])))
                results.append({
                    "lostId": lost.get("id"),
                    "claimId": claim.get("id"),
                    "itemName": lost.get("wupinmingcheng") or claim.get("wupinmingcheng"),
                    "score": score,
                    "reason": "；".join(reason_parts) if reason_parts else "物品名称或类型相近。",
                    "verifyQuestions": [
                        "认领人能否描述物品的特殊标记？",
                        "遗失时间、地点是否与发布信息一致？",
                        "是否需要管理员人工复核后再交换联系方式？",
                    ],
                })
    return sorted(results, key=lambda item: item["score"], reverse=True)[:10]


def natural_search(query, secondhand_items, lost_items):
    query_tokens = set(extract_keywords(query))
    results = []
    for item in secondhand_items:
        item_tokens = token_set(item, ["shangpinmingcheng", "shangpinleixing", "pinpai", "guige", "miaoshu", "jiaoyidizhi"])
        overlap = related_tokens(query_tokens, item_tokens)
        if overlap:
            results.append({
                "type": "ershouliuzhuan",
                "id": item.get("id"),
                "title": item.get("shangpinmingcheng"),
                "score": min(99, len(overlap) * 25 + int(item.get("storeupnum") or 0)),
                "reason": "匹配到：{}".format("、".join(overlap)),
            })
    for item in lost_items:
        item_tokens = token_set(item, ["biaoti", "wupinmingcheng", "wupinleixing", "wupinxiangqing", "shiqudidian"])
        overlap = related_tokens(query_tokens, item_tokens)
        if overlap:
            results.append({
                "type": "shiwuzhaoling",
                "id": item.get("id"),
                "title": item.get("biaoti") or item.get("wupinmingcheng"),
                "score": min(99, len(overlap) * 25 + int(item.get("storeupnum") or 0)),
                "reason": "匹配到：{}".format("、".join(overlap)),
            })
    return sorted(results, key=lambda item: item["score"], reverse=True)[:20]


def evaluate_reputation(user, secondhand_items=None, paid_orders=None, sensitive_words=None):
    user = user or {}
    def value(obj, key, default=None):
        if isinstance(obj, dict):
            return obj.get(key, default)
        return getattr(obj, key, default)

    account = value(user, "zhanghao", "") or ""
    secondhand_items = secondhand_items or []
    paid_orders = paid_orders or []
    own_items = [item for item in secondhand_items if value(item, "zhanghao") == account]
    own_paid_orders = [
        order for order in paid_orders
        if value(order, "zhanghao") == account and value(order, "ispay") == "已支付"
    ]

    low_risk_count = 0
    medium_or_high = 0
    for item in own_items:
        text = " ".join([
            clean_text(value(item, "shangpinmingcheng")),
            clean_text(value(item, "shangpinleixing")),
            clean_text(value(item, "pinpai")),
            clean_text(value(item, "guige")),
            clean_text(value(item, "miaoshu")),
            clean_text(value(item, "jiaoyidizhi")),
        ])
        audit = moderate_text(text, sensitive_words)
        if audit.get("riskLevel") == "low":
            low_risk_count += 1
        else:
            medium_or_high += 1

    published_count = len(own_items)
    pass_rate = (low_risk_count / published_count) if published_count else 0.8
    paid_count = len(own_paid_orders)
    score = int(55 + min(paid_count, 4) * 8 + pass_rate * 22 - medium_or_high * 8)
    score = max(40, min(100, score))

    if score >= 85:
        level = "优秀"
    elif score >= 70:
        level = "良好"
    elif score >= 55:
        level = "普通"
    else:
        level = "需谨慎"

    summary = "已支付成交{}笔，发布{}件，低风险发布占比{}%。".format(
        paid_count,
        published_count,
        int(pass_rate * 100)
    )
    return {
        "account": account,
        "level": level,
        "score": score,
        "summary": summary,
        "paidOrderCount": paid_count,
        "publishedCount": published_count,
        "contentPassRate": round(pass_rate, 2),
    }


def explain_recommendation(record, table_name):
    if table_name == "ershouliuzhuan":
        signals = []
        if int(record.get("clicknum") or 0) > 0:
            signals.append("近期浏览较多")
        if int(record.get("storeupnum") or 0) > 0:
            signals.append("有用户收藏")
        if int(record.get("thumbsupnum") or 0) > 0:
            signals.append("获得点赞")
        return {
            "title": record.get("shangpinmingcheng"),
            "reason": "、".join(signals) if signals else "与校园二手交易场景相关，可补充更多浏览和收藏信号。",
            "boundary": "推荐解释来自行为和文本信号，不代表平台担保商品质量。",
        }
    return {
        "title": record.get("biaoti") or record.get("wupinmingcheng"),
        "reason": "按物品类型、地点、发布时间和收藏行为进行解释。",
        "boundary": "推荐解释不代表物品归属判断，认领仍需人工核验。",
    }
