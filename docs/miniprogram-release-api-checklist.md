# 小程序体验版接口配置检查

## 问题原因

体验版安装到手机后，请求发生在手机端，不是在开发电脑上。因此下面这类地址不能用于体验版或正式版：

- `http://127.0.0.1:8080/python7i67w282/`
- `http://localhost:8080/python7i67w282/`
- 局域网 IP 的 HTTP 地址

微信体验版和正式版还会校验 request/uploadFile 合法域名。后端必须部署到公网可访问的 HTTPS 域名，并在微信公众平台配置合法域名。

## 当前代码处理

已将接口地址改为环境分流：

- 开发版：`http://127.0.0.1:8080/python7i67w282/` 或 `http://localhost:8080/python7i67w282/`
- 体验版/正式版：`https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/`

当前已替换为云托管公网 HTTPS 域名。

## 需要替换的位置

1. 源码：

```text
python7i67w282/api/templates/front/front/api/base.js
```

2. 微信开发者工具直接预览/上传目录：

```text
mp-weixin/common/vendor.js
mp-weixin/pages/ai-assistant/ai-assistant.js
```

把：

```text
https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/
```

替换为你的后端公网地址，例如：

```text
https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/
```

## 微信公众平台配置

进入微信公众平台：

```text
开发管理 -> 开发设置 -> 服务器域名
```

至少配置：

- request 合法域名：`https://api.example.com`
- uploadFile 合法域名：`https://api.example.com`
- downloadFile 合法域名：如果图片或文件也走同一域名，也配置 `https://api.example.com`

域名要求：

- 必须是 HTTPS。
- 证书必须有效。
- 不能带端口。
- 不能是 IP、localhost、127.0.0.1。
- 路径 `/python7i67w282/` 不填在微信后台域名里，只写域名。

## 后端要求

后端需要部署到公网服务器，并保证以下地址手机网络可访问：

```text
https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/config/list
https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/yonghu/login
https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/file/upload
```

如果后端仍然只跑在本机 `127.0.0.1:8080`，体验版无法正常使用。

## 重新上传体验版前检查

- 已替换为云托管公网 HTTPS 域名。
- 后端公网 HTTPS 可以访问。
- 微信公众平台合法域名已配置并保存。
- 微信开发者工具重新编译。
- 重新上传体验版。
- 手机上删除旧体验版或重新进入最新体验版。
