"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for additional runserver options.
"""

from app import create_app
# from flask_script import Manager

# # Setup Flask-Script with command line commands
# manager = Manager(create_app)
# manager.add_command('init_db', InitDbCommand)

app = create_app()

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
	app.run(host='0.0.0.0')