import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE userCourses (Email TEXT NOT NULL,courseName Text ,PRIMARY KEY(Email, courseName))')


print("Created table successfully!")

conn.close()