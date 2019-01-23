# Import the flask forms module
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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
    password = PasswordField('Password', validators=[
        DataRequired()
        ])
    password_confirmation = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')
        ])
    submit = SubmitField('Register')

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

class SiteSelectionForm(FlaskForm):
    # Form field to choose the site to display data from
    site = SelectField('Choose the site from the drop down list', validators=[
        DataRequired()
        ], choices=[('High School', 'High School'),
                    ('Middle School', 'Middle School'),
                    ('North Elementary', 'North Elementary'),
                    ('South Elementary', 'South Elemtary'),
                    ('Early Childhood', 'Early Childhood')
        ])
    submit = SubmitField('Set Site')

# Create a student sign-in form class
class StudentSignInForm(FlaskForm):
    # Form fields with validators
    student_name = StringField('Student Name', validators=[
        DataRequired(),
        ])
    grade = SelectField('Grade', choices=[
        ('KG', 'Kindergarten'),
        ('01', 'First Grade'),
        ('02', 'Second Grade'),
        ('03', 'Third Grade'),
        ('04', 'Fourth Grade'),
        ('05', 'Fifth Grade'),
        ('06', 'Sixth Grade'),
        ('07', 'Seventh Grade'),
        ('08', 'Eighth Grade'),
        ('09', 'Ninth Grade'),
        ('10', 'Tenth Grade'),
        ('11', 'Eleventh Grade'),
        ('12', 'Twelfth Grade')
        ], validators=[
        DataRequired()
        ])
    parent = StringField('Parent/Guardian', validators=[
        DataRequired()
        ])
    reason = SelectField('Reason', choices=[
        ('Appointment', 'Appointment'),
        ('Family', 'Family'),
        ('Sick', 'Vacation'),
        ('Vacation', 'Vacation'),
        ('Other', 'Other')
    ], validators=[
        DataRequired()
    ])
    reason_other = StringField('If other, please explain the reason')
    submit = SubmitField('Sign-in')

# Create a student sign-in form class
class StudentSignOutForm(FlaskForm):
    # Form fields with validators
    student_name = StringField('Student Name', validators=[
        DataRequired(),
        ])
    grade = SelectField('Grade', choices=[
        ('KG', 'Kindergarten'),
        ('01', 'First Grade'),
        ('02', 'Second Grade'),
        ('03', 'Third Grade'),
        ('04', 'Fourth Grade'),
        ('05', 'Fifth Grade'),
        ('06', 'Sixth Grade'),
        ('07', 'Seventh Grade'),
        ('08', 'Eighth Grade'),
        ('09', 'Ninth Grade'),
        ('10', 'Tenth Grade'),
        ('11', 'Eleventh Grade'),
        ('12', 'Twelfth Grade')
        ], validators=[
        DataRequired()
        ])
    parent = StringField('Parent/Guardian', validators=[
        DataRequired()
        ])
    reason = SelectField('Reason', choices=[
        ('Appointment', 'Appointment'),
        ('Family', 'Family'),
        ('Sick', 'Sick'),
        ('Vacation', 'Vacation'),
        ('Other', 'Other')
    ], validators=[
        DataRequired()
    ])
    reason_other = StringField('If other, please explain the reason')
    submit = SubmitField('Sign-out')

# Create a visitor sign-in form class
class VisitorSignInForm(FlaskForm):
    # Form fields with validators
    visitor_name = StringField('Visitor Name', validators=[
        DataRequired(),
        ])
    student_name = StringField('Student Name', validators=[
        DataRequired(),
    ])
    grade = SelectField('Grade', choices=[
        ('KG', 'Kindergarten'),
        ('01', 'First Grade'),
        ('02', 'Second Grade'),
        ('03', 'Third Grade'),
        ('04', 'Fourth Grade'),
        ('05', 'Fifth Grade'),
        ('06', 'Sixth Grade'),
        ('07', 'Seventh Grade'),
        ('08', 'Eighth Grade'),
        ('09', 'Ninth Grade'),
        ('10', 'Tenth Grade'),
        ('11', 'Eleventh Grade'),
        ('12', 'Twelfth Grade')
        ], validators=[
        DataRequired()
        ])
    reason = SelectField('Reason', choices=[
        ('Classroom Visit', 'Classroom Visit'),
        ('Lunch With Student', 'Lunch With Student'),
        ('Meeting With Teacher', 'Meeting With Teacher'),
        ('Other', 'Other')
    ], validators=[
        DataRequired()
    ])
    reason_other = StringField('If other, please explain the reason')
    submit = SubmitField('Sign-in')

# Create a visitor sign-out form class
class VisitorSignOutForm(FlaskForm):
    # Form fields with validators
    visitor_name = StringField('Visitor Name', validators=[
        DataRequired(),
        ])
    submit = SubmitField('Sign-out')