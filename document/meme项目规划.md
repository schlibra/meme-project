# meme 梗图展示项目
## 前端
前端采用vue.js作为项目语言框架，组件库使用Element-Plus
### 页面规划
- [ ] 首页 ( / )
  - [x] 标题(顶部居中位置，可以加上打字效果)
  - [x] 标题下方操作按钮
    - [x] 随机图片：点击后随机展示一张图片，通过弹窗显示
    - [x] 登录按钮：跳转至登录页面
    - [x] 个人中心：跳转至个人中心页面
    - [x] 上传图片：用于上传梗图
    - [x] 系统设置：设置站点相关信息，仅管理员可见
  - [x] 图片展示区域
    - [x] 图片列表：使用网格布局展示图片，每页显示固定数量的图片，底部有分页条
    - [ ] 图片预览：点击图片列表中某个图片时弹出图片预览弹窗，图片下方显示图片描述，左右箭头可切换上一张/下一张图
- [x] 登录页面 ( /login )
  - [x] 标题：登录页面标题
  - [x] 登录表单：账号密码输入框，账号输入框支持用户名/邮箱
  - [x] 表单下方双链接：忘记密码，注册账号
  - [x] 提交按钮：登录
- [x] 注册页面 ( /register )
- [x] 忘记密码页面 ( /forget )
- [ ] 用户中心页面 ( /user )
- [ ] 系统设置页面 ( /admin )
  - [ ] 系统设置基本信息 ( /admin/basic )
  - [ ] 系统设置用户列表 ( /admin/user )
  - [ ] 系统设置图片列表 ( /admin/pics )

## 后端
后端采用thinkphp框架进行开发
### 后端规划
- [ ] 用户部分
  - [x] 登录
  - [x] 注册
  - [x] 获取用户信息
  - [x] 忘记密码
  - [ ] 更新用户信息
- [ ] 图片部分
  - [ ] 图片列表，分页
  - [ ] 图片详情
  - [ ] 图片评分
  - [ ] 图片评论
  - [ ] 图片删除
- [ ] 系统设置
  - [ ] 系统基本信息
  - [ ] 用户列表
  - [ ] 用户组列表
  - [ ] 安全设置

## 数据库
数据库采用MySQL进行存储
### 数据表规划
- 用户表 ( user )

| 字段名 | 类型 | 必填 | 描述 | 示例 | 备注 |
| --- | --- | --- | --- | --- | --- |
| id | int | 是 | 用户id | 1 | 自动生成 |
| username | varchar(50) | 是 | 用户名 | user | |
| password | longtext | 是 | 密码 | | BC加密后的内容 |
| nickname | varchar(50) | 否 | 昵称 | 用户 | |
| email | varchar(50) | 是 | 邮箱 | user@example.com | |
| create | datetime | 是 | 创建时间 | NOW() |  |
| group | int | 是 | 用户组 | 1 | 关联表group |
| ban | varchar(1) | 是 | 用户封禁 | Y | 封禁为Y，正常为N |
| reason | varchar(100) | 否 | 封禁原因 | 违规封禁 | ban为Y时需要设置改数据 |
| birth | int | 否 | 出生年份 | 2004 |  |
| sex | varchar(10) | 否 | 性别 | 男 |  |
| description | varchar(500) | 否 | 个人介绍 |  |  |

- 用户组表 (group)

| 字段名 | 类型 | 必填 | 描述 | 示例 | 备注 |
| --- | --- | --- | --- | --- | --- |
| id | int | 是 | 用户组id | 1 | 自动生成 |
| name | varchar(30) | 是 | 用户组名称 | 管理员组 | |
| admin | varchar(1) | 是 | 是否管理员 | Y | |
| upload | varchar(1) | 是 | 允许上传图片 | Y | |
| deletePic | varchar(1) | 是 | 允许删除图片 | Y | 只能删除自己上传的图片 |
| deleteComment | varchar(1) | 是 | 允许删除评论 | Y | 只能删除自己发布的评论 |
| updateComment | varchar(1) | 是 | 允许修改评论 | Y | |
| comment | varchar(1) | 是 | 允许评论 | Y | |
| score | varchar(1) | 是 | 允许评分 | Y | |
| updateScore | varchar(1) | 是 | 允许修改评分 | Y | |
| deleteScore | varchar(1) | 是 | 允许删除评分 | Y | |
| create | datetime | 是 | 创建时间 | | |
| update | datetime | 是 | 修改时间 | | |

- 图片列表 (pics)

| 字段名 | 类型 | 必填 | 描述 | 示例 | 备注 |
| --- | --- | --- | --- | --- | --- |
| id | int | 是 | 数据id | 1 | 自动生成 |
| name | varchar(50) | 是 | 图片名称 | 图片名称 | |
| description | varchar(100) | 是 | 图片描述 | 图片描述 | |
| user | int | 是 | 上传者id | 1 | 关联表user |
| data | longtext | 是 | 图片数据 |  |  |
| type | varchar(50) | 是 | 文件类型 | | |
| create | datetime | 是 | 上传时间 | | |
| verified | varchar(1) | 是 | 图片审核通过 | Y | |
| update | datetime | 是 | 修改时间 |  | |
| delete | datetime | 否 | 删除时间 |  | |

- 评分列表 (score)

| 字段名 | 类型 | 必填 | 描述 | 示例 | 备注 |
| --- | --- | --- | --- | --- | --- |
| id | int | 是 | 数据id | 1 | 自动生成 |
| pic | int | 是 | 图片id | 1 | 关联表pics |
| user | int | 是 | 用户id | 1 | 关联表user |
| score | float | 是 | 评分 | 5 | |
| create | datetime | 是 | 创建时间 |  | |
| update | datetime | 是 | 修改时间 |  | |

- 评论列表 (comment)

| 字段名 | 类型 | 必填 | 描述 | 示例 | 备注 |
| --- | --- | --- | --- | --- | --- |
| id | int | 是 | 数据id | 1 | 自动生成 |
| pic | int | 是 | 图片id | 1 | 关联表pics |
| user | int | 是 | 用户id | 1 | 关联表user |
| parent | int | 是 | 父级评论id | 0 | 0表示当前评论最高级 |
| reply | int | 否 | 回复用户id | 0 | 0表示当前评论最高级 |
| comment | varchar(500) | 是 | 评论内容 | 评论内容 | |
| create | datetime | 是 | 发布时间 | | |
| verified | varchar(1) | 是 | 评论通过审核 | Y | |
| update | datetime | 是 | 更新时间 | | |
| delete | datetime | 否 | 删除时间 |  | |
