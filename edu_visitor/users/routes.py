from flask import Blueprint, render_template, url_for, session, flash, redirect, request
from edu_visitor import db, bcrypt
from edu_visitor.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from edu_visitor.users.utils import save_picture, send_reset_email
from edu_visitor.models import Users
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)


# Route to a registration page
@users.route('/register', methods=['GET', 'POST'])
# Require users to login to access the registration page after an admin user has been created
# @login_required
def register():
    # Create the registration form to pass to the registration page
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the password from the registration form
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, user_first_name=form.user_first_name.data, user_last_name=form.user_last_name.data, email=form.email.data, role=form.role.data, building=form.building.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'You have successfully created an account for {form.user_first_name.data} {form.user_last_name.data}!', category='success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


# Route to a login page
@users.route('/login', methods=['GET', 'POST'])
def login():
    # Redirect the user to the home page if they are logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # Create the login form to pass to the login template
    form = LoginForm()
    # Validate the submitted form against the database and log in the user using Login Manager
    if form.validate_on_submit():
        # Query the database to see if the submitted email exists
        user = Users.query.filter_by(email=form.email.data).first()
        # If the email exists and the hashed pw matched the one in the database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            session['site'] = user.building
            session['role'] = user.role
            # Check if there is a next parameter in the URL b/c the user was redirected to the login page by trying to access a login only page and send them to the page they were trying to get to after they login instead of sending them to the homepage
            next_page = request.args.get('next')
            flash('You have successfully logged in!', category='success')
            return redirect(next_page) if next_page else redirect(url_for('visitor_logs.daily_summary'))
        else:
            flash(f'Login unsuccessful, please check your credentials', category='alert')
    return render_template('login.html', title='Login', form=form)


# Route to a logout page
@users.route('/logout')
@login_required
def logout():
    # Log the user out
    logout_user()
    # Clear the session cookies
    session.pop('site', None)
    session.pop('role', None)
    return redirect(url_for('main.home'))


# Route to display and update user account information
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    # TODO: Display the filename selected to update the profile pic https://codepen.io/hidde/pen/LyLmrG
    # TODO: Write code to delete old profile pics when a user updates their account
    form = UpdateAccountForm()
    # Update the database and session cookie with account update data
    if form.validate_on_submit():
        # Check for an updated profile picture submission
        if form.picture.data:
            # Call the function to rename the picture and save it to the filesystem
            picture_file = save_picture(form.picture.data)
            # Update the database entry for the user
            current_user.profile_image = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.building = form.building.data
        session['site'] = current_user.building
        db.session.commit()
        flash('Your account has been updated', category='success')
        return redirect(url_for('users.account'))
    # Pre-populate the form with the current user's info
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.building.data = current_user.building
    # Pass the correct image file to the template to display in the user account page
    image_file = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

# A route for users to enter their email address to get a password reset link
@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', category='secondary')
        return redirect(url_for('users.login'))
    return render_template('users.reset-request.html', title='Reset Password', form=form)


# A route for users to reset their passwords
@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = Users.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token.', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Hash the password from the registration form
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash(f'You have successfully updated your password!', category='success')
        return redirect(url_for('users.login'))
    return render_template('reset-token.html', title='Reset Password', form=form)