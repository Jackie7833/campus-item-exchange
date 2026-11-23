const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "../../mp-weixin");
const baseUrl = "http://127.0.0.1:8080/python7i67w282/";

function read(file) {
  return fs.readFileSync(path.join(root, file), "utf8");
}

function write(file, content) {
  const full = path.join(root, file);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, content);
}

function replaceOnce(file, from, to) {
  const content = read(file);
  if (!content.includes(from)) {
    throw new Error(`${file} missing expected content: ${from.slice(0, 80)}`);
  }
  write(file, content.replace(from, to));
}

function ensureAppJson() {
  const file = "app.json";
  const app = JSON.parse(read(file));
  const page = "pages/ai-assistant/ai-assistant";
  if (!app.pages.includes(page)) {
    app.pages.splice(1, 0, page);
  }
  write(file, `${JSON.stringify(app, null, 2)}\n`);
}

function writeAiAssistantPage() {
  write("pages/ai-assistant/ai-assistant.json", JSON.stringify({
    navigationBarTitleText: "AI校园助手",
    navigationBarBackgroundColor: "#FFFFFF",
    navigationBarTextStyle: "black"
  }, null, 2) + "\n");

  write("pages/ai-assistant/ai-assistant.wxml", `<view class="page">
  <view class="hero">
    <view class="hero-title">AI校园物品流转助手</view>
    <view class="hero-subtitle">集中测试智能搜索、失物匹配和内容审核。</view>
  </view>

  <view class="tabs">
    <view class="tab {{mode == 'search' ? 'active' : ''}}" data-mode="search" bindtap="switchMode">智能搜索</view>
    <view class="tab {{mode == 'match' ? 'active' : ''}}" data-mode="match" bindtap="switchMode">失物匹配</view>
    <view class="tab {{mode == 'moderate' ? 'active' : ''}}" data-mode="moderate" bindtap="switchMode">内容审核</view>
  </view>

  <view class="panel">
    <textarea class="input" value="{{query}}" placeholder="{{placeholder}}" bindinput="onInput"></textarea>
    <button class="primary" loading="{{loading}}" disabled="{{loading}}" bindtap="runAiTask">{{buttonText}}</button>
  </view>

  <view class="result" wx:if="{{hasResult}}">
    <view class="result-title">AI 结果</view>

    <block wx:if="{{mode == 'search'}}">
      <view class="empty" wx:if="{{results.length == 0}}">暂未找到相关内容，可换一种描述。</view>
      <view class="item" wx:for="{{results}}" wx:key="id" data-type="{{item.type}}" data-id="{{item.id}}" bindtap="goDetail">
        <view class="item-title">{{item.title}}</view>
        <view class="item-meta">{{item.type}} · 匹配分 {{item.score}}</view>
        <view class="item-reason">{{item.reason}}</view>
      </view>
    </block>

    <block wx:if="{{mode == 'match'}}">
      <view class="empty" wx:if="{{results.length == 0}}">暂无疑似匹配的认领申请。</view>
      <view class="item" wx:for="{{results}}" wx:key="claimId">
        <view class="item-title">{{item.itemName}}</view>
        <view class="item-meta">失物 #{{item.lostId}} · 认领 #{{item.claimId}} · {{item.score}}分</view>
        <view class="item-reason">{{item.reason}}</view>
        <view class="item-reason">核验：{{item.verifyText}}</view>
      </view>
    </block>

    <block wx:if="{{mode == 'moderate'}}">
      <view class="item">
        <view class="item-title">风险等级：{{moderation.riskLevel}}</view>
        <view class="item-meta">处理建议：{{moderation.action}}</view>
        <view class="item-reason">{{moderation.summary}}</view>
        <view class="item-reason">命中：{{moderation.hitText}}</view>
        <view class="item-reason">边界：{{moderation.guardrailText}}</view>
      </view>
    </block>
  </view>
</view>
`);

  write("pages/ai-assistant/ai-assistant.wxss", `.page{min-height:100vh;background:#f4f7fb;padding:24rpx;box-sizing:border-box}.hero{padding:28rpx 8rpx 20rpx}.hero-title{font-size:40rpx;font-weight:700;color:#102a43;line-height:1.4}.hero-subtitle{font-size:26rpx;color:#526579;line-height:1.6;margin-top:8rpx}.tabs{display:flex;gap:12rpx;margin:10rpx 0 20rpx}.tab{flex:1;text-align:center;font-size:26rpx;line-height:64rpx;border-radius:10rpx;background:#e8eef5;color:#526579}.tab.active{background:#102a43;color:#fff}.panel,.result{background:#fff;border-radius:12rpx;padding:24rpx;margin-top:20rpx}.input{width:100%;min-height:180rpx;border:2rpx solid #dde6f0;border-radius:10rpx;padding:18rpx;box-sizing:border-box;font-size:28rpx;line-height:1.6;background:#fbfdff}.primary{margin-top:20rpx;background:#1f7a8c;color:#fff;border-radius:12rpx;font-size:28rpx;line-height:76rpx}.result-title{font-size:30rpx;font-weight:700;color:#102a43;margin-bottom:16rpx}.item{padding:20rpx;border:2rpx solid #e6eef7;border-radius:10rpx;margin-bottom:16rpx;background:#fbfdff}.item-title{font-size:30rpx;font-weight:700;color:#102a43;line-height:1.5}.item-meta{font-size:24rpx;color:#62758a;line-height:1.6;margin-top:4rpx}.item-reason{font-size:24rpx;color:#34495e;line-height:1.7;margin-top:6rpx}.empty{font-size:26rpx;color:#7a8796;line-height:1.7;padding:20rpx 0}
`);

  write("pages/ai-assistant/ai-assistant.js", `const BASE_URL = ${JSON.stringify(baseUrl)};

function postAI(url, data) {
  return new Promise((resolve, reject) => {
    wx.request({
      url: BASE_URL + url,
      method: "POST",
      data: data || {},
      header: { "content-type": "application/json" },
      success(res) {
        if (res.data && res.data.code === 0) resolve(res.data.data);
        else reject(new Error((res.data && res.data.msg) || "AI request failed"));
      },
      fail: reject
    });
  });
}

Page({
  data: {
    mode: "search",
    query: "",
    loading: false,
    hasResult: false,
    results: [],
    moderation: {},
    placeholder: "例如：我想找蓝牙耳机或者手机充电器",
    buttonText: "开始智能搜索"
  },
  switchMode(e) {
    const mode = e.currentTarget.dataset.mode;
    const text = {
      search: ["例如：我想找蓝牙耳机或者手机充电器", "开始智能搜索"],
      match: ["可选：描述你丢失、捡到或想认领的物品，例如：我丢了白色无线耳机，带充电盒，可能在操场附近", "生成失物匹配"],
      moderate: ["粘贴商品描述、评论或认领申请，检测隐私、诈骗、违规交易风险", "检测内容风险"]
    }[mode];
    this.setData({ mode, query: "", hasResult: false, results: [], moderation: {}, placeholder: text[0], buttonText: text[1] });
  },
  onInput(e) {
    this.setData({ query: e.detail.value });
  },
  runAiTask() {
    if (this.data.mode !== "match" && !this.data.query.trim()) {
      wx.showToast({ title: "请先输入内容", icon: "none" });
      return;
    }
    this.setData({ loading: true });
    let task;
    if (this.data.mode === "search") task = postAI("ai/search", { query: this.data.query });
    else if (this.data.mode === "match") task = postAI("ai/lostfound/match", { query: this.data.query });
    else task = postAI("ai/moderate", { text: this.data.query });
    task.then((data) => {
      if (this.data.mode === "moderate") {
        const moderation = Object.assign({}, data, {
          hitText: (data.hits || []).join("、") || "无",
          guardrailText: (data.guardrails || []).join("；")
        });
        this.setData({ moderation, hasResult: true });
      } else {
        const results = (data || []).map((item) => Object.assign({}, item, {
          verifyText: (item.verifyQuestions || []).join("；")
        }));
        this.setData({ results, hasResult: true });
      }
    }).catch(() => {
      wx.showToast({ title: "AI助手暂不可用", icon: "none" });
    }).finally(() => {
      this.setData({ loading: false });
    });
  },
  goDetail(e) {
    const type = e.currentTarget.dataset.type;
    const id = e.currentTarget.dataset.id;
    if (!type || !id) return;
    wx.navigateTo({ url: "/pages/" + type + "/detail?id=" + id });
  }
});
`);
}

function patchIndexEntry() {
  const file = "pages/index/index.wxml";
  const marker = `</view><block wx:if="{{true}}"><view class="menu_view data-v-57280228">`;
  const card = `</view><navigator url="/pages/ai-assistant/ai-assistant" hover-class="none" class="ai-entry"><view class="ai-entry-title">AI校园物品流转助手</view><view class="ai-entry-subtitle">智能搜索、失物匹配、内容审核与推荐解释</view></navigator><block wx:if="{{true}}"><view class="menu_view data-v-57280228">`;
  const content = read(file);
  if (!content.includes(`class="ai-entry"`)) replaceOnce(file, marker, card);
  const wxss = read("pages/index/index.wxss");
  if (!wxss.includes(".ai-entry")) {
    write("pages/index/index.wxss", wxss + `.ai-entry{display:block;margin:24rpx 20rpx 0;padding:24rpx;border-radius:12rpx;background:#102a43;color:#fff}.ai-entry-title{font-size:34rpx;font-weight:700;line-height:1.5}.ai-entry-subtitle{font-size:24rpx;line-height:1.6;opacity:.86}\n`);
  }
}

function patchSecondhandPublish() {
  if (!read("pages/ershouliuzhuan/add-or-update.js").includes("aiLoading: false")) {
    replaceOnce("pages/ershouliuzhuan/add-or-update.js", "      virtualPay: false\n    };", "      virtualPay: false,\n      aiLoading: false,\n      aiResult: null\n    };");
  }
  if (!read("pages/ershouliuzhuan/add-or-update.js").includes("onAiGenerateTap: function onAiGenerateTap")) {
    replaceOnce("pages/ershouliuzhuan/add-or-update.js", `    miaoshuChange: function miaoshuChange(e) {
      this.ruleForm.miaoshu = e;
    },`, `    miaoshuChange: function miaoshuChange(e) {
      this.ruleForm.miaoshu = e;
    },
    onAiGenerateTap: function onAiGenerateTap() {
      var _this = this;
      this.aiLoading = true;
      this.$api.postPublic("ai/listing/generate", Object.assign({ scene: "secondhand" }, this.ruleForm)).then(function (res) {
        var data = res.data || {};
        _this.aiResult = data;
        if (!_this.ruleForm.shangpinmingcheng && data.title) _this.ruleForm.shangpinmingcheng = data.title;
        if ((!_this.ruleForm.shangpinleixing || _this.ruleForm.shangpinleixing === "请选择商品类型") && data.category) _this.ruleForm.shangpinleixing = data.category;
        if (!_this.ruleForm.miaoshu && data.description) _this.ruleForm.miaoshu = data.description;
        if (!_this.ruleForm.jiage && data.priceSuggestion) _this.ruleForm.jiage = data.priceSuggestion.min;
        _this.$utils.msg("AI 已生成草稿，请确认后提交");
        _this.$forceUpdate();
      }).catch(function () {
        _this.$utils.msg("AI 发布助手暂不可用，请继续手动填写");
      }).finally(function () {
        _this.aiLoading = false;
        _this.$forceUpdate();
      });
    },`);
  }
  const file = "pages/ershouliuzhuan/add-or-update.wxml";
  const marker = `<view class="btn data-v-7db93a16"`;
  const aiCard = `<view class="ai-card data-v-7db93a16"><view class="ai-card-title data-v-7db93a16">AI 发布助手</view><view class="ai-card-desc data-v-7db93a16">根据已填写内容生成标题、分类、描述、参考价和交易风险提示，结果需人工确认后再提交。</view><button loading="{{aiLoading}}" disabled="{{aiLoading}}" data-event-opts="{{[['tap',[['onAiGenerateTap',['$event']]]]]}}" bindtap="__e" class="ai-card-button data-v-7db93a16">AI 优化发布信息</button><view wx:if="{{aiResult}}" class="ai-result data-v-7db93a16"><view wx:if="{{aiResult.priceSuggestion}}" class="data-v-7db93a16">参考价：{{aiResult.priceSuggestion.min}}-{{aiResult.priceSuggestion.max}} 元</view><view wx:if="{{aiResult.moderation}}" class="data-v-7db93a16">风险：{{aiResult.moderation.summary}}</view><view wx:if="{{aiResult.modelBoundary}}" class="boundary data-v-7db93a16">{{aiResult.modelBoundary}}</view></view></view><view class="btn data-v-7db93a16"`;
  const content = read(file);
  if (!content.includes("AI 发布助手")) replaceOnce(file, marker, aiCard);
  const wxss = read("pages/ershouliuzhuan/add-or-update.wxss");
  if (!wxss.includes(".ai-card")) {
    write("pages/ershouliuzhuan/add-or-update.wxss", wxss + `.ai-card{padding:20rpx;margin:0 0 24rpx;border:2rpx solid #dde9f6;border-radius:12rpx;background:#f7fbff}.ai-card-title{font-size:30rpx;font-weight:600;color:#1f4e79;margin-bottom:12rpx}.ai-card-desc,.ai-result{font-size:24rpx;line-height:1.7;color:#526579;margin-bottom:16rpx}.ai-card-button{border:0;color:#fff;border-radius:12rpx;background:#1f7a8c;width:100%;line-height:72rpx;font-size:28rpx;height:72rpx}.boundary{color:#7a4e00;margin-top:6rpx}\n`);
  }
}

function patchLostfoundPublish() {
  if (!read("pages/shiwuzhaoling/add-or-update.js").includes("aiLoading: false")) {
    replaceOnce("pages/shiwuzhaoling/add-or-update.js", "      virtualPay: false\n    };", "      virtualPay: false,\n      aiLoading: false,\n      aiResult: null\n    };");
  }
  if (!read("pages/shiwuzhaoling/add-or-update.js").includes("onAiGenerateTap: function onAiGenerateTap")) {
    replaceOnce("pages/shiwuzhaoling/add-or-update.js", `    wupinxiangqingChange: function wupinxiangqingChange(e) {
      this.ruleForm.wupinxiangqing = e;
    },`, `    wupinxiangqingChange: function wupinxiangqingChange(e) {
      this.ruleForm.wupinxiangqing = e;
    },
    onAiGenerateTap: function onAiGenerateTap() {
      var _this = this;
      this.aiLoading = true;
      this.$api.postPublic("ai/listing/generate", Object.assign({ scene: "lostfound" }, this.ruleForm)).then(function (res) {
        var data = res.data || {};
        _this.aiResult = data;
        if (!_this.ruleForm.biaoti && data.title) _this.ruleForm.biaoti = data.title;
        if (!_this.ruleForm.wupinleixing && data.category) _this.ruleForm.wupinleixing = data.category;
        if (!_this.ruleForm.wupinxiangqing && data.description) _this.ruleForm.wupinxiangqing = data.description;
        _this.$utils.msg("AI 已生成招领草稿，请确认后提交");
        _this.$forceUpdate();
      }).catch(function () {
        _this.$utils.msg("AI 失物助手暂不可用，请继续手动填写");
      }).finally(function () {
        _this.aiLoading = false;
        _this.$forceUpdate();
      });
    },`);
  }
  const file = "pages/shiwuzhaoling/add-or-update.wxml";
  const marker = `<view class="btn data-v-74e2c573"`;
  const aiCard = `<view class="ai-card data-v-74e2c573"><view class="ai-card-title data-v-74e2c573">AI 失物发布助手</view><view class="ai-card-desc data-v-74e2c573">自动生成招领标题、物品详情、核验问题和风险提示；模型不判断真实归属，认领仍需人工复核。</view><button loading="{{aiLoading}}" disabled="{{aiLoading}}" data-event-opts="{{[['tap',[['onAiGenerateTap',['$event']]]]]}}" bindtap="__e" class="ai-card-button data-v-74e2c573">AI 优化招领信息</button><view wx:if="{{aiResult}}" class="ai-result data-v-74e2c573"><view wx:if="{{aiResult.verifyQuestions}}" class="data-v-74e2c573">核验问题：{{aiResult.verifyQuestions}}</view><view wx:if="{{aiResult.moderation}}" class="data-v-74e2c573">风险：{{aiResult.moderation.summary}}</view><view wx:if="{{aiResult.modelBoundary}}" class="boundary data-v-74e2c573">{{aiResult.modelBoundary}}</view></view></view><view class="btn data-v-74e2c573"`;
  const content = read(file);
  if (!content.includes("AI 失物发布助手")) replaceOnce(file, marker, aiCard);
  const wxss = read("pages/shiwuzhaoling/add-or-update.wxss");
  if (!wxss.includes(".ai-card")) {
    write("pages/shiwuzhaoling/add-or-update.wxss", wxss + `.ai-card{padding:20rpx;margin:0 0 24rpx;border:2rpx solid #dde9f6;border-radius:12rpx;background:#f7fbff}.ai-card-title{font-size:30rpx;font-weight:600;color:#1f4e79;margin-bottom:12rpx}.ai-card-desc,.ai-result{font-size:24rpx;line-height:1.7;color:#526579;margin-bottom:16rpx}.ai-card-button{border:0;color:#fff;border-radius:12rpx;background:#1f7a8c;width:100%;line-height:72rpx;font-size:28rpx;height:72rpx}.boundary{color:#7a4e00;margin-top:6rpx}\n`);
  }
}

function patchRecommendExplain() {
  if (!read("pages/ershouliuzhuan/detail.js").includes("aiRecommend: null")) {
    replaceOnce("pages/ershouliuzhuan/detail.js", "      detail: {},\n      swiperList: [],", "      detail: {},\n      aiRecommend: null,\n      swiperList: [],");
  }
  if (!read("pages/ershouliuzhuan/detail.js").includes("ai/recommend/explain")) {
    replaceOnce("pages/ershouliuzhuan/detail.js", `                _this7.detail = res.data;
                _this7.title = _this7.detail.shangpinmingcheng;`, `                _this7.detail = res.data;
                _this7.title = _this7.detail.shangpinmingcheng;
                _this7.$api.postPublic("ai/recommend/explain", {
                  tableName: "ershouliuzhuan",
                  record: _this7.detail
                }).then(function (aiRes) {
                  _this7.aiRecommend = aiRes.data;
                  _this7.$forceUpdate();
                }).catch(function () {});`);
  }
  const file = "pages/ershouliuzhuan/detail.wxml";
  const marker = `<view class="detail-list-item rich"`;
  const card = `<view wx:if="{{aiRecommend}}" class="ai-recommend"><view class="ai-recommend-title">AI 推荐理由</view><view class="ai-recommend-text">{{aiRecommend.reason}}</view><view class="ai-recommend-boundary">{{aiRecommend.boundary}}</view></view><view class="detail-list-item rich"`;
  const content = read(file);
  if (!content.includes("AI 推荐理由")) replaceOnce(file, marker, card);
  const wxss = read("pages/ershouliuzhuan/detail.wxss");
  if (!wxss.includes(".ai-recommend")) {
    write("pages/ershouliuzhuan/detail.wxss", wxss + `.ai-recommend{padding:20rpx;margin:0 0 24rpx;background:#fff;border-left:8rpx solid #1f7a8c}.ai-recommend-title{font-size:30rpx;font-weight:700;color:#102a43;line-height:1.5}.ai-recommend-text{font-size:26rpx;color:#34495e;line-height:1.7;margin-top:8rpx}.ai-recommend-boundary{font-size:24rpx;color:#7a4e00;line-height:1.7;margin-top:6rpx}\n`);
  }
}

function patchStudentCardStatus() {
  const file = "pages/user-info/user-info.wxml";
  const marker = `<view class="btn data-v-3a65c7b0"`;
  const card = `<view wx:if="{{ruleForm.sfsh}}" class="student-ai-status data-v-3a65c7b0"><view class="student-ai-title data-v-3a65c7b0">AI 学生证审核状态</view><view class="student-ai-text data-v-3a65c7b0">状态：{{ruleForm.sfsh}}</view><view wx:if="{{ruleForm.shhf}}" class="student-ai-text data-v-3a65c7b0">说明：{{ruleForm.shhf}}</view></view><view class="btn data-v-3a65c7b0"`;
  const content = read(file);
  if (!content.includes("AI 学生证审核状态")) replaceOnce(file, marker, card);
  const wxss = read("pages/user-info/user-info.wxss");
  if (!wxss.includes(".student-ai-status")) {
    write("pages/user-info/user-info.wxss", wxss + `.student-ai-status{padding:20rpx;margin:0 0 24rpx;border:2rpx solid #dde9f6;border-radius:12rpx;background:#f7fbff}.student-ai-title{font-size:30rpx;font-weight:600;color:#1f4e79;line-height:1.5}.student-ai-text{font-size:24rpx;color:#34495e;line-height:1.7;margin-top:6rpx}\n`);
  }
}

ensureAppJson();
writeAiAssistantPage();
patchIndexEntry();
patchSecondhandPublish();
patchLostfoundPublish();
patchRecommendExplain();
patchStudentCardStatus();
console.log("AI features synced to mp-weixin.");
