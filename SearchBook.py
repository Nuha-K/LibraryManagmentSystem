import sqlite3

def search_all():
    while True:
        option = ['blank', 'book_name', 'author', 'isbn', 'genre']
        search_option = int(input( "You can search by 1. Title, 2. Author, 3. ISBN or 4. Genre. Enter Option 1, 2, 3, or 4: "))
        if search_option > 4 or search_option < 1:
            print("ERROR. INVALID OPTION")
        else:
            break
    return option[search_option]

def search_info():
        search_value = input("Enter Title, Author, ISBN or Genre: ")
        return '%'+search_value+'%'

def Search_Book_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    usr_opt = search_all()
    usr_str = search_info()
    sql_select = "SELECT * FROM book_master WHERE "+usr_opt+" like :fld_value;"
    cur.execute(sql_select, {'fld_value': usr_str})
    data = cur.fetchall()
    if data:
        for row in data:
            print(row)
    else:
        print("Sorry. There is no such Book in the system ")
    conn.commit()
    conn.close()


# Control Code
#if __name__ == "__main__":
#    Main_all()
#

