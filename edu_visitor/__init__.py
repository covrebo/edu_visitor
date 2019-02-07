from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from edu_visitor.config import Config


# Create the database instance
db = SQLAlchemy()

# Create an instance of the bcrypt encoder
bcrypt = Bcrypt()

# Create an instance of login manager for user authentication
login_manager = LoginManager()
# Create the route for redirects of the @login_user decorator if someone tries to login to a page without being logged in
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'warning'

# Create an instance of moment for displaying correct dates and times
moment = Moment()

# Create an instance of mail to send emails
mail = Mail()

# Function to create the app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    from edu_visitor.users.routes import users
    from edu_visitor.visitor_logs.routes import visitor_logs
    from edu_visitor.main.routes import main
    from edu_visitor.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(visitor_logs)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app