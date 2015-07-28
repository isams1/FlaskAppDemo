from app import db
from app import bcrypt
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy import ForeignKey, Column, DateTime, text
from sqlalchemy.orm import relationship, backref

class Employee(db.Model):

    __tablename__ = "employee"
    

    e_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    attendances = relationship('Attendance', backref='author', lazy='dynamic')

    def __init__(self, e_id, name, email, password):
           self.e_id = e_id
           self.name = name
           self.email = email
           self.password = bcrypt.generate_password_hash(password)
     
    def __repr__(self):
        return '{}-{}-{}'.format(self.e_id, self.name, self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.e_id)


class Attendance(db.Model):
    __tablename__ = "attendance"

    e_id = db.Column(db.Integer, db.ForeignKey('employee.e_id'), primary_key=True)
    #name = db.Column(db.String, nullable=False)
    check_in_date = db.Column(db.DateTime, server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME'))"))


    def __init__(self, e_id):
         self.e_id = e_id
         #self.name = name
         #self.check_in_date = check_in_date

    def __repr__(self):
        return '{} , {}'.format(self.e_id, self.check_in_date)

    
        