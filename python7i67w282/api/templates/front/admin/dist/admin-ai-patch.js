(function () {
  var BASE = "/python7i67w282/";
  var routeTimer = null;

  function token() {
    try {
      return (localStorage.getItem("Token") || "").replace(/^"|"$/g, "");
    } catch (error) {
      return "";
    }
  }

  function headers(extra) {
    var result = { "Content-Type": "application/json; charset=utf-8" };
    var t = token();
    if (t) result.Token = t;
    return Object.assign(result, extra || {});
  }

  function request(path, options) {
    var cfg = Object.assign({ credentials: "include", headers: headers() }, options || {});
    if (cfg.body && typeof cfg.body !== "string") cfg.body = JSON.stringify(cfg.body);
    return fetch(BASE + path, cfg).then(function (res) {
      return res.json().catch(function () {
        return { code: res.status, msg: res.statusText };
      });
    });
  }

  function getList(table, params) {
    var query = new URLSearchParams(Object.assign({ page: 1, limit: 1 }, params || {}));
    return request(table + "/list?" + query.toString()).then(function (data) {
      var page = data && data.data ? data.data : {};
      return {
        total: Number(page.total || 0),
        list: Array.isArray(page.list) ? page.list : []
      };
    }).catch(function () {
      return { total: 0, list: [] };
    });
  }

  function routeName() {
    var vueRoute = "";
    try {
      var app = document.querySelector("#app");
      vueRoute = app && app.__vue__ && app.__vue__.$route ? app.__vue__.$route.path : "";
    } catch (error) {}
    var hashRoute = location.hash || "#/";
    return (hashRoute || vueRoute || "#/")
      .replace(/^#?\/?/, "")
      .split("?")[0] || "home";
  }

  function markRoute() {
    document.body.className = document.body.className.replace(/\badmin-route-[^\s]+/g, "").trim();
    document.body.classList.add("admin-route-" + routeName().replace(/\W+/g, "-"));
    enforceWorkbenchLayout();
  }

  function routerView() {
    return document.querySelector(".router-view");
  }

  function enforceWorkbenchLayout() {
    ensureHomeAndWorkbenchNav();

    var aside = document.querySelector(".menu-preview");
    var sidebarWidth = 220;
    if (aside) {
      var fixedBox = aside.closest('[style*="fixed"]') || aside.closest(".el-aside") || aside.parentElement;
      var asideBox = fixedBox || aside.parentElement;
      if (asideBox) {
        asideBox.style.setProperty("width", sidebarWidth + "px", "important");
        asideBox.style.setProperty("min-width", sidebarWidth + "px", "important");
        asideBox.style.setProperty("left", "0", "important");
        asideBox.style.setProperty("box-sizing", "border-box", "important");
      }
    }

    document.querySelectorAll(".admin-main, .el-main").forEach(function (main) {
      main.style.setProperty("padding-left", "0", "important");
      main.style.setProperty("margin-left", sidebarWidth + "px", "important");
      main.style.setProperty("box-sizing", "border-box", "important");
      main.style.setProperty("overflow-x", "hidden", "important");
      main.style.setProperty("width", "calc(100% - " + sidebarWidth + "px)", "important");
      main.style.setProperty("max-width", "calc(100% - " + sidebarWidth + "px)", "important");
    });

    var view = routerView();
    if (view) {
      view.style.setProperty("box-sizing", "border-box", "important");
      view.style.setProperty("width", "calc(100% - 48px)", "important");
      view.style.setProperty("margin", "16px 24px 30px", "important");
      view.style.setProperty("padding", "0", "important");
      view.style.setProperty("max-width", "calc(100% - 48px)", "important");
      view.style.setProperty("overflow-x", "hidden", "important");
    }
  }

  function setMenuText(item, text) {
    if (!item) return;
    var span = item.querySelector("span[slot='title'], span");
    if (span) span.textContent = text;
  }

  function bindMenuRoute(item, hash, active) {
    if (!item || item.dataset.adminRouteBound === hash) return;
    item.dataset.adminRouteBound = hash;
    item.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      event.stopImmediatePropagation();
      location.hash = hash;
    }, true);
  }

  function ensureHomeAndWorkbenchNav() {
    var menu = document.querySelector(".menu-preview .el-menu-vertical-2");
    var first = menu && menu.querySelector(".el-menu-item.home");
    if (!menu || !first) return;

    setMenuText(first, "首页");
    first.setAttribute("index", "/");
    bindMenuRoute(first, "#/", routeName() === "home");

    var workbench = menu.querySelector(".admin-workbench-nav");
    if (!workbench) {
      workbench = first.cloneNode(true);
      workbench.classList.add("admin-workbench-nav");
      workbench.classList.remove("is-active");
      workbench.removeAttribute("data-admin-route-bound");
      first.parentNode.insertBefore(workbench, first.nextSibling);
    }
    setMenuText(workbench, "工作台");
    workbench.setAttribute("index", "/workbench");
    bindMenuRoute(workbench, "#/workbench", routeName() === "workbench");

    first.classList.toggle("is-active", routeName() === "home");
    workbench.classList.toggle("is-active", routeName() === "workbench");
  }

  function n(value) {
    return Number(value || 0).toLocaleString("zh-CN");
  }

  function money(value) {
    return "¥" + Number(value || 0).toLocaleString("zh-CN");
  }

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function metric(label, value, note) {
    return '<div class="admin-ai-metric"><span>' + label + '</span><strong>' + value + '</strong><small>' + note + '</small></div>';
  }

  function fallbackSummary() {
    return Promise.all([
      getList("ershouliuzhuan", { limit: 10000 }),
      getList("goumaidingdan", { limit: 10000 }),
      getList("shiwuzhaoling"),
      getList("renlingshenqing", { sfsh: "待审核" })
    ]).then(function (res) {
      var items = res[0].list || [];
      var orders = res[1].list || [];
      var paidOrders = orders.filter(function (item) { return item.ispay === "已支付"; });
      var unpaidOrders = orders.filter(function (item) { return item.ispay !== "已支付"; });
      return {
        secondhandCount: res[0].total,
        secondhandStock: items.reduce(function (sum, item) { return sum + Number(item.shuliang || 0); }, 0),
        orderCount: res[1].total,
        purchaseQuantity: orders.reduce(function (sum, item) { return sum + Number(item.shuliang || 0); }, 0),
        paidOrderCount: paidOrders.length,
        unpaidOrderCount: unpaidOrders.length,
        paidAmount: paidOrders.reduce(function (sum, item) { return sum + Number(item.jine || 0); }, 0),
        lostfoundCount: res[2].total,
        pendingClaimCount: res[3].total
      };
    });
  }

  function loadSummary() {
    return request("dashboard/summary", { method: "GET" }).then(function (data) {
      if (data && data.code === 0 && data.data) return data.data;
      return fallbackSummary();
    }).catch(fallbackSummary);
  }

  function renderDashboard() {
    var view = routerView();
    var currentRoute = routeName();
    if (!view || currentRoute !== "workbench") return;
    if (view.querySelector(".admin-ai-dashboard")) return;

    view.innerHTML = "";
    var box = document.createElement("section");
    box.className = "admin-ai-dashboard";
    box.innerHTML = [
      '<div class="admin-ai-hero">',
      '<div><h1>数据总览仪表盘</h1><p>汇总校园二手流转、订单支付、失物招领和待审核事项，方便后台运营和答辩展示。</p></div>',
      '<span class="admin-ai-badge">校园物品流转后台</span>',
      '</div>',
      '<div class="admin-ai-metrics" data-role="metrics">',
      metric("二手商品发布数", "...", "已发布商品总量") +
      metric("购买订单数", "...", "全部购买记录") +
      metric("购买总数量", "...", "订单购买数量汇总") +
      metric("已支付成交金额", "...", "仅统计已支付订单"),
      '</div>',
      '<div class="admin-ai-grid">',
      '<div class="admin-ai-card"><h2>订单状态概览</h2><div class="admin-ai-status" data-role="order-status"></div></div>',
      '<div class="admin-ai-card"><h2>待处理事项</h2><div class="admin-ai-list" data-role="todos"></div></div>',
      '</div>',
      '<div class="admin-ai-card"><h2>AI 辅助线索</h2><div class="admin-ai-list" data-role="ai"></div></div>'
    ].join("");
    view.appendChild(box);

    loadSummary().then(function (summary) {
      box.querySelector('[data-role="metrics"]').innerHTML =
        metric("二手商品发布数", n(summary.secondhandCount), "当前库存 " + n(summary.secondhandStock)) +
        metric("购买订单数", n(summary.orderCount), "全部购买记录") +
        metric("购买总数量", n(summary.purchaseQuantity), "订单 shuliang 汇总") +
        metric("已支付成交金额", money(summary.paidAmount), "已支付订单金额");

      box.querySelector('[data-role="order-status"]').innerHTML = [
        '<div><span>已支付订单</span><strong>' + n(summary.paidOrderCount) + '</strong></div>',
        '<div><span>未支付订单</span><strong>' + n(summary.unpaidOrderCount) + '</strong></div>',
        '<div><span>订单转化率</span><strong>' + (summary.orderCount ? Math.round(summary.paidOrderCount * 100 / summary.orderCount) : 0) + '%</strong></div>'
      ].join("");

      box.querySelector('[data-role="todos"]').innerHTML = [
        '<div class="admin-ai-item"><div class="admin-ai-item-title"><span>待审核认领申请</span><b>' + n(summary.pendingClaimCount) + '</b></div><p>建议优先核对申请说明、物品图片和联系方式。</p></div>',
        '<div class="admin-ai-item"><div class="admin-ai-item-title"><span>失物招领信息</span><b>' + n(summary.lostfoundCount) + '</b></div><p>可进入失物招领页运行 AI 匹配认领线索。</p></div>'
      ].join("");
    });

    request("ai/lostfound/match", { method: "GET" }).then(function (data) {
      var list = normalizeList(data).slice(0, 3);
      var html = list.map(function (item) {
        return '<div class="admin-ai-item"><div class="admin-ai-item-title"><span>' + escapeHtml(item.title || item.itemName || item.name || "高匹配线索") + '</span><b>' + escapeHtml(item.score || item.matchScore || "") + '</b></div><p>' + escapeHtml(item.reason || item.matchReason || "建议人工核验后再处理") + '</p></div>';
      }).join("");
      box.querySelector('[data-role="ai"]').innerHTML = html || '<div class="admin-ai-empty">暂无高匹配 AI 线索</div>';
    }).catch(function () {
      box.querySelector('[data-role="ai"]').innerHTML = '<div class="admin-ai-empty">AI 线索暂不可用，不影响统计数据查看</div>';
    });
  }

  function renderHomePage() {
    var view = routerView();
    if (!view || routeName() !== "home") return;
    if (view.querySelector(".admin-ai-home")) return;

    view.innerHTML = "";
    var box = document.createElement("section");
    box.className = "admin-ai-home";
    box.innerHTML = [
      '<div class="admin-ai-home-hero">',
      '<div class="admin-ai-home-copy">',
      '<p class="admin-ai-eyebrow">校园物品流转后台</p>',
      '<h1>基于小程序的校园物品流转平台</h1>',
      '<p>后台首页保留为清晰的业务入口。统计数据、待处理事项和 AI 辅助线索已拆分到“工作台”。</p>',
      '<div class="admin-ai-home-actions">',
      '<button class="admin-ai-btn" data-route="#/workbench">查看工作台</button>',
      '<button class="admin-ai-btn secondary" data-route="#/ershouliuzhuan">管理二手流转</button>',
      '<button class="admin-ai-btn secondary" data-route="#/shiwuzhaoling">管理失物招领</button>',
      '</div>',
      '</div>',
      '</div>',
      '<div class="admin-ai-home-grid">',
      '<button class="admin-ai-entry-card" data-route="#/yonghu"><span class="admin-ai-entry-icon">U</span><strong>用户管理</strong><p>查看用户资料、学生证图片和审核状态。</p></button>',
      '<button class="admin-ai-entry-card" data-route="#/ershouliuzhuan"><span class="admin-ai-entry-icon">S</span><strong>二手流转</strong><p>管理商品发布、库存、订单和交易状态。</p></button>',
      '<button class="admin-ai-entry-card" data-route="#/shiwuzhaoling"><span class="admin-ai-entry-icon">L</span><strong>失物招领</strong><p>处理失物信息、认领申请和 AI 匹配线索。</p></button>',
      '<button class="admin-ai-entry-card" data-route="#/news"><span class="admin-ai-entry-icon">C</span><strong>内容与配置</strong><p>维护校园动态、分类、敏感词和轮播配置。</p></button>',
      '</div>'
    ].join("");
    box.addEventListener("click", function (event) {
      var target = event.target.closest("[data-route]");
      if (target) location.hash = target.getAttribute("data-route");
    });
    view.appendChild(box);
  }

  function normalizeList(data) {
    if (!data) return [];
    if (Array.isArray(data)) return data;
    if (Array.isArray(data.data)) return data.data;
    if (data.data && Array.isArray(data.data.list)) return data.data.list;
    if (data.data && Array.isArray(data.data.matches)) return data.data.matches;
    if (Array.isArray(data.matches)) return data.matches;
    return [];
  }

  function showModal(title, content) {
    var old = document.querySelector(".admin-ai-modal-mask");
    if (old) old.remove();
    var mask = document.createElement("div");
    mask.className = "admin-ai-modal-mask";
    mask.innerHTML = '<div class="admin-ai-modal"><header><h3>' + escapeHtml(title) + '</h3><button class="admin-ai-btn secondary" data-close>关闭</button></header><main>' + content + '</main><footer><button class="admin-ai-btn" data-close>知道了</button></footer></div>';
    mask.addEventListener("click", function (event) {
      if (event.target === mask || event.target.hasAttribute("data-close")) mask.remove();
    });
    document.body.appendChild(mask);
  }

  function resultHtml(data) {
    var list = normalizeList(data);
    if (list.length) {
      return '<div class="admin-ai-list">' + list.slice(0, 8).map(function (item) {
        return '<div class="admin-ai-item"><div class="admin-ai-item-title"><span>' + escapeHtml(item.title || item.name || item.itemName || item.username || "AI 结果") + '</span><b>' + escapeHtml(item.score || item.matchScore || item.riskLevel || "") + '</b></div><p>' + escapeHtml(item.reason || item.matchReason || item.suggestion || item.explain || JSON.stringify(item)) + '</p></div>';
      }).join("") + '</div>';
    }
    var payload = data && data.data ? data.data : data;
    if (!payload || !Object.keys(payload).length) return '<div class="admin-ai-empty">接口已返回，但暂无可展示结果。</div>';
    return '<pre style="white-space:pre-wrap;margin:0;line-height:1.6;">' + escapeHtml(JSON.stringify(payload, null, 2)) + '</pre>';
  }

  function addPageTools() {
    var name = routeName();
    if (!/^(shiwuzhaoling|renlingshenqing|ershouliuzhuan|yonghu)$/.test(name)) return;
    var view = routerView();
    if (!view || view.querySelector(".admin-ai-page-tools")) return;
    var meta = {
      shiwuzhaoling: ["失物招领 AI 匹配", "根据失物和认领申请给出匹配线索，不自动通过审核。", runLostfound],
      renlingshenqing: ["认领申请 AI 审核提示", "抽取最近申请说明进行风险检测，管理员仍需人工确认。", runClaimModerate],
      ershouliuzhuan: ["二手流转 AI 风险检测", "检测押金、转账、验证码等风险表达，并生成推荐解释。", runSecondhand],
      yonghu: ["用户学生证 AI 验证", "对待审核用户的学生证图片进行 OCR 辅助验证。", runUserVerify]
    }[name];
    var bar = document.createElement("div");
    bar.className = "admin-ai-page-tools";
    bar.innerHTML = '<div><strong>' + meta[0] + '</strong><br><span>' + meta[1] + '</span></div><button class="admin-ai-btn">运行 AI</button>';
    bar.querySelector("button").addEventListener("click", function (event) {
      var btn = event.currentTarget;
      btn.disabled = true;
      btn.textContent = "分析中...";
      meta[2]().finally(function () {
        btn.disabled = false;
        btn.textContent = "运行 AI";
      });
    });
    view.prepend(bar);
  }

  function runLostfound() {
    return request("ai/lostfound/match", { method: "GET" }).then(function (data) {
      showModal("AI 匹配认领", resultHtml(data));
    });
  }

  function runClaimModerate() {
    return getList("renlingshenqing", { page: 1, limit: 1, sort: "addtime", order: "desc" }).then(function (page) {
      var item = page.list[0] || {};
      var text = [item.wupinmingcheng, item.shenqingshuoming, item.beizhu].filter(Boolean).join(" ");
      return request("ai/moderate", { method: "POST", body: { text: text || "暂无申请说明" } });
    }).then(function (data) {
      showModal("AI 审核提示", resultHtml(data));
    });
  }

  function runSecondhand() {
    return getList("ershouliuzhuan", { page: 1, limit: 1, sort: "addtime", order: "desc" }).then(function (page) {
      var item = page.list[0] || {};
      var text = [item.shangpinmingcheng, item.shangpinjieshao, item.jiaoyifangshi, item.miaoshu].filter(Boolean).join(" ");
      return Promise.all([
        request("ai/moderate", { method: "POST", body: { text: text || "暂无商品说明" } }),
        request("ai/recommend/explain", { method: "POST", body: { item: item } }).catch(function () { return null; })
      ]);
    }).then(function (res) {
      showModal("AI 风险检测/推荐解释", resultHtml(res[0]) + (res[1] ? '<hr style="border:0;border-top:1px solid #e5eaee;margin:16px 0;">' + resultHtml(res[1]) : ""));
    });
  }

  function runUserVerify() {
    return getList("yonghu", { page: 1, limit: 1, sfsh: "待审核" }).then(function (page) {
      var item = page.list[0] || {};
      return request("ai/student-card/verify", { method: "POST", body: { user: item, image: item.shenfenzheng || item.xueshengzheng || "" } });
    }).then(function (data) {
      showModal("AI 验证学生证", resultHtml(data));
    });
  }

  function apply() {
    markRoute();
    setTimeout(function () {
      renderHomePage();
      renderDashboard();
      addPageTools();
      enforceWorkbenchLayout();
    }, 180);
  }

  window.addEventListener("hashchange", function () {
    clearTimeout(routeTimer);
    routeTimer = setTimeout(apply, 120);
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", apply);
  } else {
    apply();
  }
  setTimeout(apply, 800);
  setInterval(enforceWorkbenchLayout, 1000);
})();
