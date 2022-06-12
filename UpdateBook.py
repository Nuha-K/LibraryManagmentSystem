import sqlite3

def search_all():
    while True:
        option = ['blank', 'book_name', 'author', 'isbn', 'genre']
        search_option = int(input("What would you like to update 1. Title, 2. Author, 3. ISBN or 4. Genre. Enter Option 1, 2, 3, or 4: "))
        if search_option > 4 or search_option < 1:
            print("ERROR. INVALID OPTION")
        else:
            break
    return option[search_option]

def book(cur):
    while True:
        book_id = input("Please enter in the Book ID: ")
        book_select = "SELECT * FROM book_master WHERE book_id = :fld_value;"
        cur.execute(book_select, {'fld_value': book_id})
        data = cur.fetchone()
        if data is not None:
            break
        else:
            print("ERROR! Book ID is unavailable or incorrect")
    return book_id

def search_info():
        search_value = input("Enter the information you would like to update: ")
        return search_value

def Update_Book_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    while True:
        usr_opt = book(cur)
        usr_field = search_all()
        usr_str = search_info()

        sql_select = "SELECT * FROM book_master WHERE book_id =:fld_value;"
        cur.execute(sql_select, {'fld_value': usr_opt})
        for row in cur.fetchall():
            print(row)

        Ans = input("Is this the book you'd like to update? Press 'Y' or 'N': ")
        Update_Answer = Ans.upper()

        if Update_Answer == "Y":
            sql_update = "UPDATE book_master SET "+usr_field+" =:usr_str WHERE book_id =:fld_value;"
            cur.execute(sql_update, {'fld_value': usr_opt, 'usr_str': usr_str})
            cur.execute(sql_select, {'fld_value': usr_opt})
            print(cur.fetchone(), "\nBook Updated")
            break
        else:
            print("Okay. Record not Updated. Exiting")
            break
    conn.commit()
    conn.close()