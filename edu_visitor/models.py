from edu_visitor import db
from datetime import datetime

# Create database models/classes
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    user_first_name = db.Column(db.String(30), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    building = db.Column(db.String(20), nullable=False)
    profile_image = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.user_first_name}', '{self.user_last_name}', " \
            f"'{self.email}', '{self.role}', '{self.building}')"

class StudentLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.String(20), nullable=False)
    reason_other = db.Column(db.String(120), nullable=False)
    building = db.Column(db.String(20), nullable=False)
    direction = db.Column(db.String(3), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"StudentLog('{self.student_name}', '{self.grade}', '{self.parent_name}', " \
            f"'{self.reason}', '{self.reason_other}', '{self.building}, '{self.direction}', " \
            f"'{self.date_time}')"

class VisitorLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(50), nullable=False)
    student_name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    reason = db.Column(db.String(20), nullable=False)
    reason_other = db.Column(db.String(120), nullable=False)
    building = db.Column(db.String(20), nullable=False)
    direction = db.Column(db.String(3), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"VisitorLog('{self.visitor_name}', '{self.student_name}', '{self.grade}', " \
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
