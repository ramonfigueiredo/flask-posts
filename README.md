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

### Deploing to Heroku

#### Prerequisites

* Installed Python and Virtualenv in a unix-style environment.
* Your application must use Pip to resolve dependencies.
* A Heroku user account.
* PostgreSQL installed locally, if running the app locally.

#### Local workstation setup

* First, install the Heroku Toolbelt on your workstation.

	* Heroku Command Line Interface (CLI) for Debian/Ubuntu:

```sh
# Run this from your terminal.

# The following will add our apt repository and install the CLI:

sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"

curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -

sudo apt-get update

sudo apt-get install heroku
```

#### Log in to Heroku (Enter your Heroku credentials: e-mail and password)

```sh
heroku login
```

#### Start Flask app inside a Virtualenv

```sh
virtualenv venv
```

#### Activate the Virtualenv

```sh
source venv/bin/activate
```

#### Install Flask gunicorn, if it is not installed

```sh
pip install Flask gunicorn
```

#### Declare process types with Procfile

Create a file in the root of the repository called ```Procfile``` with the context:

```sh
web: gunicorn app:app
```

To test if the ```Procfile``` is valid:

```sh
foreman check
```

You can now start the processes in your ```Procfile``` using Foreman (installed as part of the Toolbelt):

Locally, instead of ```python app.py``` you can use:

```sh
foreman start
```

#### Specify dependencies with Pip

Heroku recognizes Python applications by the existence of a ```requirements.txt``` file in the root of a repository. This simple format is used by most Python projects to specify the external Python modules the application requires.

Pip has a command (```pip freeze```) that will generate this file for you:

```sh
pip freeze > requirements.txt
```

#### Store your app in Git

Now that you've written and tested your application, you need to store the project in a Git repository.

Since your current directory contains a lot of extra files, you'll want to configure your repository to ignore these files with a ```.gitignore``` file:

```sh
venv
*.pyc
```

Next, we'll create a new git repository and save our changes.

```sh
git init
git add .
git commit -m "Your commit message here."

```

#### Deploy your application to Heroku

The next step is to push the application's repository to Heroku. First, you have to get a place to push to from Heroku. You can do this with the ```heroku create``` command:

```sh
heroku create
```


### Unit Tests

* Local environment
```sh
python run_unit_tests.py -v
```

* Heroku environment
```sh
heroku run python run_unit_tests.py -v
```

### PostgreSQL: Detailed Installation guides

* Common operating systems: https://wiki.postgresql.org/wiki/Detailed_installation_guides#General_Linux

* Debian/Ubuntu Linux: https://help.ubuntu.com/community/PostgreSQL

### [flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/): [SQLAlchemy](https://www.sqlalchemy.org/) database migrations

**Initialize migrations:** Creates a folder called migrations. This folder stores the configuration files as well as the system future migration scripts.

* Local environment
```sh
python manage.py db init
```

Before creating your migration, you need to update the system models. So make the programming of the new database structure upgrading models.py file.

The migration script is created in the folder: migrations > versions > filename.py . This script essentially has two main functions: upgrade and downgrade. To create the migration script, run the following command:

* Local environment
```sh
python manage.py db migrate
```

To apply the database migration, run the following command:

* Local environment
```sh
python manage.py db upgrade
```

* Heroku environment
```sh
heroku run python manage.py db upgrade
```

* Check the database migration

```sh
Opens PostgreSQL shell in the Local environment
sudo -u postgres psql
```

```sh
Opens PostgreSQL shell in the Heroku environment
heroku pg:psql
```

```sh
Connects to flask_posts database
\c flask_posts

Shows the tables in the database
\d

Shows the posts table structure (schema)
\d posts

Select all data in posts table
SELECT * FROM posts;

Insert data into posts table
INSERT INTO users VALUES(1, 'admin', 'admin@gmail.com', 'admin');

Select all data in users table
SELECT * FROM users;

Update data in posts table
UPDATE posts SET author_id = 1;

Select all data in posts table
SELECT * FROM posts;
```