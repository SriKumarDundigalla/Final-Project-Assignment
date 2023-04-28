
import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")


conn.execute('''INSERT INTO About_Course (imgURL, courseName, aboutCourse,COST) VALUES
             ('course1.png', 'React.js', 'The Complete React Js & Redux Course - Build Modern Web Apps.','50'),
             ('course2.png', 'Python', 'Mastering the Fundamentals of Python Programming.','30'),
             ('course3.png', 'Node.js', 'Building Scalable and High-Performance Web Applications with JavaScript','30');
             ''')
conn.commit()

print("Inserted data successfully!")

conn.close()
