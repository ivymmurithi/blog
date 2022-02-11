from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Devconfig


app = Flask(__name__)
app.config.from_object(Devconfig)
db = SQLAlchemy(app)

