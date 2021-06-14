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

