from project import db # pragma: no cover
from project import bcrypt # pragma: no cover

from sqlalchemy import ForeignKey # pragma: no cover
from sqlalchemy.orm import relationship # pragma: no cover


class BlogPost(db.Model):

    __tablename__ = "posts" # pragma: no cover

    id = db.Column(db.Integer, primary_key=True) # pragma: no cover
    title = db.Column(db.String, nullable=False) # pragma: no cover
    description = db.Column(db.String, nullable=False) # pragma: no cover
    author_id = db.Column(db.Integer, ForeignKey('users.id')) # pragma: no cover

    def __init__(self, title, description, author_id):
        self.title = title
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return '<title - {}>'.format(self.title)


class User(db.Model):

    __tablename__ = "users" # pragma: no cover

    id = db.Column(db.Integer, primary_key=True) # pragma: no cover
    name = db.Column(db.String, nullable=False) # pragma: no cover
    email = db.Column(db.String, nullable=False) # pragma: no cover
    password = db.Column(db.String, nullable=False) # pragma: no cover
    posts = relationship("BlogPost", backref="author") # pragma: no cover

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)
