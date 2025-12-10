"""数据模型定义"""
from datetime import datetime

from exts import db


class UserModel(db.Model):
    """联系人模型"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, comment='联系人姓名')
    # 主联系电话与地址保留以兼容旧数据，允许为空
    phone_number = db.Column(db.String(50), nullable=True, comment='主联系电话')
    address = db.Column(db.String(255), nullable=True, comment='主联系地址')
    is_favorite = db.Column(db.Boolean, default=False, nullable=False, comment='是否收藏')
    join_time = db.Column(
        db.DateTime,
        default=datetime.now,
        comment='创建时间'
    )

    # 联系方式列表
    contact_methods = db.relationship(
        'ContactMethodModel',
        backref='user',
        cascade='all, delete-orphan',
        lazy='joined'
    )

    def to_dict(self):
        """将模型实例转换为字典"""
        return {
            'id': self.id,
            'username': self.username,
            'phone_number': self.phone_number,
            'address': self.address,
            'is_favorite': self.is_favorite,
            'join_time': self.join_time.strftime('%Y-%m-%d %H:%M:%S'),
            'contact_methods': [method.to_dict() for method in self.contact_methods],
        }


class ContactMethodModel(db.Model):
    """联系人多种联系方式"""
    __tablename__ = 'contact_method'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    contact_type = db.Column(db.String(50), nullable=False, comment='联系方式类型：phone/email/social/address/other')
    value = db.Column(db.String(255), nullable=False, comment='联系方式详情')
    label = db.Column(db.String(100), nullable=True, comment='备注或标签')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'type': self.contact_type,
            'value': self.value,
            'label': self.label or ''
        }