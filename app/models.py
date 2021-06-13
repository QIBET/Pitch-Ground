from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):
    '''
    This class will contain database schema for users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    password_hash = db.Column(db.String)
    @property
    def password(self):
        '''
        Raises error when someone trys to read the password
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        '''
        Generates password hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        '''
        confirms password equal to the password hash during login
        '''
        check_password_hash(self.password_hash,password)

class Pitch(db.Model):
    '''
    This class will contain the database schema for picthes table
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category = db.Column(db.String)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches
class Comment(db.Model):
    '''
    This class will contain the schema for comments
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))