from project import db
from project.models import BlogPost

# create the database and db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

# commit the changes
db.session.commit()