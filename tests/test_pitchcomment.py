import unittest
from app.models import Pitch, User, PitchComments
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_content = "pitch one", pitch_category = "Technology")
        self.new_comment = PitchComments(comment_content = "One Comment", pitch = self.new_pitch)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, PitchComments))
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"One comment")
        self.assertEquals(self.new_comment.pitch,self.new_pitch, 'pitch one')

