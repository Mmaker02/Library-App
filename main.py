#import load_csvs
#BELEJKA: Za da suzdadete bazata danni trqbva da otkomentirate load_csvs importa. Az sum si q suzdal veche i zatova sum go zakomentiral!
import mysql.connector
from models import Library

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="examlibrary"
)
cursor = mydb.cursor()



while True:
    get_libraries_sql = 'SELECT id,name FROM libraries;'
    cursor.execute(get_libraries_sql)
    libraries_to_show = cursor.fetchall()
    print("---Libraries---:")
    for library in libraries_to_show:
        print(f'ID - {library[0]}: {library[1]}')
    get_library = int(input("Select a library (By selecting its ID)[Select 0 to exit]: "))
    if(get_library == 0): quit()
    try:
        cursor.execute(f'SELECT * FROM libraries WHERE id = {get_library}')
        fetch_library_data = cursor.fetchone();
        library = Library(*fetch_library_data)
    except:
        print("Invalid Library ID!")
        quit()

    while True:
        option_input = int(input("What would you like to do? \n1.Show all books\n2.Edit book\n3.Delete book\n4.Add book\n5.Go to main menu:"))
        if(option_input == 1):
            print(f"\n--Books in library {library.get_name()}--")
            print()
            library.print_all_books()
        elif(option_input == 2):
            books_any = library.print_all_books()
            if(books_any == None):
                continue
            print()
            book_id = int(input("Which book would you like to edit? (ID): "))
            print("Please provide new information in this format:")
            print("title,author,genre,publisher")
            print()
            new_info = input().split(',')
            if(len(new_info) != 4):
                print("Invalid info...")
                continue

            new_book_title = new_info[0]
            new_book_author = new_info[1]
            new_book_genre = new_info[2]
            new_book_publisher = new_info[3]

            library.edit_book_info(book_id,new_book_title,new_book_author, new_book_genre, new_book_publisher)
        elif(option_input == 3):
            books_any = library.print_all_books()
            if(books_any == None):
                continue
            print()
            book_id = int(input("Which book would you like to delete? (ID): "))
            library.delete_book(book_id)
        elif(option_input == 4):
            print("Please provide information in this format:")
            print("title,author,genre,publisher")
            print()
            new_info = input().split(',')
            if(len(new_info) != 4):
                print("Invalid info...")
                continue

            new_book_title = new_info[0]
            new_book_author = new_info[1]
            new_book_genre = new_info[2]
            new_book_publisher = new_info[3]

            library.add_book(new_book_title,new_book_author, new_book_genre, new_book_publisher)
        elif(option_input == 5):
            break;
        else:
            print("Invalid option!")