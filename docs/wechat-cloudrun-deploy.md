# 微信云托管 / 云开发部署方案

## 为什么选云托管

微信云托管可以托管后端容器服务，并提供 HTTPS 访问能力。相比自己购买云服务器、域名、备案和手动配置 Nginx，云托管对小程序体验版更友好。

本项目已经补齐云托管部署所需文件：

```text
python7i67w282/Dockerfile
python7i67w282/.dockerignore
python7i67w282/requirements-cloud.txt
python7i67w282/wsgi.py
python7i67w282/cloudrun.env.example
```

并且 `configs.py` 已支持用环境变量配置 MySQL，适合云环境部署。

## 推荐部署结构

```text
微信小程序体验版
  -> 微信云托管 HTTPS 服务域名
  -> Flask 容器服务
  -> 云托管 MySQL / 腾讯云 MySQL
```

## 操作步骤

### 1. 进入微信公众平台

打开：

```text
微信公众平台 -> 开发管理 -> 云开发
```

如果还没有云开发环境，先开通一个环境。

### 2. 创建云托管服务

进入云开发控制台后：

```text
云托管 -> 新建服务
```

建议：

```text
服务名：campus-api
端口：8080
部署方式：Dockerfile
代码目录：python7i67w282
```

### 3. 准备 MySQL

后端依赖 MySQL，云托管容器不能只靠本机数据库。你需要准备一个云端 MySQL：

- 微信云托管提供的 MySQL 能力，或
- 腾讯云 MySQL / 云数据库 MySQL。

创建数据库：

```text
python7i67w282
```

然后导入项目 SQL 数据。当前项目 SQL 文件在：

```text
python7i67w282/db/python7i67w282.sql
python7i67w282/db/campus_demo_update.sql
python7i67w282/db/demo_student_identity_update.sql
python7i67w282/db/fix_secondhand_images_v2.sql
python7i67w282/db/restore_campus_avatar_update.sql
```

建议先导入 `python7i67w282.sql`，再按需要执行演示数据更新脚本。

### 4. 配置环境变量

在云托管服务的环境变量中配置：

```text
PORT=8080
APP_HOST=0.0.0.0
SQL_TYPE=mysql
SQL_HOST=你的云数据库内网地址
SQL_PORT=3306
SQL_USER=数据库账号
SQL_PASSWORD=数据库密码
SQL_DATABASE=python7i67w282
```

这些变量对应：

```text
python7i67w282/cloudrun.env.example
```

### 5. 部署服务

选择 `python7i67w282` 目录作为服务代码目录，使用其中的 `Dockerfile` 构建。

部署完成后，云托管会提供一个 HTTPS 访问地址。最终接口应类似：

```text
https://你的云托管域名/python7i67w282/config/list
```

打开该地址，如果返回：

```json
{"code":0,"msg":"success",...}
```

说明后端部署成功。

### 6. 同步小程序接口地址

拿到云托管 HTTPS 域名后，在项目根目录执行：

```bash
scripts/set_miniprogram_api_domain.sh https://你的云托管域名
```

注意只传域名，不带 `/python7i67w282/`。

脚本会把小程序体验版接口改成：

```text
https://你的云托管域名/python7i67w282/
```

### 7. 微信后台服务器域名

如果使用云托管提供的小程序免域名访问能力，可以按云托管控制台提示处理。

如果你使用云托管的 HTTPS 公网访问域名，并且微信后台要求配置服务器域名，则在：

```text
开发管理 -> 开发设置 -> 服务器域名
```

填写：

```text
request 合法域名：https://你的云托管域名
uploadFile 合法域名：https://你的云托管域名
downloadFile 合法域名：https://你的云托管域名
```

微信后台这里只填域名，不填 `/python7i67w282/`。

## 注意事项

- 云托管容器文件系统通常不适合长期保存上传文件。第一版演示可以继续使用当前上传接口；正式上线建议迁移到云存储。
- 当前项目图片路径很多是 `upload/xxx.jpg`。如果云端没有这些文件，列表图片会缺失，需要同步上传目录或改为云存储。
- 部署前要确保数据库中演示数据和图片资源路径一致。
- 不要把真实数据库密码写进代码文件，使用云托管环境变量。
- 如果云托管控制台提供“公网访问地址”，可以把该 HTTPS 地址作为小程序接口域名同步到代码。
- 如果选择 `wx.cloud.callContainer` 免域名调用，需要额外改造小程序请求层和上传/图片访问逻辑；当前项目优先走云托管 HTTPS 访问地址，改动最小。

## 本地验证

本机后端当前可通过：

```bash
curl http://127.0.0.1:8080/python7i67w282/config/list
```

验证基础接口是否可用。云托管部署后，改用云托管 HTTPS 地址验证。
