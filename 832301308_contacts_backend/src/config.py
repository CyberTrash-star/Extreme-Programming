"""应用配置文件"""
import os
from datetime import timedelta


class Config:
    """基础配置类"""
    # 数据库配置
    HOSTNAME = os.environ.get('DB_HOST', '127.0.0.1')
    PORT = os.environ.get('DB_PORT', '3306')
    DATABASE = os.environ.get('DB_NAME', 'mydata')
    USERNAME = os.environ.get('DB_USER', 'mydata')
    PASSWORD = os.environ.get('DB_PASSWORD', 'ZtmejirrzzkiFeXf')

    # 构建数据库URI
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # 其他配置
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-development-only')
    JSON_SORT_KEYS = False