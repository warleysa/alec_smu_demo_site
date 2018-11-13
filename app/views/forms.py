from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models.user_models import User

class LoginForm(FlaskForm):
    smu_id = StringField('SMU ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    full_name  = StringField('Full Name', validators=[DataRequired()])
    smu_id = StringField('SMU ID', validators=[DataRequired(), Length(min=8, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_smu_id(self, smu_id):
        user = User.query.filter_by(smu_id=smu_id.data).first()
        if user is not None:
            raise ValidationError('Account is already created with this SMU ID.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')