

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")


# conn.execute('CREATE TABLE Reviews (Name TEXT, review TEXT,rating INT)')
# conn.execute('DROP TABLE Reviews')
# print("Table created successfully!")
conn.execute('''INSERT INTO Reviews (name, review, rating) VALUES
('Brat Lee', 'The Learning Place is a popular choice among many of my employees for ongoing education. Compared to other options Ive explored, I believe it offers the finest variety, training, and curriculum. The courses are more detailed even if they may be lengthier than others.', 5),
('Brat Lee', 'The Learning Place is a popular choice among many of my employees for ongoing education. Compared to other options Ive explored, I believe it offers the finest variety, training, and curriculum. The courses are more detailed even if they may be lengthier than others.', 5),
('Brat Lee', 'The Learning Place is a popular choice among many of my employees for ongoing education. Compared to other options Ive explored, I believe it offers the finest variety, training, and curriculum. The courses are more detailed even if they may be lengthier than others.', 5),
('Brat Lee', 'The Learning Place is a popular choice among many of my employees for ongoing education. Compared to other options Ive explored, I believe it offers the finest variety, training, and curriculum. The courses are more detailed even if they may be lengthier than others.', 5)
''')

conn.commit()

print("Inserted data successfully!")

conn.close()
