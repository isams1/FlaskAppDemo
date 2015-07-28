from flask import Flask, render_template, redirect, url_for, request, session, flash
import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, login_user, login_required, logout_user

#import sqlite3
from form import LoginForm
#from form import LoginForm
#from project.models import User, bcrypt

#create the application object
bcrypt = Bcrypt()
app = Flask(__name__)

#config
#app.config.from_object('config.BaseConfig')
#app.config.from_envvar('APP_SETTINGS')


#app.secret_key = "bailey"
#app.database = "sample.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

app.config.update(
     DEBUG=False,
     SECRET_KEY='development key',
     USERNAME='admin',
     PASSWORD='default',
     SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'
)


#def init_db():
 #   """Initializes the database."""
 #   db = get_db()
 #   with app.open_resource('employee.sql', mode='r') as f:
 #       db.cursor().executescript(f.read())
  #  db.commit()



@app.route('/')
def home():
     employees = db.session.query(Employee).all()
     #g.db = connect_db()
     #cur = g.db.execute('select * from employee')
     
     #employees =[]
     #for row in cur.fetchall():
     #  employees.append(dict(emid=row[0], ename=row[1], email=row[2]))

     #posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
     #print posts
     #g.db.close()
     # return "Hello, World!"
     return render_template('index.html', employees=employees)


@app.route('/welcomeboss')
def welcome_boss():
     return render_template('welcomeboss.html')

@app.route('/welcomeasemployee')
def welcome_employee():
     return render_template('welcomeemployee.html')

# route for handling the login page logic
@app.route('/loginasboss', methods=['GET','POST'])
def login_boss():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if (request.form['username'] != app.config['USERNAME']) or (request.form['password'] != app.config['PASSWORD']):
                error = 'Invalid Credentials. Please try again.'
            else:
                #login_user(user)
                session['logged_in'] = True

                flash('You were just logged in!')
                return redirect(url_for('welcome_boss'))
            #if not session.get('logged_in'):
                #abort(500) 
    return render_template('login.html', form=form, error=error)


@app.route('/loginasemployee', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
             user = Employee.query.filter_by(e_id=request.form['username']).first()
             if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                 db.session.add(Attendance(request.form['username']))
                 login_user(user)
                 #session['logged_in'] = True

                 flash('You were just logged in!')
                 return redirect(url_for('welcome_employee'))

             else: 
                error = 'Invalid Credentials. Please try again.'
        
    return render_template('loginasemployee.html', form=form, error=error)     

@app.route('/logout')
def logout_boss():
    logout_user()
    #session.pop('logged_in', None)
    #flash('You were just logged out')
    return redirect(url_for('home'))



@app.route('/view')
def view():
    attendances = db.session.query(Attendance.e_id, Attendance.check_in_date , Employee.name).filter(Employee.e_id==Attendance.e_id).all()
    
    return render_template('view.html', attendances = attendances)

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.filter(Employee.e_id == int(user_id)).first()

@app.errorhandler(500)
def exception_handler(e):
    return render_template('500.html'), 500
#@app.route('/loginasemployee', methods=['GET','POST'])
#def add_entry():
   #if not session.get('logged_in'):
   #     abort(401) 
#   g.db = connect_db()
 #  g.db.execute('insert into attendance (emid, ename) values (?, ?)',
 #                [request.form.get['emid',None], request.form.get['ename',None]])
 #  g.db.commit()
 #  g.db.close()
 #  flash('You have just successfully logged in')

 #  return redirect(url_for('welcome'))
   
  # return render_template('loginasemployee.html')


#def connect_db():
#    return sqlite3.connect(app.config['DATABASE'])    
      
