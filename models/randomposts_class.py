from db import db

class Random(db.Model):
    __tablename__ = 'random'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255))
    quote = db.Column(db.String(255))

    def __repr__(self):
        return f'User{self.author}'