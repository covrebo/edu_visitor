from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

# Create a student sign-in form class
class StudentSignInForm(FlaskForm):
    # Form fields with validators
    student_name = StringField('Student Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
        ])
    grade = SelectField('Grade', choices=[
        ('EC', 'Early Chilhood'),
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
        DataRequired(),
        Length(min=2, max=50)
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
    reason_other = StringField('If other, please explain the reason', validators=[
        Length(max=120)
        ])
    submit = SubmitField('Sign-in')

# Create a student sign-out form class
class StudentSignOutForm(FlaskForm):
    # Form fields with validators
    student_name = StringField('Student Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
        ])
    grade = SelectField('Grade', choices=[
        ('EC', 'Early Chilhood'),
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
        DataRequired(),
        Length(min=2, max=50)
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
    reason_other = StringField('If other, please explain the reason', validators=[
        Length(max=120)
        ])
    submit = SubmitField('Sign-out')

# Create a student update form class
class StudentUpdateForm(FlaskForm):
    # Form fields with validators
    student_name = StringField('Student Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
        ])
    grade = SelectField('Grade', choices=[
        ('EC', 'Early Chilhood'),
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
        DataRequired(),
        Length(min=2, max=50)
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
    reason_other = StringField('If other, please explain the reason', validators=[
        Length(max=120)
        ])
    direction = SelectField('Direction', choices=[
        ('In', 'Entry'),
        ('Out', 'Exit')
    ], validators=[
        DataRequired()
    ])
    submit = SubmitField('Update')

# Create a visitor sign-in form class
class VisitorSignInForm(FlaskForm):
    # Form fields with validators
    visitor_name = StringField('Visitor Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
        ])
    student_name = StringField('Student Name', validators=[
        DataRequired()
    ])
    grade = SelectField('Grade', choices=[
        ('EC', 'Early Chilhood'),
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
    reason_other = StringField('If other, please explain the reason', validators=[
        Length(max=120)
        ])
    submit = SubmitField('Sign-in')

# Create a visitor sign-out form class
class VisitorSignOutForm(FlaskForm):
    # Form fields with validators
    visitor_name = StringField('Visitor Name', validators=[
        DataRequired(),
        ])
    submit = SubmitField('Sign-out')

# Create a visitor sign-in update form class
class VisitorUpdateForm(FlaskForm):
    # Form fields with validators
    visitor_name = StringField('Visitor Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
        ])
    student_name = StringField('Student Name', validators=[
        DataRequired()
    ])
    grade = SelectField('Grade', choices=[
        ('EC', 'Early Chilhood'),
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
    reason_other = StringField('If other, please explain the reason', validators=[
        Length(max=120)
        ])
    direction = SelectField('Direction', choices=[
        ('In', 'Entry'),
        ('Out', 'Exit')
    ], validators=[
        DataRequired()
    ])
    submit = SubmitField('Update')