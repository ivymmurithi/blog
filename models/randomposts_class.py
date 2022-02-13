from db import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255))
    quote = db.Column(db.String(255))
    permalink = db.Column(db.Varchar)

    def __repr__(self):
        return f'User{self.username}'