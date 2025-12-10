# -*- coding: utf-8 -*-

"""Flask应用入口文件"""
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from exts import db
from config import Config
from controller.contacts import bp as contacts_bp


def create_app(config_class=Config):
    """创建并配置Flask应用实例"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化扩展
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})  # 仅允许API路径的跨域请求

    # 注册蓝图
    app.register_blueprint(contacts_bp, url_prefix='/api')

    # 开发环境自动创建数据库表
    with app.app_context():
        db.create_all()

    return app


app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)