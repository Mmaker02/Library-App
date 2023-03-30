import mysql.connector
from decimal import Decimal, InvalidOperation
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="examlibrary"
)
cursor = mydb.cursor()


#id,name,location
class Library:

    def __init__(self, id,name,location):
        self.id = id
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.id} {self.name}'

    def __repr__(self):
        return f'{self.id} {self.name}'

    def print_all_books(self):
        cursor.execute(f'SELECT id,title,genre,publisher FROM books WHERE library_id = {self.id}')
        library_books = cursor.fetchall()
        if(len(library_books) == 0):
            print("No books in this library...")
            return None
        for book in library_books:
            print(f'ID - {book[0]}: Book title:{book[1]} Book genre: {book[2]} Book publisher: {book[3]}')
        return len(library_books)

    def get_name(self): return self.name

    @staticmethod
    def edit_book_info(book_id,new_book_title,new_book_author, new_book_genre, new_book_publisher):
        try:
            cursor.execute(f'SELECT * FROM books WHERE id = {book_id}')
            fetch_book_data = cursor.fetchone();
            book_to_update = Book(*fetch_book_data)
            book_to_update.update_info(new_book_title,new_book_author, new_book_genre, new_book_publisher)
        except:
            print("\nThere was a problem in editing the book you selected. Make sure you entered valid ID and try again.")

    def add_book(self,new_book_title,new_book_author, new_book_genre, new_book_publisher):
        try:
            sql = f'INSERT INTO books (title, author, genre, publisher, library_id) VALUES ("{new_book_title}","{new_book_author}","{new_book_genre}","{new_book_publisher}",{self.id});'
            cursor.execute(sql)
            mydb.commit()
            print("Book added!")
        except:
            print("\nThere was a problem in adding the book. Make sure you entered valid information and try again.")


    @staticmethod
    def delete_book(book_id):
        try:
            cursor.execute(f'SELECT * FROM books WHERE id = {book_id}')
            fetch_book_data = cursor.fetchone();
            book_to_delete = Book(*fetch_book_data)
            book_to_delete.delete_self()
        except:
            print("\nThere was a problem in deleting the book you selected. Make sure you entered valid ID and try again.")



#id,title,author,genre,publisher,library_id
class Book:
    def __init__(self, id,title,author,genre,publisher,library_id):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.library_id = library_id

    def update_info(self,title,author, genre, publisher):

        cursor.execute(f'''
        UPDATE books
        SET title = '{title}', author = '{author}', genre='{genre}', publisher='{publisher}'
        WHERE id = {self.id}
        ''')
        mydb.commit()
        print("Updated info!")

    def delete_self(self):
        #DELETE FROM table_name WHERE condition;
        cursor.execute(f'''
        DELETE FROM books
        WHERE id = {self.id}
        ''')
        mydb.commit()
        print("Book deleted!")
