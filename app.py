from flask import Flask, render_template, url_for, session, flash, redirect
from forms import RegistrationForm, LoginForm, SiteSelectionForm, StudentSignInForm, StudentSignOutForm, VisitorSignInForm, VisitorSignOutForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '142972b1bb8f93156d1ce84ae83a9e9f'

# Example data from sign-in or sign-out forms
student_log = [
    {
        'student_name': 'Evan Ovrebo',
        'grade': '01',
        'parent': 'Chris Ovrebo',
        'reason': 'Appointment',
        'direction': 'In',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 11:24:35'
    },
    {
        'student_name': 'Allison Ovrebo',
        'grade': '01',
        'parent': 'Jodi Ovrebo',
        'reason': 'Appointment',
        'direction': 'In',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 12:24:35'
    },
    {
        'student_name': 'Calvin Ovrebo',
        'grade': '03',
        'parent': 'Chris Ovrebo',
        'reason': 'Vacation',
        'direction': 'Out',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 13:24:35'
    },
    {
        'student_name': 'Eliza Ovrebo',
        'grade': 'KG',
        'parent': 'Jodi Ovrebo',
        'reason': 'Illness',
        'direction': 'In',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 14:24:35'
    },
]
visitor_log = [
    {
        'student_name': 'Evan Ovrebo',
        'grade': '01',
        'visitor': 'Chris Ovrebo',
        'reason': 'Classroom visit',
        'direction': 'In',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 11:24:35'
    },
    {
        'student_name': 'Allison Ovrebo',
        'grade': '01',
        'visitor': 'Jodi Ovrebo',
        'reason': 'Appointment',
        'direction': 'In',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 12:24:35'
    },
    {
        'student_name': 'Calvin Ovrebo',
        'grade': '03',
        'visitor': 'Chris Ovrebo',
        'reason': 'Vacation',
        'direction': 'Out',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 13:24:35'
    },
    {
        'student_name': 'Eliza Ovrebo',
        'grade': 'KG',
        'visitor': 'Jodi Ovrebo',
        'reason': 'Illness',
        'direction': 'In',
        'building': 'North Elementary',
        'timestamp': '18-Jan-2019 14:24:35'
    },
]

# Route to the home page, which includes options to sign in or sign out
@app.route('/')
@app.route('/home')
def home():
    # TODO: Create a quick welcome page that has four buttons: Student Sign-In, Student Sign-Out, Visitor Sign-In, and Visitor Sign-Out
    # TODO: Flash a message that the user has successfully signed in or out
    # TODO: Finish the links and pages for the footer
    # TODO: Fix the "URL_FOR" links for the JS on the bottom of layouts.html
    # TODO: Fix the frame in the home page to act correctly when the window is sized down
    return render_template('home.html')

# Route to a page that tells about the creation of the system
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Route to a registration page
@app.route('/register')
def register():
    # TODO make registration link in navigation bar only visible to admins and page only accessible to admins
    # Create the registration form to pass to the registration page
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

# Route to a login page
@app.route('/login')
def login():
    # Create the registration form to pass to the registration page
    # TODO: Create the url_for the password reset link
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# Route to a set the entrance
@app.route('/site-selection', methods=['GET', 'POST'])
def site_selection():
    # Create a form to set the site value for the session
    form = SiteSelectionForm()
    if form.validate_on_submit():
        # Update site value in session cookie
        session['site'] = form.site.data
        flash('Your location has been updated!', 'success')
        return redirect(url_for('daily_summary'))
    return render_template('site-selection.html', title='Site Selection', form=form)

# Route to the sign-in page for students
@app.route('/student-signin')
def student_signin():
    form = StudentSignInForm()
    return render_template('student-signin.html', title='Student Sign-in', form=form)

# Route to the sign-out page for students
@app.route('/student-signout')
def student_signout():
    form = StudentSignOutForm()
    return render_template('student-signout.html', title='Student Sign-out', form=form)

# Route to the sign-in page for visitors
@app.route('/visitor-signin')
def visitor_signin():
    form = VisitorSignInForm()
    return render_template('visitor-signin.html', title='Visitor Sign-in', form=form)

# Route to the sign-out page for visitors
@app.route('/visitor-signout')
def visitor_signout():
    form = VisitorSignOutForm()
    return render_template('visitor-signout.html', title='Visitor Sign-out', form=form)

# Route with information about how to use the application
@app.route('/help')
def help():
    # TODO: Add to the right hand or footer of the website
    # TODO: Make visible only when logged in
    # TODO: Add content to help explain how to use the site
    return render_template('help.html', title='help')

# Route to display a summary of the day's student sign-ins and sign-outs
@app.route('/daily-summary')
def daily_summary():
    # TODO: Make this visible only when you are logged in
    # TODO: When you click on a specific log entry, it brings you to a page where an admin can update or delete it
    # TODO: Create DB calls to create the dictionaries only for the current day
    return render_template('daily-summary.html', student_log=student_log, visitor_log=visitor_log, title='Daily Summary')

if __name__ == '__main__':
    app.run()

# TODO: Add the capability to search for a day's summary
# TODO: Add the ability to search for an individual's activity
# TODO: Add admin panel to manage users and sites
# TODO: Add the option of choosing from a list of signed in visitors to a visitor that is signing out
