from db import  app, db
from flask import render_template,redirect,url_for,session
from config import *
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from models.user_class import User
from forms import SignupForm,LoginForm
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager, login_user
from flask_login import login_required
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
manager = Manager(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/',methods=['GET','POST'])
def home():
    db.create_all()
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username = login_form.username.data).first()

        if user:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user, remember=True)
                session["user_id"] = user.id
                session["email"]
                return redirect(url_for('posts'))

    return render_template('login.html', login_form= login_form)


@app.route('/signup',methods=['GET','POST'])
def signup():

    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        first_name = signup_form.first_name.data
        last_name = signup_form.last_name.data
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data

        hashed_password = generate_password_hash(password, method="sha256")

        new_user = User(first_name=first_name,last_name=last_name,username=username,email=email,password=hashed_password)

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
    return dict(app=app,db=db)

if __name__ == '__main__':
    manager.run()