import csv
import mysql.connector

def load_information_from_csv(file_path):

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return list(reader)


connector = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=3306,
)

cursor = connector.cursor()

#id,name,location
#id,title,author,genre,publisher,library_id
cursor.execute('CREATE DATABASE IF NOT EXISTS examlibrary')
cursor.execute('USE examlibrary')
#CREATE LIBRARIES TABLE
cursor.execute('''
CREATE TABLE IF NOT EXISTS libraries(  
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(150),  
    location VARCHAR(150),  
    PRIMARY KEY (id)  
);
''')

#CREATE BOOKS TABLE
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(  
    id INT NOT NULL AUTO_INCREMENT primary key,  
    title VARCHAR(150),  
    author VARCHAR(150),  
    genre VARCHAR(150),  
    publisher VARCHAR(150),
    library_id INT,
    FOREIGN KEY (library_id) REFERENCES libraries(id)
 
);
''')



libraries = load_information_from_csv('libraries.csv')
for library in libraries:
    sql = f"INSERT INTO libraries (name,location) VALUES ('{library[1]}', '{library[2]}');"
    cursor.execute(sql)

connector.commit()


books = load_information_from_csv('books.csv')
for book in books:
    sql = f'INSERT INTO books (title, author, genre, publisher, library_id) VALUES ("{book[1]}","{book[2]}","{book[3]}","{book[4]}",{book[5]});'
    cursor.execute(sql)

connector.commit()



