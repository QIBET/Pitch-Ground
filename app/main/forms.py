
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators= [Required()])
    description = TextAreaField('Pitch Comment', validators = [Required()])
    category = RadioField('Label', choices = [('Technology','Technology'), ('FashionPitch','FashionPitch'),('MotivationalPitch','Motivational'), ('Entrepreneuralpitch','Entrepreneuralpitch')],validators=[Required()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    description = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField()

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class DownvoteForm(FlaskForm):
    submit = SubmitField()
