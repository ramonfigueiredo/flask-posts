#################
#### imports ####
#################

from project import db
from project.models import BlogPost
from flask import render_template, Blueprint
from sqlalchemy.exc import OperationalError
from flask_login import login_required

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
	posts=""
	try:
		posts = db.session.query(BlogPost).all()
	except OperationalError:
		flash("You have no database! Please, contact your system administrator to set up the database!")

	return render_template("index.html", posts=posts) # render a template

@home_blueprint.route('/welcome')
def welcome():
	return render_template("welcome.html") # render a template
