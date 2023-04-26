from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class ConfirmSessionForm(FlaskForm):
    submit = SubmitField(label='Confirm Session!')