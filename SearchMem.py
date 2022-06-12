import sqlite3

def search_all():
    while True:
        option = ['blank', 'member_id', 'first_name', 'last_name', 'email']
        search_option = int(input( "You can search by 1. Member ID, 2. First Name, 3. Last Name or 4. Email. Enter Option 1, 2, 3, or 4: "))
        if search_option > 4 or search_option < 1:
            print("ERROR. INVALID OPTION")
        else:
           break
    return option[search_option]

def search_info():
        search_value = input("Enter Member ID, First Name, Last Name or Email: ")
        return '%'+search_value+'%'

def Search_Member_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    usr_opt = search_all()
    usr_str = search_info()
    sql_select = "SELECT * FROM member_master WHERE "+usr_opt+" like :fld_value;"
    cur.execute(sql_select, {'fld_value': usr_str})
    data = cur.fetchall()
    if data:
        for row in data:
            print(row)
    else:
        print("Sorry. There is no such Member in the system ")

    conn.commit()
    conn.close()



