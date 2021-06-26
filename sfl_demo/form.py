from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sfl_demo.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name",validators=[DataRequired(),Length(min=2, max=20)])
    last_name = StringField("Last Name",validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("Email address already exits, please use a different email")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')

class UploadPictureForm(FlaskForm):
    picture = FileField('Upload Picture', validators=[FileAllowed(['jpeg', 'png','jpg'])])
    submit = SubmitField('Upload')

