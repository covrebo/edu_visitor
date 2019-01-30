import os
import secrets
from PIL import Image
from flask import render_template, url_for, session, flash, redirect, request
from datetime import date
from edu_visitor import app, db, bcrypt, moment
from edu_visitor.forms import RegistrationForm, LoginForm, SiteSelectionForm, StudentSignInForm, StudentSignOutForm, VisitorSignInForm, VisitorSignOutForm, UpdateAccountForm, StudentUpdateForm, VisitorUpdateForm
from edu_visitor.models import Users, StudentLog, VisitorLog, Sites, Roles
from flask_login import login_user, current_user, logout_user, login_required

# Example data from sign-in or sign-out forms
# student_log = [
#     {
#         'student_name': 'Evan Ovrebo',
#         'grade': '01',
#         'parent': 'Chris Ovrebo',
#         'reason': 'Appointment',
#         'direction': 'In',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 11:24:35'
#     },
#     {
#         'student_name': 'Allison Ovrebo',
#         'grade': '01',
#         'parent': 'Jodi Ovrebo',
#         'reason': 'Appointment',
#         'direction': 'In',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 12:24:35'
#     },
#     {
#         'student_name': 'Calvin Ovrebo',
#         'grade': '03',
#         'parent': 'Chris Ovrebo',
#         'reason': 'Vacation',
#         'direction': 'Out',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 13:24:35'
#     },
#     {
#         'student_name': 'Eliza Ovrebo',
#         'grade': 'KG',
#         'parent': 'Jodi Ovrebo',
#         'reason': 'Illness',
#         'direction': 'In',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 14:24:35'
#     },
# ]
# visitor_log = [
#     {
#         'student_name': 'Evan Ovrebo',
#         'grade': '01',
#         'visitor': 'Chris Ovrebo',
#         'reason': 'Classroom visit',
#         'direction': 'In',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 11:24:35'
#     },
#     {
#         'student_name': 'Allison Ovrebo',
#         'grade': '01',
#         'visitor': 'Jodi Ovrebo',
#         'reason': 'Appointment',
#         'direction': 'In',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 12:24:35'
#     },
#     {
#         'student_name': 'Calvin Ovrebo',
#         'grade': '03',
#         'visitor': 'Chris Ovrebo',
#         'reason': 'Vacation',
#         'direction': 'Out',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 13:24:35'
#     },
#     {
#         'student_name': 'Eliza Ovrebo',
#         'grade': 'KG',
#         'visitor': 'Jodi Ovrebo',
#         'reason': 'Illness',
#         'direction': 'In',
#         'building': 'North Elementary',
#         'timestamp': '18-Jan-2019 14:24:35'
#     },
# ]

# Route to the home page, which includes options to sign in or sign out

@app.route('/')
@app.route('/home')
def home():
    # TODO: Finish the links and pages for the footer
    # TODO: Fix the "URL_FOR" links for the JS on the bottom of layouts.html
    # TODO: Fix the frame in the home page to act correctly when the window is sized down
    return render_template('home.html')


# Route to a page that tells about the creation of the system
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# Route to a registration page
@app.route('/register', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Route to a login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Create the url_for the password reset link
    # Redirect the user to the home page if they are logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
            return redirect(next_page) if next_page else redirect(url_for('daily_summary'))
        else:
            flash(f'Login unsuccessful, please check your credentials', category='alert')
    return render_template('login.html', title='Login', form=form)


# Route to a logout page
@app.route('/logout')
@login_required
def logout():
    # Log the user out
    logout_user()
    # Clear the session cookies
    session.pop('site', None)
    session.pop('role', None)
    return redirect(url_for('home'))


# Route to a set the session cookie to display the correct site for the user
@app.route('/site-selection', methods=['GET', 'POST'])
def site_selection():
    # Create a form to set the site value for the session
    form = SiteSelectionForm()
    if form.validate_on_submit():
        # Update site value in session cookie
        session['site'] = form.site.data
        flash('Your location has been updated!', 'success')
        return redirect(url_for('daily_summary')) if current_user.is_authenticated else redirect(url_for('home'))
    return render_template('site-selection.html', title='Site Selection', form=form)


# Route to the sign-in page for students
@app.route('/student-signin', methods=['GET', 'POST'])
def student_signin():
    form = StudentSignInForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = StudentLog(student_name=form.student_name.data, grade=form.grade.data, parent_name=form.parent.data, reason=form.reason.data, reason_other=form.reason_other.data, building=session['site'], direction='In')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed in to { session['site'] }!",
              category='success')
        return redirect(url_for('home'))
    return render_template('student-signin.html', title='Student Sign-in', form=form)


# Route to the sign-out page for students
@app.route('/student-signout', methods=['GET', 'POST'])
def student_signout():
    form = StudentSignOutForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = StudentLog(student_name=form.student_name.data, grade=form.grade.data, parent_name=form.parent.data, reason=form.reason.data, reason_other=form.reason_other.data, building=session['site'], direction='Out')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed out of { session['site'] }!",
              category='success')
        return redirect(url_for('home'))
    return render_template('student-signout.html', title='Student Sign-out', form=form)


# Route to the sign-in page for visitors
@app.route('/visitor-signin', methods=['GET', 'POST'])
def visitor_signin():
    form = VisitorSignInForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = VisitorLog(visitor_name=form.visitor_name.data, student_name=form.student_name.data, grade=form.grade.data, reason=form.reason.data, reason_other=form.reason_other.data, building=session['site'], direction='In')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed in to { session['site'] }!",
              category='success')
        return redirect(url_for('home'))
    return render_template('visitor-signin.html', title='Visitor Sign-in', form=form)


# Route to the sign-out page for visitors
@app.route('/visitor-signout', methods=['GET', 'POST'])
def visitor_signout():
    form = VisitorSignOutForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = VisitorLog(visitor_name=form.visitor_name.data, building=session['site'], direction='Out')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed out of { session['site'] }!",
              category='success')
        return redirect(url_for('home'))
    return render_template('visitor-signout.html', title='Visitor Sign-out', form=form)


# Route with information about how to use the application
@app.route('/help')
@login_required
def help():
    # TODO: Add content to help explain how to use the site
    return render_template('help.html', title='help')


# Route to display a summary of the day's student sign-ins and sign-outs
@app.route('/daily-summary')
@login_required
def daily_summary():
    # TODO: Create DB calls to create the dictionaries only for the current day
    # Query database for student visitor logs entering the building and get the correct page to display from the URL
    student_page_in = request.args.get('student_page_in', 1, type=int)
    student_log_in = StudentLog.query.order_by(StudentLog.id.desc()).filter_by(direction='In', building=session['site']).paginate(page=student_page_in, per_page=5)
    # Query database for student visitor logs leaving the building
    student_page_out = request.args.get('student_page_out', 1, type=int)
    student_log_out = StudentLog.query.order_by(StudentLog.id.desc()).filter_by(direction='Out', building=session['site']).paginate(page=student_page_out, per_page=5)
    # Query database for visitor logs entering the building
    visitor_page_in = request.args.get('visitor_page_in', 1, type=int)
    visitor_log_in = VisitorLog.query.order_by(VisitorLog.id.desc()).filter_by(direction='In', building=session['site']).paginate(page=visitor_page_in, per_page=5)
    # Query database for visitor logs leaving the building
    visitor_page_out = request.args.get('visitor_page_out', 1, type=int)
    visitor_log_out = VisitorLog.query.order_by(VisitorLog.id.desc()).filter_by(direction='Out', building=session['site']).paginate(page=visitor_page_out, per_page=5)
    return render_template('daily-summary.html', student_log_in=student_log_in, student_log_out=student_log_out, visitor_log_in=visitor_log_in, visitor_log_out=visitor_log_out, title='Daily Summary')


# A route to view a specific post for students
@app.route('/student-signin/<int:post_id>')
@login_required
def view_student_signin(post_id):
    post = StudentLog.query.get_or_404(post_id)
    return render_template('student-view.html', title="Update Entry", post=post)


# A route to update a specific post for students
@app.route('/student-signin/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_student_signin(post_id):
    post = StudentLog.query.get_or_404(post_id)
    form = StudentUpdateForm()
    if form.validate_on_submit():
        post.student_name = form.student_name.data
        post.grade = form.grade.data
        post.parent_name = form.parent.data
        post.reason = form.reason.data
        post.reason_other = form.reason_other.data
        post.direction = form.direction.data
        db.session.commit()
        flash("Your post has been updated.", 'success')
        return redirect(url_for('daily_summary'))
    # Pre-populate the form
    elif request.method == 'GET':
        form.student_name.data = post.student_name
        form.grade.data = post.grade
        form.parent.data = post.parent_name
        form.reason.data = post.reason
        form.reason_other.data = post.reason_other
        form.direction.data = post.direction
    return render_template('student-update.html', title="Update Entry", post=post, form=form)


# A route to delete a specific post for students
@app.route('/student-signin/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_student_signin(post_id):
    post = StudentLog.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('The entry has been deleted.', category='success')
    return redirect(url_for('daily_summary'))


# A route to view a specific post for visitors
@app.route('/visitor-signin/<int:post_id>')
@login_required
def view_visitor_signin(post_id):
    post = VisitorLog.query.get_or_404(post_id)
    return render_template('visitor-view.html', title="Update Entry", post=post)


# A route to update a specific post for visitors
@app.route('/visitor-signin/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_visitor_signin(post_id):
    post = VisitorLog.query.get_or_404(post_id)
    form = VisitorUpdateForm()
    if form.validate_on_submit():
        post.visitor_name = form.visitor_name.data
        post.student_name = form.student_name.data
        post.grade = form.grade.data
        post.reason = form.reason.data
        post.reason_other = form.reason_other.data
        post.direction = form.direction.data
        db.session.commit()
        flash("Your post has been updated.", 'success')
        return redirect(url_for('daily_summary'))
    # Pre-populate the form
    elif request.method == 'GET':
        form.visitor_name.data = post.visitor_name
        form.student_name.data = post.student_name
        form.grade.data = post.grade
        form.reason.data = post.reason
        form.reason_other.data = post.reason_other
        form.direction.data = post.direction
    return render_template('visitor-update.html', title="Update Entry", post=post, form=form)


# A route to delete a specific post for visitor
@app.route('/visitor-signin/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_visitor_signin(post_id):
    post = VisitorLog.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('The entry has been deleted.', category='success')
    return redirect(url_for('daily_summary'))


# Function to save a new profile picture submission form the user - used in the update account form
def save_picture(form_picture):
    # Randomize the file name to avoid conflicts in the file system
    random_hex = secrets.token_hex(8)
    # Get the filname and file extension of the submitted file
    _, f_ext = os.path.splitext(form_picture.filename)
    # Combine the random hex string and file extension to create a new name for the submitted picture file
    picture_file_name = random_hex + f_ext
    # Create the path to the folder where the image will be stored
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_file_name)
    # Resize the picture before saving it
    output_size = (125,125)
    resized_image = Image.open(form_picture)
    resized_image.thumbnail(output_size)
    # Save the resized image to the file system
    resized_image.save(picture_path)
    # Pass the new name of the file back so it can be used to update the database entry for the user
    return picture_file_name


# Route to display a summary of the day's student sign-ins and sign-outs
@app.route('/account', methods=['GET', 'POST'])
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
        return redirect(url_for('account'))
    # Pre-populate the form with the current user's info
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.building.data = current_user.building
    # Pass the correct image file to the template to display in the user account page
    image_file = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


# Enhancements
# TODO: Add the capability to search for a day's summary
# TODO: Add the ability to search for an individual's activity
# TODO: Add admin panel to manage users and sites and reasons
# TODO: Add the option of choosing from a list of signed in visitors to a visitor that is signing out
# TODO: Throw an error on the sign in page if the reason = "Other" but there isn't any text in the other fields
# TODO: Change the "Change site" button on the top right navigation bar to a drop down menu when the user is logged in
# TODO: Add the option to receive a confirmation email when signing in or signing out
