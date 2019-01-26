from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Create the database instance
db = SQLAlchemy(app)

# Create an instance of the bcrypt encoder
bcrypt = Bcrypt(app)

# Create an instance of login manager for user authentication
login_manager = LoginManager(app)
# Create the route for redirects of the @login_user decorator if someone tries to login to a page without being logged in
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

from edu_visitor import routes