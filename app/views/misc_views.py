
from flask import Blueprint, redirect, render_template, current_app
from flask import request, url_for, flash, send_from_directory, jsonify, render_template_string
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin

from werkzeug.urls import url_parse

from app.models.user_models import User
from app.models.class_models import Class

from app import db
from app.models.user_models import User
from app.views.forms import LoginForm, RegistrationForm
import uuid, json, os
import datetime

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
main_blueprint = Blueprint('main', __name__, template_folder='templates')

# The User page is accessible to authenticated users (users that have logged in)
@main_blueprint.route('/')
@main_blueprint.route('/home')
@main_blueprint.route('/index')
def member_page():
    sql=("SELECT tc.id as id, CONCAT(c.dept,' ',c.number) as class_info, c.class_name as name, u.full_name as tutor_name, u.location as location FROM classes c INNER JOIN tutor_classes tc ON c.id = tc.class_id INNER JOIN users u ON tc.user_id = u.id")
    result = db.session.execute(sql)
    current_tutors = result.fetchall()
    if not current_user.is_authenticated:
        return render_template('index.html', current_tutors=current_tutors)

    return render_template('index.html', current_tutors=current_tutors)

@main_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/adminPage')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(smu_id=form.smu_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(u'Invalid password provided', 'danger')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/adminPage')
    return render_template('login.html', title='Sign In', form=form)

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('index')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(smu_id=form.smu_id.data, email=form.email.data, full_name=form.full_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'Congratulations, you are now a registered user!', 'success')
        return redirect('login')
    return render_template('register.html', title='Register', form=form)


@main_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

# The Admin page is accessible to users with the 'admin' role
# @main_blueprint.route('/admin')
# @roles_accepted('admin')  # Limits access to users with the 'admin' role
# def admin_page():
#     return render_template('pages/admin_page.html')

# @main_blueprint.route('/users')
# @roles_accepted('admin')
# def user_admin_page():
#     users = User.query.all()
#     return render_template('pages/admin/users.html',
#         users=users)

# @main_blueprint.route('/create_user', methods=['GET', 'POST'])
# @roles_accepted('admin')
# def create_user_page():
#     form = UserProfileForm(request.form, obj=current_user)

#     if request.method == 'POST':
#         user = User.query.filter(User.email == request.form['email']).first()
#         if not user:
#             user = User(email=request.form['email'],
#                         first_name=request.form['first_name'],
#                         last_name=request.form['last_name'],
#                         password=current_app.user_manager.hash_password(request.form['password']),
#                         active=True,
#                         email_confirmed_at=datetime.datetime.utcnow())
#             db.session.add(user)
#             db.session.commit()
#         return redirect(url_for('main.user_admin_page'))
#     return render_template('pages/admin/create_user.html',
#                            form=form)

# @main_blueprint.route('/delete_user', methods=['GET'])
# @roles_accepted('admin')
# def delete_user_page():
#     try:
#         user_id = request.args.get('user_id')

#         db.session.query(UsersRoles).filter_by(user_id = user_id).delete()
#         db.session.query(User).filter_by(id = user_id).delete()
#         db.session.commit()

#         flash('You successfully deleted your user!', 'success')
#         return redirect(url_for('main.user_admin_page'))
#     except Exception as e:
#         flash('Opps!  Something unexpected happened.  On the brightside, we logged the error and will absolutely look at it and work to correct it, ASAP.', 'error')
#         return redirect(request.referrer)

# @main_blueprint.route('/pages/profile', methods=['GET', 'POST'])
# @login_required
# def user_profile_page():
#     # Initialize form
#     form = UserProfileForm(request.form, obj=current_user)

#     # Process valid POST
#     if request.method == 'POST' and form.validate():
#         # Copy form fields to user_profile fields
#         form.populate_obj(current_user)

#         # Save user_profile
#         db.session.commit()

#         # Redirect to home page
#         return redirect(url_for('main.user_profile_page'))

#     # Process GET or invalid POST
#     return render_template('pages/user_profile_page.html',
#                            current_user=current_user,
#                            form=form)
