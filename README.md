flask-posts
===========================

### Requirements
* python 2.7
* virtualenv
* Flask
* sqlite3
* Flask-SQLAlchemy
* A github account

### Installation
```sh
git clone https://github.com/ramon-pessoa/flask-posts.git
cd flask-posts
virtualenv venv
pip install -r requirements.txt

* Create the database in the Local environment
```sh
python db_create.py
```

* Create the database in the Heroku environment
```sh
heroku run python db_create.py
```

```sh
python app.py
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