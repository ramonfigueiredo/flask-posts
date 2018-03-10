flask-posts
===========================

### Requirements
* python 2.7
* virtualenv
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* A github account
* sqlite3
* PostgreSQL
* A heroku account
* gunicorn
* Jinja2
* psycopg2
* psycopg2-binary
* Werkzeug
* flask-migrate

### Installation
```sh
git clone https://github.com/ramon-pessoa/flask-posts.git
cd flask-posts
virtualenv venv
pip install -r requirements.txt
```

* Create the database in the Local environment
```sh
python db_create.py
```

* Create the database in the Heroku environment
```sh
heroku run python db_create.py
```

* Run the application in the Local environment
```sh
python app.py
```

* Run the application in the Heroku environment
```sh
1) Use the website url

2) 
heroku open 
This command will open the website url

3) 
heroku run python app.py
This command show prints in the terminal. Useful when the Flask variable DEBUG = True
```

### Run python commands in Heroku

* Add data in the Heroku PostgreSQL database right from the terminal
```sh
heroku run python

>>> from app import db
>>> from models import BlogPost
>>> db.session.add(BlogPost("Test", "This is a post test on heroku"))
>>> db.session.commit()
```

### Unit Tests

* Local environment
```sh
python test.py -v
```

* Heroku environment
```sh
heroku run python test.py -v
```

### PostgreSQL: Detailed Installation guides

* Common operating systems: https://wiki.postgresql.org/wiki/Detailed_installation_guides#General_Linux

* Debian/Ubuntu Linux: https://help.ubuntu.com/community/PostgreSQL