# coding:utf-8
import os

from flask import jsonify, session

from . import main_bp
from api.models.brush_model import ershouliuzhuan, goumaidingdan, renlingshenqing, sensitivewords, shiwuzhaoling, yonghu
from api.services.ai_product_service import (
    evaluate_reputation,
    explain_recommendation,
    generate_listing,
    match_lostfound,
    moderate_text,
    natural_search,
)
from utils.baidubce_api import BaiDuBce
from utils.codes import normal_code, crud_error_code


def _req():
    return session.get("req_dict") or {}


def _sensitive_words():
    try:
        return [item.get("content") for item in sensitivewords.retrieve(sensitivewords, sensitivewords)]
    except Exception:
        return []


def _page(model, params=None):
    params = params or {"page": 1, "limit": 100}
    try:
        data, _, _, _, _ = model.page(model, model, params)
        return data
    except Exception:
        return []


def _student_card_result(ocr_text, user):
    text = (ocr_text or "").replace(" ", "")
    required_keywords = ["北京工业大学", "学生证", "学号", "姓名", "学院", "专业", "学生"]
    hits = [word for word in required_keywords if word in text]
    name = (user or {}).get("xingming") or ""
    has_name = bool(name and name in text)

    if len(hits) >= 2 and (has_name or not name):
        return True, "自动审核通过"

    reasons = []
    if len(hits) < 2:
        reasons.append("未识别到足够的学生证关键信息")
    if name and not has_name:
        reasons.append("学生证姓名与个人资料姓名不匹配")
    return False, "；".join(reasons) or "学生证识别未通过"


@main_bp.route("/python7i67w282/ai/listing/generate", methods=["POST"])
def python7i67w282_ai_listing_generate():
    payload = _req()
    data = generate_listing(payload, _sensitive_words())
    return jsonify({"code": normal_code, "msg": "success", "data": data})


@main_bp.route("/python7i67w282/ai/moderate", methods=["POST"])
def python7i67w282_ai_moderate():
    payload = _req()
    text = payload.get("text") or " ".join([str(v) for v in payload.values()])
    data = moderate_text(text, _sensitive_words())
    return jsonify({"code": normal_code, "msg": "success", "data": data})


@main_bp.route("/python7i67w282/ai/lostfound/match", methods=["GET", "POST"])
def python7i67w282_ai_lostfound_match():
    payload = _req()
    query = payload.get("query") or payload.get("description") or payload.get("text") or ""
    lost_items = _page(shiwuzhaoling, {"page": 1, "limit": 100, "sort": "addtime", "order": "desc"})
    claims = _page(renlingshenqing, {"page": 1, "limit": 100, "sort": "addtime", "order": "desc"})
    data = match_lostfound(lost_items, claims, query)
    return jsonify({"code": normal_code, "msg": "success", "data": data})


@main_bp.route("/python7i67w282/ai/search", methods=["GET", "POST"])
def python7i67w282_ai_search():
    payload = _req()
    query = payload.get("query") or payload.get("keyword") or ""
    secondhand_items = _page(ershouliuzhuan, {"page": 1, "limit": 100, "sort": "addtime", "order": "desc"})
    lost_items = _page(shiwuzhaoling, {"page": 1, "limit": 100, "sort": "addtime", "order": "desc"})
    data = natural_search(query, secondhand_items, lost_items)
    return jsonify({"code": normal_code, "msg": "success", "data": data})


@main_bp.route("/python7i67w282/ai/recommend/explain", methods=["POST"])
def python7i67w282_ai_recommend_explain():
    payload = _req()
    table_name = payload.get("tableName") or "ershouliuzhuan"
    record = payload.get("record") or payload
    data = explain_recommendation(record, table_name)
    return jsonify({"code": normal_code, "msg": "success", "data": data})


@main_bp.route("/python7i67w282/ai/reputation/recalculate", methods=["GET", "POST"])
def python7i67w282_ai_reputation_recalculate():
    payload = _req()
    user_id = payload.get("userId") or payload.get("userid") or payload.get("id")
    account = payload.get("zhanghao") or payload.get("account")
    users = []
    if user_id:
        users = yonghu.getbyid(yonghu, yonghu, int(user_id))
    elif account:
        users = yonghu.getbyparams(yonghu, yonghu, {"zhanghao": account})
    else:
        users = _page(yonghu, {"page": 1, "limit": 200, "sort": "id", "order": "asc"})

    secondhand_items = _page(ershouliuzhuan, {"page": 1, "limit": 500, "sort": "id", "order": "asc"})
    paid_orders = _page(goumaidingdan, {"page": 1, "limit": 500, "sort": "id", "order": "asc"})
    sensitive_words = _sensitive_words()
    results = []
    for user in users:
        reputation = evaluate_reputation(user, secondhand_items, paid_orders, sensitive_words)
        user["xinyudengji"] = reputation["level"]
        user["xinyufen"] = reputation["score"]
        user["xinyushuoming"] = reputation["summary"]
        yonghu.updatebyparams(yonghu, yonghu, user)
        results.append(reputation)

    return jsonify({"code": normal_code, "msg": "success", "data": results})


@main_bp.route("/python7i67w282/ai/student-card/verify", methods=["POST"])
def python7i67w282_ai_student_card_verify():
    payload = _req()
    user_id = payload.get("userId") or payload.get("userid") or payload.get("id")
    file_name = payload.get("fileName") or payload.get("shenfenzheng") or ""
    msg = {"code": normal_code, "msg": "success", "data": {}}

    if not user_id or not file_name:
        msg["code"] = crud_error_code
        msg["msg"] = "缺少用户或学生证图片"
        return jsonify(msg)

    file_name = str(file_name).split(",")[0].replace("\\", "/")
    if file_name.startswith("upload/"):
        relative_path = file_name.replace("upload/", "", 1)
    else:
        relative_path = file_name
    file_path = os.path.join(os.getcwd(), "api", "templates", "front", relative_path)

    users = yonghu.getbyid(yonghu, yonghu, int(user_id))
    if not users:
        msg["code"] = crud_error_code
        msg["msg"] = "用户不存在"
        return jsonify(msg)

    user = users[0]
    if not os.path.exists(file_path):
        user["sfsh"] = "待审核"
        user["shhf"] = "学生证图片不存在，请重新上传"
        yonghu.updatebyparams(yonghu, yonghu, user)
        msg["data"] = {"passed": False, "status": "待审核", "reason": user["shhf"], "ocrText": ""}
        return jsonify(msg)

    try:
        ocr_text = BaiDuBce().ocr_checkpic(file_path)
        passed, reason = _student_card_result(ocr_text, user)
        user["shenfenzheng"] = "upload/" + relative_path
        user["sfsh"] = "是" if passed else "否"
        user["shhf"] = reason
        yonghu.updatebyparams(yonghu, yonghu, user)
        msg["data"] = {
            "passed": passed,
            "status": user["sfsh"],
            "reason": reason,
            "ocrText": ocr_text,
        }
        return jsonify(msg)
    except Exception:
        user["shenfenzheng"] = "upload/" + relative_path
        user["sfsh"] = "待审核"
        user["shhf"] = "OCR服务暂不可用，已转入人工审核"
        yonghu.updatebyparams(yonghu, yonghu, user)
        msg["data"] = {
            "passed": False,
            "status": "待审核",
            "reason": user["shhf"],
            "ocrText": "",
        }
        return jsonify(msg)
