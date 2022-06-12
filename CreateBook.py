import sqlite3
from BookInfo import book_info

def insert_book(bk,conn):
    conn.execute("INSERT INTO book_master VALUES (:book_id,:ISBN, :book_name,:author,:genre, :availability, :reserve)",
                {'book_id': bk.book_id,
                 'ISBN': bk.isbn,
                 'book_name': bk.book_name,
                 'author': bk.author,
                 'genre': bk.genre,
                 'availability': bk.availability,
                 'reserve': bk.reserve
                 })
    conn.commit()

def check_book_exists(book_id,cur):
    sql_select = "SELECT * FROM book_master WHERE book_id like :fld_value;"
    cur.execute(sql_select, {'fld_value': book_id})
    data = cur.fetchall()
    if data:
        print(data)
        print("Sorry. Book ID already exists, please use another ID")
        return False
    else:
        return True


def Create_Book_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
#Initialise and create an book_info object
    bkx = book_info()

#Ask the user to enter the Book id and also check if member exists to avoid duplicates
    while True:
        bkx.Set_BookID()
        book_id = bkx.Get_BookID()
        result = check_book_exists(book_id,cur)
        if result == True:
            break
#Ask the user to enter the book id
    #bkx.Set_BookID()
#Ask the user to enter the book name
    bkx.Set_Book_Name()
#Ask user to enter in ISBN
    bkx.Set_ISBN()
#Ask user to enter in the books author
    bkx.Set_author()
#ask user to input the books genre
    bkx.Set_genre()
#set avaiablity to "y"
    bkx.Set_availability()
    bkx.Set_reserve()
#Just checking if the values have been set in the book-info object
    y = bkx.Get_BookID()
    z = bkx.Get_Book_Name()
    w = bkx.Get_ISBN()
    t = bkx.Get_Author()
    j = bkx.Get_genre()
    p = bkx.Get_available()
    r = bkx.Get_reserve()
    print(y, z, w, t, j, p, r)
#Call the SQL function to insert the values received from the user
    insert_book(bkx,conn)
#Close the SQL database connection
    conn.close()