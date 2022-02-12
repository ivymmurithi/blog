from db import  app, db
from flask import render_template
from config import *
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from models.user_class import User
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager
from flask_login import login_required

manager = Manager(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


@app.route('/')
def home():
    db.create_all()
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/posts')
def posts():
    return render_template('posts.html')


manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)

if __name__ == '__main__':
    manager.run()