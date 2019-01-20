from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('home.html')

# Route to a page that tells about the creation of the system
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Route to the signin page for students
@app.route('/signin-student.html')
def student_signin():
    return render_template('student-signin.html', title='Student Sign-in')

# TODO: Create route for student signouts
# TODO: Create route for visitor signins
# TODO: Create route for visitor signouts

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

# TODO: Add visitor sign-ins/sign-outs in addition to the students
# TODO: Add the capability to search for a day's summary
# TODO: Add the ability to search for an individual's acitivity
# TODO: Add multiple buildings to the site and track which building view is active
# TODO: Add the option of choosing from a list of signed in visitors to a visitor that is signing out
