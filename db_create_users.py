from app import db
from models import User

# insert data
db.session.add(User("testA", "testA@mail.com", "passTestA"))
db.session.add(User("testB", "testBA@mail.com", "tBpass"))

# commit the changes
db.session.commit()