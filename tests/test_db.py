import unittest

from app import create_app, db
from app.models import School, Student

class DbTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        School.insert_schools()
        self.client = self.app.test_client() # for HTTP requests

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_preloaded(self):
        schools = School.query.all()
        self.assertEqual(len(schools), 11)

    def test_add_schools(self):
        new_school = School(name='new school')
        db.session.add(new_school)
        db.session.commit()
        school_id = new_school.id
        
        school = School.query.filter_by(name='new school').first()
        self.assertEqual(school.id, school_id)

    
    def test_session(self):
        session = db.session
        print(session)
        n = session.query(School).first()
        print(n)
        session.close()
        print(session.query(School).first())