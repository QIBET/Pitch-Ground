from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User, PitchComments, Upvote, Downvote
from .forms import PitchForm, CommentForm, UpvoteForm
from flask.views import View, MethodView
from .. import db
import markdown2

@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = 'Home'
    Technology = Pitch.query.filter_by(category="Technology")
    FashionPitch = Pitch.query.filter_by(category = "FashionPitch")
    MotivationalPitch = Pitch.query.filter_by(category = "MotivationalPitch")
    Entrepreneuralpitch = Pitch.query.filter_by(category = "Entrepreneuralpitch")

    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
    

    return render_template('home.html', title = title, pitch = pitch, Technology = Technology,FashionPitch = FashionPitch, MotivationalPitch = MotivationalPitch, Entrepreneuralpitch = Entrepreneuralpitch)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        user_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(user_id = current_user._get_current_object().id,  title = title,description=description,category=category)
        
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)

