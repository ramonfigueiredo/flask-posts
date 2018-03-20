from flask import Flask, render_template, redirect, \
	url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from functools import wraps
import os

# create the application object
app = Flask(__name__)

## LOCAL: Example to set environment variable in linux (ubuntu)
# > export APP_SETTINGS="config.DevelopmentConfig"
## HEROKU: Example to set environment variable in linux (ubuntu)
# >  
# config
app.config.from_object(os.environ['APP_SETTINGS'])

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *
from project.users.view import users_blueprint

# register the blueprints
# > By registering the blueprint against the flask app 
# > the future operations or functionality associated 
# > with that blueprint will be executed when the
# > flask app is initialized
app.register_blueprint(users_blueprint)

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
@app.route('/')
@login_required
def home():
	posts=""
	try:
		# return "Hello, World!" # return a string
		posts = db.session.query(BlogPost).all()
	except OperationalError:
		flash("You have no database! Please, contact your system administrator to set up the database!")

	return render_template("index.html", posts=posts) # render a template

@app.route('/welcome')
def welcome():
	return render_template("welcome.html") # render a template

####################
#### run server ####
####################

if __name__ == '__main__':
	app.run()