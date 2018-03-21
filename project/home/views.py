#################
#### imports ####
#################

from project import app, db
from project.models import BlogPost
from flask import flash, redirect, session, url_for, render_template, Blueprint
from sqlalchemy.exc import OperationalError
from functools import wraps

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

##########################
#### helper functions ####
##########################

# login required decorator
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('users.login'))
	return wrap

################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
	posts=""
	try:
		# return "Hello, World!" # return a string
		posts = db.session.query(BlogPost).all()
	except OperationalError:
		flash("You have no database! Please, contact your system administrator to set up the database!")

	return render_template("index.html", posts=posts) # render a template

@home_blueprint.route('/welcome')
def welcome():
	return render_template("welcome.html") # render a template