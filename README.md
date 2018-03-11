flask-posts
===========================

### Requirements
```sh
alembic==0.9.8
click==6.7
Flask==0.12.2
Flask-Migrate==2.1.1
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
gunicorn==19.7.1
itsdangerous==0.24
Jinja2==2.10
Mako==1.0.7
MarkupSafe==1.0
psycopg2==2.7.4
psycopg2-binary==2.7.4
python-dateutil==2.6.1
python-editor==1.0.3
six==1.11.0
SQLAlchemy==1.2.5
Werkzeug==0.14.1
```

### Installation
```sh
git clone https://github.com/ramon-pessoa/flask-posts.git
cd flask-posts
virtualenv venv
pip install -r requirements.txt

Install PostgreSQL database: https://help.ubuntu.com/community/PostgreSQL

Create a database called flask_posts using the user postgresql and password postgresql in localhost:5432
-> sudo -u postgres psql
-> postgres=# CREATE DATABASE flask_posts;
-> postgres=# \q

Create the following environment variables:
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/flask_posts"
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

### [flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/): [SQLAlchemy](https://www.sqlalchemy.org/) database migrations

Initialize migrations

-> Creates a folder called migrations. This folder stores the configuration files as well as the system future migration scripts

* Local environment
```sh
python manage.py db init
```

Before creating your migration, you need to update the system models. So make the programming of the new database structure upgrading models.py file.

To create the actual migration script, run the following command.
The migration script is created in the folder: migrations > versions > filename.py

* Local environment
```sh
python manage.py db migrate
```