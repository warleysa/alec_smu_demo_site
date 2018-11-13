import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'
CSRF_SESSION_KEY = 'Secret Here'

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://swarley:seproject2018@se-mysql.cadmmxgevqis.us-east-2.rds.amazonaws.com/alec_tutors?charset=utf8mb4&use_unicode=1'
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

