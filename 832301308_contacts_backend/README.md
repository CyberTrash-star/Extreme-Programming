# 联系人管理系统后端

一个基于Flask框架开发的联系人管理系统后端API，提供联系人的增删改功能，支持跨域请求，
采用MySQL数据库存储数据。

## 功能特点
- 联系人信息（姓名、电话、地址）的添加、更新、删除
- 支持跨域请求（CORS）
- 完善的日志记录

## 技术栈
- 框架：Flask
- ORM：Flask-SQLAlchemy
- 数据库：MySQL
- 部署：Gunicorn
- 其他：Flask-Migrate（数据库迁移）、Flask-CORS（跨域支持）

## 环境要求
- Python 3.6+
- MySQL 5.7+

## 项目后端结构
    src/
    ├── app.py              # Flask应用入口
    ├── config.py           # 应用配置
    ├── exts.py             # 扩展实例化
    ├── models.py           # 数据模型定义
    ├── controller/         # 控制器目录
    │   └── contacts.py     # 联系人相关接口实现
    ├── gunicorn_conf.py    # Gunicorn配置文件