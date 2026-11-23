# 后端公网 HTTPS 部署方案

## 结论

手机体验版不能访问本机 `127.0.0.1:8080`。要让体验版正常使用，需要把 Flask 后端部署到公网 HTTPS 域名，例如：

```text
https://api.example.com/python7i67w282/
```

然后把该域名配置到微信公众平台的服务器域名中，并同步替换小程序代码里的体验版接口地址。

## 推荐方案

### 方案 A：云服务器 + 域名 + HTTPS

这是最稳定、最适合体验版/答辩演示的方案。

需要准备：

- 一台云服务器，系统建议 Ubuntu 22.04 或 24.04。
- 一个已备案、可配置 HTTPS 的域名。
- MySQL 8.0。
- Nginx。
- Python 运行环境。
- SSL 证书。

部署结构：

```text
手机微信体验版
  -> https://api.example.com/python7i67w282/
  -> Nginx 443
  -> 127.0.0.1:8080 Flask
  -> MySQL 3306
```

### 方案 B：微信云托管

如果没有服务器和域名，可以考虑微信云托管。优点是和小程序生态更贴近，缺点是需要把 Flask 项目按云托管要求整理成可部署服务。

适合后续正式上线，不是当前最小改动路径。

### 方案 C：临时内网穿透

Cloudflare Tunnel、ngrok、frp 等可以临时把本机服务暴露为 HTTPS 地址，但不建议作为提交体验版的长期方案。原因：

- 临时域名可能变动。
- 微信后台合法域名通常需要稳定域名。
- 部分临时域名不适合配置到微信服务器域名。
- 本机电脑关机或网络断开后服务不可用。

## 云服务器部署步骤

### 1. 上传项目

把项目上传到服务器，例如：

```text
/opt/campus-platform
```

后端目录：

```text
/opt/campus-platform/python7i67w282
```

### 2. 安装依赖

进入后端目录：

```bash
cd /opt/campus-platform/python7i67w282
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

### 3. 配置 MySQL

在服务器上创建数据库，并修改：

```text
python7i67w282/config.ini
```

确认数据库地址、端口、账号、密码和库名正确。

### 4. 启动后端

测试启动：

```bash
cd /opt/campus-platform/python7i67w282
source .venv/bin/activate
gunicorn -w 2 -b 127.0.0.1:8080 wsgi:app
```

项目已提供 `python7i67w282/wsgi.py`，用于生产部署。不要用 `run.py` 作为 gunicorn 入口，因为 `run.py` 会在导入时直接启动开发服务器。

### 5. 配置 Nginx

示例：

```nginx
server {
    listen 80;
    server_name api.example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/api.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/api.example.com/privkey.pem;

    client_max_body_size 50m;

    location /python7i67w282/ {
        proxy_pass http://127.0.0.1:8080/python7i67w282/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}
```

### 6. 配置微信公众平台合法域名

进入：

```text
微信公众平台 -> 开发管理 -> 开发设置 -> 服务器域名
```

配置：

```text
request 合法域名: https://api.example.com
uploadFile 合法域名: https://api.example.com
downloadFile 合法域名: https://api.example.com
```

注意：

- 这里只填域名，不填 `/python7i67w282/` 路径。
- 域名必须是 HTTPS。
- 不要填 IP、localhost、127.0.0.1。

### 7. 同步修改小程序代码

在项目根目录执行：

```bash
scripts/set_miniprogram_api_domain.sh https://api.example.com
```

脚本会同步修改：

```text
python7i67w282/api/templates/front/front/api/base.js
mp-weixin/common/vendor.js
mp-weixin/pages/ai-assistant/ai-assistant.js
docs/miniprogram-release-api-checklist.md
.ai-memory/current_status.md
.ai-memory/handoff.md
```

### 8. 重新上传体验版

在微信开发者工具中：

```text
重新编译 -> 上传 -> 体验版
```

手机端重新进入最新版体验版测试。

## 上线前验证地址

在电脑或手机浏览器中访问：

```text
https://api.example.com/python7i67w282/config/list
```

预期返回：

```json
{"code":0,"msg":"success",...}
```

再测试登录接口、图片上传接口和列表接口。
