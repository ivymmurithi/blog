from db import  app, db
from flask import render_template
from config import *
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)
migrate = Migrate(app,db)


@app.route('/')
def home():
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
    return dict(app=app,db=db)

if __name__ == '__main__':
    manager.run()