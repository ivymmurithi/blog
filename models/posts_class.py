from db import db
from sqlalchemy.orm import relationship
from .user_class import User

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    posts = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = relationship("User", backref="posts")

    def __repr__(self):
        return f'Posts {self.posts}'