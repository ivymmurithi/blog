import os

class Config:
    FLASK_APP = 'main.py'

class Prodconfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI']
    SECRET_KEY=os.environ['SECRET_KEY']


class Devconfig(Config):
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI']
    SECRET_KEY=os.environ['SECRET_KEY']

    DEBUG = True