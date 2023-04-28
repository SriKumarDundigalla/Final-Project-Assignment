import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE mycourse (Email TEXT NOT NULL,usercourse Text)')


print("Created table successfully!")

conn.close()