import sqlite3
from db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        user = cls.query.filter_by(id=_id).first()
        return user

    def save(self):
        db.session.add(self)
        db.session.commit()