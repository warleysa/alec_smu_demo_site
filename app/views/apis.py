# Copyright 2018 Twin Tech Labs. All rights reserved

from flask import Blueprint, redirect, render_template
from flask import request, url_for, flash, send_from_directory, jsonify, render_template_string
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin

from app import db
from app.models.user_models import User
from app.models.class_models import Class

import uuid, json, os
import datetime

import pusher

pusher_client = pusher.Pusher(
    app_id='639453',
    key='989251a250c4490baf73',
    secret='726b8083be6dae5d3111',
    cluster='us2',
    ssl=True)

api_blueprint = Blueprint('api', __name__, template_folder='templates')

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
@api_blueprint.route('/admin/add-class', methods=['POST'])
def addClass():
    if request.method == "POST":
        class_name = request.form["class_name"]
        dept = request.form["dept"]
        number = request.form["number"]
        desc = request.form["desc"]
        new_class = Class(class_name, dept, number, desc)
        db.session.add(new_class)
        db.session.commit()
        data = {
                "id": new_class.id,
                "class_name": class_name,
                "dept": dept,
                "number": number,
                "desc": desc}

        pusher_client.trigger('table', 'new-class', {'data': data })

        return 'ok'


@api_blueprint.route('/edit-class/post/<int:id>', methods=['POST'])
def update_class(id):
    class_name = request.form["class_name"]
    dept = request.form["dept"]
    number = request.form["number"]
    desc = request.form["desc"]

    update_class = Class.query.get(id)
    update_class.class_name = class_name
    update_class.dept = dept
    update_class.number = number
    update_class.desc = desc
    db.session.commit()

    return redirect("adminPage", code=302)

@api_blueprint.route('/remove/<int:id>', methods=['DELETE'])
def remove_class(id):
    Class.query.filter_by(id=id).delete()
    db.session.commit()
    pusher_client.trigger('table', 'remove-class', {'id': id })
    return 'OK'
