from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Devconfig, Prodconfig


app = Flask(__name__)
app.config.from_object(Prodconfig)
db = SQLAlchemy(app)

