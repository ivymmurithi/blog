import os

class Config:
    FLASK_APP = 'main.py'

class Prodconfig(Config):
    pass


class Devconfig(Config):
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI']

    DEBUG = True