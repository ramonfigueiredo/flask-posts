import os
import unittest
from coverage import Coverage

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from project import app, db

'''
flask-migrate : https://flask-migrate.readthedocs.io/en/latest/
SQLAlchemy: https://www.sqlalchemy.org/
Alembic: http://alembic.zzzcomputing.com/en/latest/
unittest : https://docs.python.org/2/library/unittest.html
coverage.py : https://coverage.readthedocs.io/en/coverage-4.5.1/index.html
'''

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
	"""Runs the unit tests without coverage."""	
	tests = unittest.TestLoader().discover('tests/', pattern='*.py')
	unittest.runner.TextTestRunner(verbosity=2).run(tests)


@manager.command
def coverage():
	"""Runs the unit tests with coverage."""
	cov = Coverage(
		branch=True, include='project/*', omit='*/__init__.py')
	cov.start()
	tests = unittest.TestLoader().discover('tests/', pattern='*.py')
	unittest.runner.TextTestRunner(verbosity=2).run(tests)
	cov.stop()
	cov.save()
	print 'Coverage Summary:'
	cov.report(show_missing=True)
	basedir = os.path.abspath(os.path.dirname(__file__))
	covdir = os.path.join(basedir, 'coverage_html')
	cov.html_report(directory=covdir)
	cov.erase()

if __name__ == '__main__':
    manager.run()