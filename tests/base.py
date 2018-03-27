from flask_testing import TestCase

from project import app, db
from project.models import User, BlogPost

'''
flask-testing: https://pythonhosted.org/Flask-Testing/
'''

'''
BaseTestCase:
- establishes our test configuration (config.py > TestConfig class)
- creates all of our database tables before each test and then deletes 
all the tables at the end of every test run.

That means each of the following tests are going to run against clean database.
And then each of our future test cases will also inherit from this base test case
and that will help keep our code dry.
'''

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin@mail.com", "adminpass"))
        db.session.add(BlogPost("Test post", "This is a test. Only a test.", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()