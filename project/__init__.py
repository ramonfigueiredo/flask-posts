#################
#### imports ####
#################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

#################
#### config ####
#################

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

'''
http://flask.pocoo.org/docs/0.12/blueprints/

Flask uses a concept of blueprints for making application components and supporting common patterns within an application or across applications. 

Blueprints can greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications.

By registering the blueprint against the flask app the future operations or functionality associated with that blueprint will be executed when
the flask app is initialized.
'''
from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)