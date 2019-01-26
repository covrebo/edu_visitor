from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Create the database instance
db = SQLAlchemy(app)

# Create an instance of the bcrypt encoder
bcrypt = Bcrypt(app)

from edu_visitor import routes