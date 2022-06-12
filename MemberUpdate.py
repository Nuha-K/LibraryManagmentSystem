import sqlite3

def search_all():
    while True:
        option = ['blank', 'first_name', 'last_name', 'email']
        search_option = int(input("What would you like to update 1. First Name, 2. Last Name or 3. Email. Enter Option 1, 2 or 3: "))
        if search_option > 3 or search_option < 1:
            print("ERROR. INVALID OPTION")
        else:
            break
    return option[search_option]

def member():
    mem_id = input("Enter in the Member ID: ")
    return mem_id

def search_info():
        search_value = input("Enter in the updated information: ")
        return search_value

def Member_Update_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    while True:
        usr_opt = member()
        usr_field = search_all()
        usr_str = search_info()
        sql_select = "SELECT * FROM member_master WHERE member_id =:fld_value;"
        cur.execute(sql_select, {'fld_value': usr_opt})
        data = cur.fetchall()
        for row in data:
            print(row)

        Ans = input("Is this the Member you'd like to update? Press 'Y' if so: ")
        z = Ans.upper()
        if z == "Y":
            sql_update = "UPDATE member_master SET "+usr_field+" =:usr_str WHERE member_id =:fld_value;"
            cur.execute(sql_update, {'fld_value': usr_opt, 'usr_str': usr_str})
            cur.execute(sql_select, {'fld_value': usr_opt})
            conn.commit()
            print("Update Complete")
            break
        else:
            print("Okay. Record not Updated. Exiting")
            break
    conn.close()


