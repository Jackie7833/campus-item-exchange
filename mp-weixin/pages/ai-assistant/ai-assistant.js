const DEV_API_BASE = "http://127.0.0.1:8080/python7i67w282/";
// 体验版/正式版必须使用已在微信公众平台配置的 HTTPS 合法域名。
// 示例："https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/"
const RELEASE_API_BASE = "https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/";
const CLOUD_ENV = "prod-d2glavkbz3c97ef18";
const CLOUD_SERVICE = "flask-2u3u";
function resolveApiBase() {
  try {
    const info = wx.getAccountInfoSync ? wx.getAccountInfoSync() : null;
    const envVersion = info && info.miniProgram && info.miniProgram.envVersion;
    if (envVersion === "develop") {
      return RELEASE_API_BASE;
    }
  } catch (e) {}
  return RELEASE_API_BASE;
}
const BASE_URL = resolveApiBase();
function toContainerPath(url) {
  return url.replace(/^https?:\/\/[^/]+/, "");
}
function postAI(url, data) {
  if (BASE_URL.indexOf("YOUR_HTTPS_DOMAIN") !== -1) {
    wx.showToast({ title: "请先配置体验版接口域名", icon: "none" });
    return Promise.reject(new Error("release api domain is not configured"));
  }
  return new Promise((resolve, reject) => {
    const requestUrl = BASE_URL + url;
    if (wx.cloud && wx.cloud.callContainer) {
      wx.cloud.callContainer({
        config: { env: CLOUD_ENV },
        path: toContainerPath(requestUrl),
        method: "POST",
        data: data || {},
        header: {
          "content-type": "application/json",
          "X-WX-SERVICE": CLOUD_SERVICE
        },
        success(res) {
          if (res.data && res.data.code === 0) resolve(res.data.data);
          else reject(new Error((res.data && res.data.msg) || "AI request failed"));
        },
        fail: reject
      });
      return;
    }
    wx.request({
      url: requestUrl,
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
    const routes = {
      ershouliuzhuan: "/pkg-trade/ershouliuzhuan/detail",
      shiwuzhaoling: "/pkg-lost/shiwuzhaoling/detail",
      news: "/pkg-content/news-detail/news-detail"
    };
    const route = routes[type] || "/pages/" + type + "/detail";
    wx.navigateTo({ url: route + "?id=" + id });
  }
});
