const fs = require('fs');
const path = require('path');

const adminDist = path.resolve(__dirname, '../api/templates/front/admin/dist');
const indexHtml = path.join(adminDist, 'index.html');
const appJs = path.join(adminDist, 'js/app.5c3ae10e.js');
const appCss = path.join(adminDist, 'css/app.0dd69b3a.css');
const adminPatchJs = path.join(adminDist, 'admin-ai-patch.js');

function replaceOnce(source, from, to, label) {
  if (!source.includes(from) && source.includes(to)) {
    return source;
  }
  if (!source.includes(from)) {
    throw new Error(`Pattern not found: ${label}`);
  }
  return source.replace(from, to);
}

let js = fs.readFileSync(appJs, 'utf8');

js = replaceOnce(
  js,
  '{path:"/",name:"系统首页",component:Fe,meta:{icon:"",title:"center",affix:!0}}',
  '{path:"/",redirect:"/workbench"},{path:"/workbench",name:"工作台",component:Fe,meta:{icon:"",title:"workbench",affix:!0}}',
  'workbench route'
);

js = js
  .replace(/padding:"0px 0 0 214px"/g, 'padding:"0px 0 0 220px"')
  .replace(/margin:"10px 0 0 30px",borderColor:"#3b6885",borderWidth:"0 0 0px 0",background:" #FFFFFF",width:"calc\(100% - 55px\)",fontSize:"16px",borderStyle:"solid"/g,
    'margin:"10px 20px 0",borderColor:"#3b6885",borderWidth:"0 0 0px 0",background:" #FFFFFF",width:"calc(100% - 40px)",fontSize:"16px",borderStyle:"solid",boxSizing:"border-box"')
  .replace(/attrs:\{"popper-append-to-body":!1,"popper-class":"home",index:"\/"\},nativeOn:\{click:function\(t\)\{return e\.menuHandler\(""\)\}\}/g,
    'attrs:{"popper-append-to-body":!1,"popper-class":"home",index:"/workbench"},nativeOn:{click:function(t){return e.menuHandler("workbench")}}')
  .replace(/"text":"系统首页"/g, '"text":"工作台"')
  .replace(/homeChange:function\(e\)\{this\.itemMenu=\[\],this\.title="",this\.currentIndex=e,this\.\$router\.push\(\{name:"home"\}\)\}/g,
    'homeChange:function(e){this.itemMenu=[],this.title="工作台",this.currentIndex=e,this.$router.push({name:"工作台"})}')
  .replace(/centerChange:function\(e\)\{this\.itemMenu=\[\{buttons:\["新增","查看","修改","删除"\],menu:"修改密码",tableName:"updatePassword"\},\{buttons:\["新增","查看","修改","删除"\],menu:"个人信息",tableName:"center"\}\],this\.title="",this\.currentIndex=e,this\.\$router\.push\(\{name:"home"\}\)\}/g,
    'centerChange:function(e){this.itemMenu=[{buttons:["新增","查看","修改","删除"],menu:"修改密码",tableName:"updatePassword"},{buttons:["新增","查看","修改","删除"],menu:"个人信息",tableName:"center"}],this.title="",this.currentIndex=e,this.$router.push({name:"工作台"})}');

fs.writeFileSync(appJs, js);

const cssPatch = '.admin-main{box-sizing:border-box;overflow-x:hidden;width:100%}.admin-main .el-header,.admin-main .bread-crumbs,.router-view{box-sizing:border-box;max-width:100%}.router-view{width:calc(100% - 40px);margin:16px 20px 30px}';
let css = fs.readFileSync(appCss, 'utf8');
if (!css.includes(cssPatch)) {
  css += `\n${cssPatch}\n`;
  fs.writeFileSync(appCss, css);
}

if (fs.existsSync(adminPatchJs)) {
  let patchJs = fs.readFileSync(adminPatchJs, 'utf8');
  patchJs = patchJs
    .replace('.split("?")[0] || "home";', '.split("?")[0] || "workbench";')
    .replace('if (!view || routeName() !== "home") return;', 'var currentRoute = routeName();\n    if (!view || (currentRoute !== "workbench" && currentRoute !== "home")) return;');
  fs.writeFileSync(adminPatchJs, patchJs);
}

if (fs.existsSync(indexHtml)) {
  let html = fs.readFileSync(indexHtml, 'utf8');
  const version = '2026052702';
  html = html
    .replace(/(\.\/css\/app\.0dd69b3a\.css)(?:\?v=\d+)?/g, `$1?v=${version}`)
    .replace(/(\.\/css\/chunk-vendors\.baab0025\.css)(?:\?v=\d+)?/g, `$1?v=${version}`)
    .replace(/(\.\/js\/app\.5c3ae10e\.js)(?:\?v=\d+)?/g, `$1?v=${version}`)
    .replace(/(\.\/js\/chunk-vendors\.54b6e1ea\.js)(?:\?v=\d+)?/g, `$1?v=${version}`)
    .replace(/(\.\/admin-ai-patch\.css)(?:\?v=\d+)?/g, `$1?v=${version}`)
    .replace(/(\.\/admin-ai-patch\.js)(?:\?v=\d+)?/g, `$1?v=${version}`);
  fs.writeFileSync(indexHtml, html);
}

console.log('admin dist patched: workbench route and sidebar layout');
