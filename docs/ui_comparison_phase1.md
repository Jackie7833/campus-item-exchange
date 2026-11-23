# 小程序 UI 改动对比文档（阶段 1）

阶段 1 完成 1-3：统一视觉基础、首页、二手流转列表。

阶段 2 继续完成剩余模块：失物招领列表、校园动态列表、详情页、个人中心和表单页。

## 1. 统一视觉基础

| 位置 | 修改前 | 修改后 |
| --- | --- | --- |
| 背景 | 模板浅灰和局部白底混用 | 统一为 `#f5f7f8` 页面背景 |
| 主色 | 蓝绿渐变、深蓝、灰色按钮混用 | 统一为校园工具感青绿色 `#13b8a7` |
| 圆角 | 8rpx、12rpx、20rpx 混用 | 常规控件统一 14-16rpx |
| 阴影 | 部分卡片阴影较重 | 改为低透明度轻阴影 |
| 字体 | 旧模板字号层级不稳定 | 统一为系统字体，标题加粗，正文偏紧凑 |

## 2. 首页

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 轮播图 | 全宽贴边，模板感明显 | 改为带留白的圆角横幅卡片 |
| 菜单入口 | 灰白渐变底，图标较散 | 白色入口面板，青绿色图标底，信息更集中 |
| 分区标题 | 使用外链标题背景图 | 去掉标题底图，改为干净标题 + 查看更多按钮 |
| 内容卡片 | 图片和文本间距较紧 | 卡片统一圆角、边框、轻阴影，图片固定比例 |

## 3. 二手流转列表

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 分类 | 左侧窄竖栏，占用商品展示空间 | 顶部横向分类标签，适合手机滑动 |
| 搜索 | 搜索按钮绝对定位，视觉压迫 | 搜索框和按钮统一高度，按钮主色固定 |
| 商品卡片 | 卡片宽度受左栏挤压，图片偏高 | 双列卡片固定宽度，图片高度降低，减少跳动 |
| 售出展示 | 数量为 0 时显示“已售出”但样式不突出 | 售出/数量行改为青绿色状态信息 |
| 返回顶部 | 保留原交互 | 保留按钮逻辑，仅统一视觉样式 |

## 4. 失物招领列表

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 图片展示 | 使用裁切模式，容易看不到完整物品 | 改为完整展示模式，图片背景统一浅灰，降低误判 |
| 卡片 | 标题、状态和图片距离偏紧 | 卡片增加内边距，标题和状态与图片分隔更清晰 |
| 筛选抽屉 | 旧模板边框和颜色不统一 | 统一圆角、阴影和主色按钮 |

## 5. 校园动态列表

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 分类 | 左侧窄栏占用阅读宽度 | 改为顶部横向标签，更适合新闻分类 |
| 新闻卡片 | 图片和正文排版紧，阴影偏重 | 统一白色卡片、轻阴影、固定图片比例 |
| 文本层级 | 标题和摘要区分不明显 | 标题加粗，摘要降低颜色权重 |

## 6. 详情页

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 顶部图片 | 直接铺满裁切 | 统一浅灰背景，商品/失物详情图片完整展示 |
| 字段信息 | 字段行边框重、标签靠右 | 改为白色信息组，标签左对齐，正文可换行 |
| 描述/评论 | 旧模板块感弱 | 描述和评论独立卡片化，评论按钮统一主色 |
| 底部操作 | 按钮样式混用 | 统一青绿色按钮和底部操作区阴影 |

## 7. 个人中心

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 用户信息 | 头像较小，设置和认证图标挤压 | 头像放大，认证图标和设置入口单独定位 |
| 我的服务 | 使用外链标题底图 | 去掉模板底图，改为干净标题 |
| 菜单 | 普通列表分割线较重 | 白色卡片、轻阴影、图标主色统一 |
| 修改密码 | 弹层输入框样式旧 | 输入框和按钮统一圆角与主色 |

## 8. 表单页

| 区域 | 修改前 | 修改后 |
| --- | --- | --- |
| 发布/编辑 | 表单贴边，字段分割线较重 | 表单整体白色卡片化，页面留白统一 |
| 输入控件 | 透明背景，层级不明显 | 输入框浅灰底、圆角边框 |
| 上传图片 | 80rpx 圆形缩略图不适合物品图片 | 改为 128rpx 圆角方图，更接近实际上传预览 |
| 提交按钮 | 渐变样式与其他页面混用 | 统一青绿色主按钮 |

## 已同步文件

- `python7i67w282/api/templates/front/front/App.vue`
- `python7i67w282/api/templates/front/front/pages/index/index.vue`
- `python7i67w282/api/templates/front/front/pages/ershouliuzhuan/list.vue`
- `mp-weixin/app.wxss`
- `mp-weixin/pages/index/index.wxss`
- `mp-weixin/pages/ershouliuzhuan/list.wxml`
- `mp-weixin/pages/ershouliuzhuan/list.wxss`
- `python7i67w282/api/templates/front/front/pages/shiwuzhaoling/list.vue`
- `python7i67w282/api/templates/front/front/pages/news/list.vue`
- `python7i67w282/api/templates/front/front/pages/center/center.vue`
- `python7i67w282/api/templates/front/front/pages/ershouliuzhuan/detail.vue`
- `python7i67w282/api/templates/front/front/pages/shiwuzhaoling/detail.vue`
- `python7i67w282/api/templates/front/front/pages/news-detail/news-detail.vue`
- `python7i67w282/api/templates/front/front/pages/ershouliuzhuan/add-or-update.vue`
- `python7i67w282/api/templates/front/front/pages/shiwuzhaoling/add-or-update.vue`
- `python7i67w282/api/templates/front/front/pages/news/add-or-update.vue`
- `python7i67w282/api/templates/front/front/pages/user-info/user-info.vue`
- `mp-weixin/pages/shiwuzhaoling/list.wxml`
- `mp-weixin/pages/shiwuzhaoling/list.wxss`
- `mp-weixin/pages/news/list.wxss`
- `mp-weixin/pages/center/center.wxss`
- `mp-weixin/pages/ershouliuzhuan/detail.wxss`
- `mp-weixin/pages/shiwuzhaoling/detail.wxss`
- `mp-weixin/pages/news-detail/news-detail.wxss`
- `mp-weixin/pages/ershouliuzhuan/add-or-update.wxss`
- `mp-weixin/pages/shiwuzhaoling/add-or-update.wxss`
- `mp-weixin/pages/news/add-or-update.wxss`
- `mp-weixin/pages/user-info/user-info.wxss`
