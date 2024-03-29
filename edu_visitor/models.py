from edu_visitor import db, login_manager
from flask import current_app
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Function to get login manager to find user id in database (from documentation)
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Create database models/classes
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    user_first_name = db.Column(db.String(30), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    building = db.Column(db.String(20), nullable=False)
    profile_image = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # Method for generating tokens for the password reset emails
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        # Return the token
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    # Method for verifying a token from the password reset email
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        # Check for an invalid (expired) token
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.user_first_name}', '{self.user_last_name}', '{self.profile_image}' " \
            f"'{self.email}', '{self.role}', '{self.building}')"

class StudentLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.String(20), nullable=False)
    reason_other = db.Column(db.String(120))
    building = db.Column(db.String(20), nullable=False)
    direction = db.Column(db.String(3), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"StudentLog('{self.id}, {self.student_name}', '{self.grade}', '{self.parent_name}', " \
            f"'{self.reason}', '{self.reason_other}', '{self.building}, '{self.direction}', " \
            f"'{self.date_time}')"

class VisitorLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(50), nullable=False)
    student_name = db.Column(db.String(50), nullable=False, default='NA')
    grade = db.Column(db.String(2), nullable=False, default='NA')
    reason = db.Column(db.String(20), nullable=False, default='NA')
    reason_other = db.Column(db.String(120))
    building = db.Column(db.String(20), nullable=False)
    direction = db.Column(db.String(3), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"VisitorLog('{self.id}, {self.visitor_name}', '{self.student_name}', '{self.grade}', " \
            f"'{self.reason}', '{self.reason_other}', '{self.building}, '{self.direction}', " \
            f"'{self.date_time}')"

class Sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Site('{self.site_name}')"

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Role('{self.role}')"
