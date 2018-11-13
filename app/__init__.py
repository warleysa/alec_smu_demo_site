# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from datetime import datetime
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

# Instantiate Flask extensions
db = SQLAlchemy()
csrf_protect = CSRFProtect()
login_manager = LoginManager()


def create_app(extra_config_settings={}):
    """Create a Flask applicaction.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    # Load common settings from 'app/settings.py' file
    app.config.from_object('app.settings')
    # Load local settings from 'app/local_settings.py'
    app.config.from_object('app.local_settings')
    # Load extra config settings from 'extra_config_settings' param
    app.config.update(extra_config_settings)

    login_manager.init_app(app)
    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup WTForms CSRFProtect
    csrf_protect.init_app(app)

    # Register blueprints
    from app.views.misc_views import main_blueprint
    from app.views.admin_views import admin_blueprint
    from app.views.misc_views import main_blueprint
    # from app.views.tutor_views import tutor_blueprint
    from app.views.apis import api_blueprint
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(main_blueprint)
    # app.register_blueprint(tutor_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    csrf_protect.exempt(api_blueprint)

    # Define bootstrap_is_hidden_field for flask-bootstrap's bootstrap_wtf.html
    from wtforms.fields import HiddenField

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)

    app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter

    return app




