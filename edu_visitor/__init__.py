from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# Create the database instance
db = SQLAlchemy(app)

# Create an instance of the bcrypt encoder
bcrypt = Bcrypt(app)

# Create an instance of login manager for user authentication
login_manager = LoginManager(app)
# Create the route for redirects of the @login_user decorator if someone tries to login to a page without being logged in
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'warning'

# Create an instance of moment for displaying correct dates and times
moment = Moment(app)

# Create an instance of mail to send emails
mail = Mail(app)

from edu_visitor.users.routes import users
from edu_visitor.visitor_logs.routes import visitor_logs
from edu_visitor.main.routes import main

app.register_blueprint(users)
app.register_blueprint(visitor_logs)
app.register_blueprint(main)