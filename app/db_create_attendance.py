from app import db
from models import Attendance


#create the database and the db tables

# insert
db.session.add(Attendance(13001))
#db.session.add(BlogPost("Lala Ng", "lalang@gmail.com"))


# comit the changes
db.session.commit()