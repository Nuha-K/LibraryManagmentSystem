import sqlite3

def fetch_id():
    delete_var = input("Enter in the book Id of the book you wish to delete: ")
    return delete_var

def delete_book_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    while True:
        id = fetch_id()
        sql_select = "SELECT * FROM book_master WHERE book_id = :fld_value;"
        cur.execute(sql_select, {'fld_value': id})
        data = cur.fetchone()
        if data:
            print(data[0:4])
            confirmed_ans = input("IS THIS THE BOOK YOU'D LIKE TO DELETE? TYPE Y OR N TO CONFIRM: ")
            confirmed_ans = confirmed_ans.upper()
            if confirmed_ans == "Y":
                sql_delete = """DELETE from book_master where book_id = ?"""
                cur.execute(sql_delete, (id,))
                print("Record deleted successfully")
                break
            else:
                break
        else:
            print("ERROR! Invalid Book ID entered or Book not in records")
            break

    conn.commit()
    conn.close()






