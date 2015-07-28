import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("sample.db") as connection:

# get a cursor object used to execute SQL commands  
    c = connection.cursor()

 # create the table
    c.execute("DROP TABLE IF EXISTS employee")
    c.execute("CREATE TABLE employee(emid INT, ename TEXT, email TEXT, PRIMARY KEY (emid, ename))")

# insert dummy data into the table  
    c.execute('INSERT INTO employee VALUES (1, "Bailey", "bailey@gmail.com")')
    c.execute('INSERT INTO employee VALUES (2, "Lala Ng", "lalang@gmail.com")')