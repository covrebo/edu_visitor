from flask import Blueprint, render_template, url_for, session, flash, redirect
from edu_visitor.main.forms import SiteSelectionForm
from flask_login import current_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # TODO: Finish the links and pages for the footer
    # TODO: Fix the "URL_FOR" links for the JS on the bottom of layouts.html
    # TODO: Fix the frame in the home page to act correctly when the window is sized down
    return render_template('home.html')


# Route to a page that tells about the creation of the system
@main.route('/about')
def about():
    # TODO: Create content for the about page
    return render_template('about.html', title='About')

# Route to a page that tells about the creation of the system
@main.route('/privacy')
def privacy():
    return render_template('privacy-policy.html', title='Privacy Policy')


# Route with information about how to use the application
@main.route('/help')
@login_required
def help():
    # TODO: Add content to help explain how to use the site
    return render_template('help.html', title='help')


# TODO: Route and template for a contact form


# Route to a set the session cookie to display the correct site for the user
@main.route('/site-selection', methods=['GET', 'POST'])
def site_selection():
    # TODO: Add a school logo/picture to the top of the page when the site is selected.
    # Create a form to set the site value for the session
    form = SiteSelectionForm()
    if form.validate_on_submit():
        # Update site value in session cookie
        session['site'] = form.site.data
        flash('Your location has been updated!', 'success')
        return redirect(url_for('visitor_logs.daily_summary')) if current_user.is_authenticated else redirect(url_for('main.home'))
    return render_template('site-selection.html', title='Site Selection', form=form)

# TODO: Refactor account.html
# TODO: Refactor help.html
# TODO: Refactor privacy-policy.html
# TODO: Refactor reset-request.html
# TODO: Refactor reset-token.html
# TODO: Refactor student-signin.html
# TODO: Refactor student-signout.html
# TODO: Refactor student-update.html
# TODO: Refactor student-view.html
# TODO: Refactor visitor-signin.html
# TODO: Refactor visitor-signout.html
# TODO: Refactor visitor-update.html
# TODO: Refactor visitor-view.html