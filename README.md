# 校园物品流转平台

项目提供校园二手流转、失物招领、认领审核、校园资讯和管理后台。

| 路径 | 内容 |
| --- | --- |
| `mp-weixin/` | 可导入微信开发者工具的小程序项目 |
| `python7i67w282/api/templates/front/front/` | uni-app 前端源码 |
| `python7i67w282/api/templates/front/admin/` | Vue 管理后台源码及 Flask 直接使用的构建产物 |
| `python7i67w282/` | Flask API、MySQL 表结构和部署配置 |
| `docs/` | 项目设计与部署说明 |

## 本地运行

1. 在 `python7i67w282/` 中用 Python 3.9 创建虚拟环境，并安装 `requirements-cloud.txt` 中的依赖。
2. 将 `config.ini.example` 复制为 `config.ini`，填写本机 MySQL 连接信息。
3. 在一个新建的数据库中导入 `db/mysql.sql`。此脚本包含删表并重建表结构的语句。初始化后需要自行创建测试账号和演示数据。
4. 在 `python7i67w282/` 中运行 `python run.py`，通过 `http://localhost:8080/admin` 打开管理后台。
5. 用微信开发者工具导入 `mp-weixin/`，按照 [小程序 API 配置说明](docs/miniprogram-release-api-checklist.md) 设置后端地址。

仓库提供空表结构。部署文档中提到的演示数据快照需要从原项目环境获取。
