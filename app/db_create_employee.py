from app import db
from models import Employee

#create the database and the db tables
#db.create_all()

# insert
db.session.add(Employee(13000, "Lala Nguyen", "lalang@gmail.com", "lalangrocketgirl"))
db.session.add(Employee(13001, "Bailey", "bailey@gmail.com", "baileyvstheworld"))
db.session.add(Employee(13002, "Kell Rose", "kellyrose@gmail.com", "todayyousaytomorrow"))
db.session.add(Employee(13003, "Vincent Kompany", "vincdiezel@gmail.com", "nevergiveup"))



# comit the changes
db.session.commit()