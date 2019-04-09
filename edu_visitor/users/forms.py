from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from edu_visitor.models import Users
from flask_login import current_user

# Create a registration form class
class RegistrationForm(FlaskForm):
    # Form fields with validators
    user_first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(min=2, max=30)
    ])
    user_last_name = StringField('Last Name', validators=[
        DataRequired(),
        Length(min=2, max=30)
    ])
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=20)
        ])
    email =  StringField('Email', validators=[
        DataRequired(),
        Email()
        ])
    role = SelectField('Role', choices=[
        ('staff', 'Staff'),
        ('admin', 'Administrator')
        ], validators=[
        DataRequired()
        ])
    building = SelectField('Default Building', choices=[
        ('High School', 'High School'),
        ('Middle School', 'Middle School'),
        ('North Elementary', 'North Elementary'),
        ('South Elementary', 'South Elementary'),
        ('Early Childhood', 'Early Childhood')
        ], validators=[
        DataRequired()
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
        ])
    password_confirmation = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')
        ])
    submit = SubmitField('Register')

    # Function to validate the unique username before submitting the form
    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose another.')

    # Function to validate the unique username before submitting the form
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please choose another.')

# Create a login form class
class LoginForm(FlaskForm):
    # Form fields with validators
    email =  StringField('Email', validators=[
        DataRequired(),
        Email()
        ])
    password = PasswordField('Password', validators=[
        DataRequired()
        ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# Create an account update form class
class UpdateAccountForm(FlaskForm):
    # Form fields with validators
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=20)
        ])
    email =  StringField('Email', validators=[
        DataRequired(),
        Email()
        ])
    building = SelectField('Default Building', choices=[
        ('High School', 'High School'),
        ('Middle School', 'Middle School'),
        ('North Elementary', 'North Elementary'),
        ('South Elementary', 'South Elementary'),
        ('Early Childhood', 'Early Childhood')
        ], validators=[
        DataRequired()
    ])
    picture = FileField('Update Profile Picture', id="file-upload", validators=[
        FileAllowed(['jpg', 'png'])
    ])
    submit = SubmitField('Update')

    # Function to validate the unique username before submitting the form
    def validate_username(self, username):
        if username.data != current_user.username:
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, please choose another.')

    # Function to validate the unique username before submitting the form
    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken, please choose another.')

# A form to request a password reset email
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    submit = SubmitField('Request Password Reset')

    # Function to validate the email before submitting the form
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('This email does not exist in our records, please register for an account.')

# A form to reset a password
class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired()
    ])
    password_confirmation = PasswordField('Confirm New Password', validators=[
        DataRequired(),
        EqualTo('password')
    ])
    submit = SubmitField('Reset Password')