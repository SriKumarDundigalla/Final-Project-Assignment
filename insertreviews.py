

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")


# conn.execute('CREATE TABLE Reviews (email TEXT PRIMARY KEY, review TEXT,rating INT)')
# # conn.execute('DROP TABLE Reviews')
# print("Table created successfully!")
conn.execute('''INSERT INTO Reviews (email, review, rating) VALUES
('BratLee@gmail.com', 'This is one of the best websites where a person may study at a very little cost from any domain and any area. The people who are learning from it as well as the teachers will find this helpful and advantageous. Thank you, The Learning Place.', 5),
('James@yahoo.com', 'The Learning Place is a popular choice among many of my employees for ongoing education. Compared to other options Ive explored, I believe it offers the finest variety, training, and curriculum. The courses are more detailed even if they may be lengthier than others.', 5),
('NhuXzang@edu.com', 'I have been a longtime user of The Learning Place and have over 85 courses on my account right now. Regardless of how recently a course was launched, I find the platform to be user-friendly, and you can get in touch with the teachers.', 5),
('RandyJasmine@edu.com', 'The courses are extremely affordable, very straightforward, and meet expectations... You may select from beginner to intermediate classes since they are all offered.They might cover some basic course elements, but you cant learn everything at a high level.', 5);
''')


conn.commit()

print("Inserted data successfully!")

conn.close()
