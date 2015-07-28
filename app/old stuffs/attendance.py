import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("sample.db") as connection:

# get a cursor object used to execute SQL commands  
    c = connection.cursor()

 # create the table
    c.execute("DROP TABLE IF EXISTS attendance")
    
    c.execute("CREATE TABLE attendance(emid INT NOT NULL, ename TEXT NOT NULL, Check_in DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')) NOT NULL, FOREIGN KEY (emid, ename) REFERENCES employee(emid, ename))")

# insert dummy data into the table  
    #c.execute('INSERT INTO attendance(emid, ename) VALUES (1, "Bailey")')
    #c.execute('INSERT INTO attendance(emid, ename) VALUES (2, "Lala Ng")')