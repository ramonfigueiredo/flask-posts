import os
import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from project import app, db, cov

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
	'''
	coverage.py was created and started in the file project/__init__.py

	http://coverage.readthedocs.io/en/latest/faq.html
	See answer of "Why do the bodies of functions (or classes) show as executed, but the def lines do not?"

	coverage.py is started after the functions are defined. 
	To show definition lines as executed, it is necessary start coverage.py earlier.
	'''
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