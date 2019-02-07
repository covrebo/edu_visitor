from flask import Blueprint, render_template, url_for, session, flash, redirect, request
from edu_visitor import db
from edu_visitor.visitor_logs.forms import  StudentSignInForm, StudentSignOutForm, VisitorSignInForm, VisitorSignOutForm, StudentUpdateForm, VisitorUpdateForm
from edu_visitor.models import StudentLog, VisitorLog
from flask_login import login_required

visitor_logs = Blueprint('visitor_logs', __name__)


# Route to the sign-in page for students
@visitor_logs.route('/student-signin', methods=['GET', 'POST'])
def student_signin():
    form = StudentSignInForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = StudentLog(student_name=form.student_name.data, grade=form.grade.data, parent_name=form.parent.data, reason=form.reason.data, reason_other=form.reason_other.data, building=session['site'], direction='In')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed in to { session['site'] }!",
              category='success')
        return redirect(url_for('main.home'))
    return render_template('student-signin.html', title='Student Sign-in', form=form)


# Route to the sign-out page for students
@visitor_logs.route('/student-signout', methods=['GET', 'POST'])
def student_signout():
    form = StudentSignOutForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = StudentLog(student_name=form.student_name.data, grade=form.grade.data, parent_name=form.parent.data, reason=form.reason.data, reason_other=form.reason_other.data, building=session['site'], direction='Out')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed out of { session['site'] }!",
              category='success')
        return redirect(url_for('main.home'))
    return render_template('student-signout.html', title='Student Sign-out', form=form)


# Route to the sign-in page for visitors
@visitor_logs.route('/visitor-signin', methods=['GET', 'POST'])
def visitor_signin():
    form = VisitorSignInForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = VisitorLog(visitor_name=form.visitor_name.data, student_name=form.student_name.data, grade=form.grade.data, reason=form.reason.data, reason_other=form.reason_other.data, building=session['site'], direction='In')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed in to { session['site'] }!",
              category='success')
        return redirect(url_for('main.home'))
    return render_template('visitor-signin.html', title='Visitor Sign-in', form=form)


# Route to the sign-out page for visitors
@visitor_logs.route('/visitor-signout', methods=['GET', 'POST'])
def visitor_signout():
    form = VisitorSignOutForm()
    if form.validate_on_submit():
        # Create an entry to add to the database
        post = VisitorLog(visitor_name=form.visitor_name.data, building=session['site'], direction='Out')
        db.session.add(post)
        db.session.commit()
        flash(f"You have successfully signed out of { session['site'] }!",
              category='success')
        return redirect(url_for('main.home'))
    return render_template('visitor-signout.html', title='Visitor Sign-out', form=form)


# Route to display a summary of the day's student sign-ins and sign-outs
@visitor_logs.route('/daily-summary')
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
@visitor_logs.route('/student-signin/<int:post_id>')
@login_required
def view_student_signin(post_id):
    post = StudentLog.query.get_or_404(post_id)
    return render_template('student-view.html', title="Update Entry", post=post)


# A route to update a specific post for students
@visitor_logs.route('/student-signin/<int:post_id>/update', methods=['GET', 'POST'])
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
        return redirect(url_for('visitor_logs.daily_summary'))
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
@visitor_logs.route('/student-signin/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_student_signin(post_id):
    post = StudentLog.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('The entry has been deleted.', category='success')
    return redirect(url_for('visitor_logs.daily_summary'))


# A route to view a specific post for visitors
@visitor_logs.route('/visitor-signin/<int:post_id>')
@login_required
def view_visitor_signin(post_id):
    post = VisitorLog.query.get_or_404(post_id)
    return render_template('visitor_logs.visitor-view.html', title="Update Entry", post=post)


# A route to update a specific post for visitors
@visitor_logs.route('/visitor-signin/<int:post_id>/update', methods=['GET', 'POST'])
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
        return redirect(url_for('visitor_logs.daily_summary'))
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
@visitor_logs.route('/visitor-signin/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_visitor_signin(post_id):
    post = VisitorLog.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('The entry has been deleted.', category='success')
    return redirect(url_for('visitor_logs.daily_summary'))