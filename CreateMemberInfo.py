import sqlite3
from MemberInfo import member_info

def insert_member(mem, conn):
    conn.execute("INSERT INTO member_master VALUES (:member_id,:first_name, :last_name,:email)",
                {'member_id': mem.member_id,
                 'first_name': mem.first_name,
                 'last_name': mem.last_name,
                 'email': mem.email
                 })
    conn.commit()

def check_member_exists(mem_id,cur):
    sql_select = "SELECT * FROM member_master WHERE member_id like :fld_value;"
    cur.execute(sql_select, {'fld_value': mem_id})
    data = cur.fetchall()
    if data:
        print(data)
        print("Sorry. Member ID already exists, please use another ID")
        return False
    else:
        return True

def Create_Member_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
#Initialise and create an Member_info object
    memX = member_info()
#Ask the user to enter the Member id and also check if member exists to avoid duplicates
    while True:
        memX.set_member_id()
        mem_id = memX.get_member_id()
        result = check_member_exists(mem_id,cur)
        if result == True:
            break
#Ask the user to enter the Member First name
    memX.set_first_name()
#Ask the user to enter the Member Last name
    memX.set_last_name()
#Ask the user to enter the Member Email ID
    memX.set_email()
#Just checking if the values have been set in the member-info object
    y = memX.get_member_id()
    z = memX.get_first_name()
    w = memX.get_last_name()
    t = memX.get_email()
    print(y, z, w, t)
#Call the SQL function to insert the values received from the user
    insert_member(memX,conn)
#Close the SQL database connection
    conn.close()
