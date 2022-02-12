from db import  app, db
from flask import render_template,redirect,url_for
from config import *
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from models.user_class import User
from forms import SignupForm,LoginForm
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager
from flask_login import login_required

manager = Manager(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_first_request
def create_user():
    db.create_all()


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/signup',methods=['GET','POST'])
def signup():

    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        first_name = signup_form.first_name.data
        last_name = signup_form.last_name.data
        email = signup_form.email.data
        password = signup_form.password.data

        hashed_password = generate_password_hash(password, method="sha256")

        new_user = User(first_name=first_name,last_name=last_name,email=email,password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html',signup_form=signup_form)


@app.route('/posts',methods=['GET','POST'])
@login_required
def posts():
    return render_template('posts.html')


manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)

if __name__ == '__main__':
    manager.run()