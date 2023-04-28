import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE users (first_name TEXT NOT NULL, last_name TEXT NOT NULL,email  TEXT PRIMARY KEY, password TEXT NOT NULL)')


print("Created table successfully!")

conn.close()