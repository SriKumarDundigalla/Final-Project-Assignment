

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE About_Course (imgURL TEXT, courseName TEXT,aboutCourse TEXT)')

print("Created table successfully!")

conn.close()
