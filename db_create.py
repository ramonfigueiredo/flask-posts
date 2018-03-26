from project import db
from project.models import User, BlogPost

# create the database and db tables
db.create_all()

# insert data
db.session.add(User("admin", "admin@mail.com", "admin"))

# insert
db.session.add(BlogPost("Good", "I\'m good.", 1))
db.session.add(BlogPost("Well", "I\'m well.", 1))

# commit the changes
db.session.commit()