from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,BooleanField,HiddenField
from wtforms.validators import InputRequired,Email,Length
from wtforms import ValidationError
from models.user_class import User

class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[InputRequired()])
    password = PasswordField(label='Password',validators = [InputRequired(), Length(min=5, max = 50)])
    submit = SubmitField(label='Login')


class SignupForm(FlaskForm):
    first_name = StringField(label='First Name',validators=[InputRequired()])
    last_name = StringField(label=' Last Name',validators=[InputRequired()])
    username = StringField(label='Username',validators=[InputRequired()])
    email = EmailField(label='Email',validators=[InputRequired(),Email(message = 'Invalid Email')])
    password = PasswordField(label='Password',validators = [InputRequired(),Length(min=5, max=50)])
    submit = SubmitField(label='Sign Up')
    def validate_email(form,email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email exists')

class PostsForm(FlaskForm):
    posts = StringField(label='Add post',validators=[InputRequired(), Length(min=10, max=100)])
    user_id = HiddenField(label='user_id')
    submit = SubmitField(label='Submit')

class CommentsForm(FlaskForm):
    comment = StringField(label='comment')