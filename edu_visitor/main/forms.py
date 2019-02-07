from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

class SiteSelectionForm(FlaskForm):
    # Form field to choose the site to display data from
    site = SelectField('Choose the site from the drop down list', validators=[
        DataRequired()
        ], choices=[('High School', 'High School'),
                    ('Middle School', 'Middle School'),
                    ('North Elementary', 'North Elementary'),
                    ('South Elementary', 'South Elementary'),
                    ('Early Childhood', 'Early Childhood')
        ])
    submit = SubmitField('Set Site')