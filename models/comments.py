from db import db
from sqlalchemy.orm import relationship

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    posts_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = relationship("User", backref="comments")


    def __repr__(self):
        return f'Comment {self.comment}'