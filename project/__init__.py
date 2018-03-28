#################
#### imports ####
#################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from coverage import Coverage

'''
flask-sqlalchemy: http://flask-sqlalchemy.pocoo.org/2.3/
flask-bcrypt: https://flask-bcrypt.readthedocs.io/en/latest/
blueprints: http://flask.pocoo.org/docs/0.12/blueprints/
flask-login: https://flask-login.readthedocs.io/en/latest/
'''

#################
#### config ####
#################

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

'''
http://coverage.readthedocs.io/en/latest/faq.html
See answer of "Why do the bodies of functions (or classes) show as executed, but the def lines do not?"

coverage.py is started after the functions are defined. 
To show definition lines as executed, it is necessary start coverage.py earlier.
'''
cov = Coverage(branch=True, include='project/*', omit='*/__init__.py')
cov.start()


from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()