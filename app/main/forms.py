from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators= [Required()])
    comment = TextAreaField('Pitch Comment', validators = [Required()])
    submit = SubmitField('Post')



