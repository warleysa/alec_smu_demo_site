
from flask import Blueprint, redirect, render_template, current_app
from flask import request, url_for, flash, send_from_directory, jsonify, render_template_string
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin

from werkzeug.urls import url_parse

from sqlalchemy import select
from app.models.user_models import User
from app.models.class_models import Class

from app import db
from app.models.user_models import User
from app.views.forms import LoginForm
import uuid, json, os
import datetime

import pusher

pusher_client = pusher.Pusher(
    app_id='639453',
    key='989251a250c4490baf73',
    secret='726b8083be6dae5d3111',
    cluster='us2',
    ssl=True)

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')

@admin_blueprint.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect('login')

@admin_blueprint.route('/profile', methods=['GET'])
def profilePage():
	currID = current_user.get_id()
	user = User.query.filter_by(id=currID).first()
	sqlClass=("SELECT tc.id as id, CONCAT(c.dept,' ',c.number) as class_info, c.class_name as class_name, u.full_name as tutor_name, u.location as location"
			+ " FROM classes c INNER JOIN tutor_classes tc ON c.id = tc.class_id INNER JOIN users u ON tc.user_id = u.id"
			+ " WHERE u.id = " + str(currID))
	resultC = db.session.execute(sqlClass)
	tutor_class_info = resultC.fetchall()

	return render_template('tutor-profile.html', user=user, tutor_class_info=tutor_class_info)

@admin_blueprint.route('/profile/<int:id>', methods=['GET'])
def profileEdit(id):
	currID = current_user.get_id()
	adminStatus = User.query.with_entities(User.admin_status).filter_by(id=currID).first().admin_status
	userInfo = User.query.with_entities(User.id, User.full_name, User.email, User.location, User.admin_status, User.smu_id).filter_by(id=id).first()
	# Checks if user is admin OR is editing their own profile page
	if currID == str(id) or adminStatus == True: 
		return render_template('tutor-profile-edit.html', userInfo=userInfo, adminStatus=adminStatus)
	else:
		flash(u'Invalid permissions to edit this profile', 'danger')
		return redirect('login')

@admin_blueprint.route('/profile/<int:id>/add-class', methods=['GET'])
def tutorAddClassPage(id):
	currID = current_user.get_id()
	adminStatus = User.query.with_entities(User.admin_status).filter_by(id=currID).first().admin_status
	# Checks if user is admin OR is editing their own profile page
	if currID == str(id) or adminStatus == True: 
		sql=("SELECT id, dept, number, CONCAT(dept,' ',number) as class_info, class_name FROM classes;")
		result = db.session.execute(sql)
		all_classes = result.fetchall()
		return render_template('tutor-profile-add-class.html', all_classes=all_classes, user_id=currID)
	else:
		flash(u'Invalid permissions to edit this profile', 'danger')
		return redirect('login')


@admin_blueprint.route('/profile/<int:id>/add-class', methods=['POST'])
def tutorAddClass(id):
	currID = current_user.get_id()
	adminStatus = User.query.with_entities(User.admin_status).filter_by(id=currID).first().admin_status
	# Checks if user is admin OR is editing their own profile page
	if currID == str(id) or adminStatus == True: 
		class_id = request.form['class_id']
		sql=("INSERT INTO tutor_classes (user_id, class_id) VALUES ("+currID+","+str(class_id)+")")
		db.session.execute(sql)
		db.session.commit()
		return 'ok'
	else:
		flash(u'Invalid permissions to add classes to this profile', 'danger')
		return None

@admin_blueprint.route('/stats/<int:id>', methods=['GET'])
def statsPage(id):
	currID = current_user.get_id()
	adminStatus = User.query.with_entities(User.admin_status).filter_by(id=currID).first().admin_status
	if currID == str(id) or adminStatus == True: 
		sqlClass=("SELECT tc.id as id, CONCAT(c.dept,' ',c.number) as class_info, c.class_name as class_name, u.full_name as tutor_name, u.location as location"
			+ " FROM classes c INNER JOIN tutor_classes tc ON c.id = tc.class_id INNER JOIN users u ON tc.user_id = u.id"
			+ " WHERE u.id = " + str(id))
		resultC = db.session.execute(sqlClass)
		tutor_class_info = resultC.fetchall()

		sqlAlecSessions=("SELECT id, start_time, end_time, TIMESTAMPDIFF(MINUTE, start_time, end_time) as total_time FROM alec_session WHERE user_id = "+ str(id))
		resultAS = db.session.execute(sqlAlecSessions)
		alec_sessions = resultAS.fetchall()

		sqlTutoringSessions=("SELECT ts.id as id, CONCAT(c.dept,' ',c.number) as class_name, "
			+ "ts.start_time as start_time, ts.end_time as end_time, TIMESTAMPDIFF(MINUTE,ts.start_time, ts.end_time) as total_time "
			+ "FROM tutor_session ts INNER JOIN tutor_classes tc ON ts.tutor_classes_id = tc.id "
			+ "INNER JOIN classes c ON tc.class_id = c.id WHERE user_id = "+ str(id))
		resultTS = db.session.execute(sqlTutoringSessions)
		tutoring_sessions = resultTS.fetchall()

		return render_template('stats.html', tutor_class_info=tutor_class_info, alec_sessions=alec_sessions, tutoring_sessions=tutoring_sessions)
	else:
		flash(u'Invalid permissions to view stats about this tutor', 'danger')
		return redirect('login')

@admin_blueprint.route('/adminPage', methods=['GET'])
def adminPage():
	currID = current_user.get_id()
	adminStatus = User.query.with_entities(User.admin_status).filter_by(id=currID).first().admin_status
	if currID == str(id) or adminStatus == True: 
		classes = Class.query.all()
		tutors = User.query.with_entities(User.id, User.full_name, User.email, User.location, User.admin_status, User.smu_id).filter_by(admin_status=0)
		admins = User.query.with_entities(User.id, User.full_name, User.email, User.location, User.admin_status, User.smu_id).filter_by(admin_status=1)
		return render_template('admin-page.html', classes=classes, tutors=tutors, admins=admins)
	else:
		flash(u'Invalid permissions to view this page', 'danger')
		return redirect('login')


@admin_blueprint.route('/remove-class/<int:record_id>/user/<int:id>', methods=['DELETE'])
def remove_class(record_id, id):
	currID = current_user.get_id()
	adminStatus = User.query.with_entities(User.admin_status).filter_by(id=currID).first().admin_status
	if currID == str(id) or adminStatus == True: 
		sql=("DELETE FROM tutor_classes WHERE id = "+str(record_id)+";")
		db.session.execute(sql)
		db.session.commit()
		pusher_client.trigger('table', 'remove-class', {'id': record_id })
	return 'OK'


@admin_blueprint.route('/edit-class/<int:id>', methods=['GET'])
def update_class(id):
    new_class = Class.query.get(id)
    return render_template('update_class.html', data=new_class)