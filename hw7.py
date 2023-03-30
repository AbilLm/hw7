import sqlite3


conn = sqlite3.connect('students.db')


conn.execute('''CREATE TABLE students
                (id INTEGER PRIMARY KEY,
                hobby TEXT,
                first_name TEXT,
                last_name TEXT,
                birth_year INTEGER,
                homework_score INTEGER);''')


students_data = [(1, 'чтение', 'Джаннат', 'Одинсон', 2000, 8),
                 (2, 'плавание', 'Мирдан', 'Чифкиффович', 1999, 10),
                 (3, 'живопись', 'Ахмад', 'Дагестан', 2001, 6),
                 (4, 'игра на гитаре', 'Ислам', 'Махачкала', 2005, 10),
                 (5, 'танцы', 'Тони', 'Старк', 2008, 14),
                 (6, 'фотография', 'Аскар', 'Кефтеме', 2006, 9),
                 (7, 'кулинария', 'Михаил', 'Капрафилов', 2007, 7),
                 (8, 'компьютерные игры', 'Бекболот', 'Айпидинов', 2009, 10),
                 (9, 'рисование', 'Бекболот', 'Джумагулов', 2000, 8),
                 (10, 'бег', 'Абил', 'Сагадылдаев', 2008, 9)]

for student in students_data:
    conn.execute("INSERT INTO students (id, hobby, first_name, last_name, birth_year, homework_score) \
                  VALUES (?, ?, ?, ?, ?, ?)", student)

cursor = conn.execute("SELECT * FROM students WHERE length(last_name) > 10")
for row in cursor:
    print(row)

conn.execute("UPDATE students SET first_name = 'genius' WHERE homework_score > 10")
cursor = conn.execute("SELECT * FROM students WHERE first_name = 'genius'")
for row in cursor:
    print(row)
conn.execute("DELETE FROM students WHERE id % 2 = 0")
conn.commit()
conn.close()
