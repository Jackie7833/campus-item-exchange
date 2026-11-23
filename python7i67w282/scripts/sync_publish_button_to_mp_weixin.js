const fs = require("fs");

const buttonByScope = {
  ershouliuzhuan: "data-v-20a32d60",
  shiwuzhaoling: "data-v-2ecd35bc",
};

function publishButton(scope) {
  return `<button data-event-opts="{{[['tap',[['onAddTap']]]]}}" class="add-btn publish-btn ${scope}" style="{{'border:'+('0')+';'+('box-shadow:'+('0 2rpx 12rpx rgba(0,0,0,.3)')+';')+('margin:'+('20rpx 0 0 20rpx')+';')+('color:'+('rgb(255, 255, 255)')+';')+('outline:'+('none')+';')+('border-radius:'+('20rpx')+';')+('background:'+('linear-gradient( 104deg, #489DF3 0%, #28CBB6 100%)')+';')+('width:'+('120rpx')+';')+('line-height:'+('70rpx')+';')+('font-size:'+('28rpx')+';')+('position:'+('relative')+';')+('height:'+('70rpx')+';')+('z-index:'+('1')+';')+('order:'+('3')+';')}}" bindtap="__e">发布</button>`;
}

for (const [page, scope] of Object.entries(buttonByScope)) {
  const wxmlPath = `mp-weixin/pages/${page}/list.wxml`;
  let wxml = fs.readFileSync(wxmlPath, "utf8");
  const buttonPattern = /<block wx:if="\{\{\$root\.m3\}\}"><button[^<]*>新增<\/button><\/block><block wx:if="\{\{\$root\.m4\}\}"><button[^<]*>新增<\/button><\/block>/;
  if (!buttonPattern.test(wxml) && !wxml.includes(">发布</button>")) {
    throw new Error(`publish button target not found in ${wxmlPath}`);
  }
  wxml = wxml.replace(buttonPattern, publishButton(scope));
  fs.writeFileSync(wxmlPath, wxml);

  const jsPath = `mp-weixin/pages/${page}/list.js`;
  let js = fs.readFileSync(jsPath, "utf8");
  js = js.replace(/\n  var m3 = _vm\.userid && _vm\.isAuth\("[^"]+", "新增"\)\n  var m4 = !_vm\.userid && _vm\.isAuthFront\("[^"]+", "新增"\)/, "");
  js = js.replace(/\n        m3: m3,\n        m4: m4,/, "");
  const oldAddTap = `    onAddTap: function onAddTap() {
      uni.setStorageSync("useridTag", this.userid);
      this.$utils.jump("./add-or-update");
    },`;
  const newAddTap = `    onAddTap: function onAddTap() {
      if (!uni.getStorageSync("appUserid")) {
        this.$utils.msg('请先登录');
        setTimeout(() => {
          this.$utils.jump('../login/login');
        }, 800);
        return;
      }
      uni.setStorageSync("useridTag", this.userid);
      this.$utils.jump("./add-or-update");
    },`;
  if (!js.includes(newAddTap)) {
    if (!js.includes(oldAddTap)) throw new Error(`onAddTap target not found in ${jsPath}`);
    js = js.replace(oldAddTap, newAddTap);
  }
  fs.writeFileSync(jsPath, js);
}
