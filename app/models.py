from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager 
from datetime import datetime 



class Pitch(db.Model):
    '''
    properties of pitch class
    '''
    __tablename__='pitches' 

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    content=db.Column(db.String(255))
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    votes_id=db.Column(db.Integer,db.ForeignKey("votes.id"))
    posted_by=db.Column(db.Integer,db.ForeignKey("users.id"))
    users=db.relationship('User',backref="user",lazy = "dynamic")
    pitches = db.relationship('PitchComments',lazy = "dynamic")




class PitchComments(db.Model):
    '''
    model that defines the properties of comments
    '''
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))
    title=db.Column(db.String(255))
    content=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    date_posted=db.Column(db.DateTime,dafault=datetime.utcnow)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = PitchComments.query.filter_by(pitch_id = id).all()
        return pitches

class Votes(db.Model):
    '''
    model that defines properties of votes
    '''
    __tablename__="votes"

    id=db.Column(db.Integer,primary_key=True)
    vote_count=db.Column(db.Integer)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches=db.relationship('Pitch',backref='pitches',lazy="dynamic")  



class User(db.Model):
    '''
    models that dfeines properties of user class
    '''
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    user_bio=db.Column(db.String(255))
    photos=db.relationship('PhotoProfile',backref ='user',lazy= "dynamic")
    pitches=db.relationship('Pitch', backref ='pitches',lazy= "dynamic")
    pitchcomments=db.relationship('PitchComments',backref ='pitchcomments',lazy= "dynamic")
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))
    votes=db.relationship('Votes',backref ='votes',lazy= "dynamic")
    email=db.Column(db.String(),unique = True,index = True)
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
    password_hash=db.Column(db.String(255)) 
    


class Roles(db.Model):
    '''
    defines the role of each user in the user model 
    '''
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    users = db.relationship('Users',backref='users',lazy= "dynamic")

class PhotoProfile(db.Model):
    '''
    model that defines profile photos for user account
    '''
    __tablename__ ="photos"

    id=db.Column(db.Integer,primary_key=True)
    pic_path=db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))