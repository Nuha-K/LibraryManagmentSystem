import sqlite3
import datetime

def insert_booktxn(tx,conn):
    conn.execute("INSERT INTO book_trans VALUES (:book_id, :member_id, :checkout_dt, :e_return_dt, :a_return_dt, :status)",
              {'book_id': tx.book_id,
               'member_id': tx.member_id,
               'checkout_dt': tx.checkout_dt,
               'e_return_dt': tx.e_return_dt,
               'a_return_dt': tx.a_return_dt,
               'status': tx.status
               })
    conn.commit()

def update_booktxn(tx,conn,old_status):
    if old_status == "R":
        booktxn_update = """UPDATE book_trans SET status = :chg_status, 
                                          a_return_dt = :chg_a_return_dt,
                                          checkout_dt = :chg_checkout_dt,
                                          e_return_dt = :chg_e_return_dt
                    WHERE book_id =  :book_id
                    AND   member_id = :member_id
                    AND   status = :status2;"""
    else:
        booktxn_update = """UPDATE book_trans SET status = :chg_status, 
                                          a_return_dt = :chg_a_return_dt
                    WHERE book_id =  :book_id
                    AND   member_id = :member_id
                    AND   status = :status2;"""

    conn.execute(booktxn_update, {'book_id': tx.book_id,
                    'member_id': tx.member_id,
                    'chg_checkout_dt': tx.checkout_dt,
                    'chg_e_return_dt': tx.e_return_dt,
                    'chg_a_return_dt': tx.a_return_dt,
                    'chg_status': tx.status,
                    'status2': old_status})
    conn.commit()

def validate_CheckOut(b_id, m_id,c):
        book_select = "SELECT availability, reserve FROM book_master WHERE book_id = :fld_value;"
        c.execute(book_select, {'fld_value': b_id})
        data = c.fetchone()
        if data[0] == 'Y' and data[1] == '':
            status = ['Yes','']
            return status
        elif (data[0] == 'Y' or data[0] == 'N') and data[1] == 'R':
            book_select = "SELECT * FROM book_trans WHERE book_id = :fld_value and member_id = :fld2_value and status =:stat;"
            c.execute(book_select, {'fld_value': b_id, 'fld2_value': m_id, 'stat': "R"})
            result = c.fetchone()
            if result:
                status = ['Yes', 'Update']
                return status
            else:
                status = ['No','']
                return status
        else:
            status = ['No','']
            return status

def validate_UnReserve(b_id, c):
    book_select = "SELECT * FROM book_trans WHERE book_id = :fld_value and status = 'O';"
    c.execute(book_select, {'fld_value': b_id})
    data = c.fetchone()
    if data is None:
        status = 'Y'
    else:
        status = 'N'
    return status

class Transaction:

    def __init__(self):
        self.book_id = ' '
        self.member_id = ' '
        self.checkout_dt = ' '
        self.e_return_dt = ' '
        self.a_return_dt = ' '
        self.status = ' '

    def Set_a_return_dt(self):
        self.a_return_dt = datetime.date.today()

    def Get_a_return_dt(self):
        return self.a_return_dt

    def check_in(self,bk_id,mem_id,c,conn):
        while True:
            book_select = "SELECT * FROM book_trans WHERE book_id = :fld_value and member_id = :fld2_value and status = 'O';" \
                          and "SELECT * FROM book_master WHERE book_id = :fld_value and availability ='N' ;"
            c.execute(book_select, {'fld_value': bk_id, 'fld2_value': mem_id})
            data = c.fetchone()
            if data is not None:
                reserve_select = "SELECT reserve FROM book_master WHERE book_id = :fld_value;"
                c.execute(reserve_select, {'fld_value': bk_id})
                reserve_val = c.fetchone()
                if reserve_val[0] != 'R':
                    c.execute("""UPDATE book_master SET availability = :avbl_yes
                                WHERE book_id = :book_id""",
                                {'book_id': bk_id, 'avbl_yes': "Y"})
                    print("Book has been returned successfully ")
                    conn.commit()
                    break
                else:
                    print("This member has not checked out the book.")
                    break
            else:
                print("ERROR! Incorrect Book ID. Please try again")

    def get_memberId(self):
        return self.member_id

    def input_memberId_unreserve(self, bk_id, c):
        while True:
            self.member_id = input("Please enter your Member ID: ")
            member_select = "SELECT * FROM book_trans WHERE member_id = :fld_value and status = :fld2_value and book_id = :fld3_value;"
            c.execute(member_select, {'fld_value': self.member_id, 'fld2_value':'R', 'fld3_value': bk_id})
            data = (c.fetchone())
            if data is not None:
                break
            else:
                print("ERROR! Invalid  Member ID")
        return self.member_id

    def input_memberId(self,c):
        while True:
            self.member_id = input("Please enter your Member ID: ")
            member_select = "SELECT * FROM member_master WHERE member_id = :fld_value;"
            c.execute(member_select,{'fld_value': self.member_id})
            data = (c.fetchone())
            if data is not None:
                break
            else:
                print("ERROR! Please input a valid Member ID")
        return self.member_id

    def get_bookId(self):
        return self.book_id

    def input_bookId_check_in(self,c):
        while True:
            self.book_id = input("Please enter in the Book ID: ")
            book_select = "SELECT * FROM book_master WHERE book_id = :fld_value and availability = 'N';"
            c.execute(book_select, {'fld_value': self.book_id})
            data = c.fetchone()
            if data is not None:
                break
            else:
                print("ERROR! Book ID is unavailable")
        return self.book_id


    def input_bookId(self,c):
        while True:
                self.book_id = input("Please enter in the Book ID: ")
                book_select = "SELECT * FROM book_master WHERE book_id = :fld_value;"
                c.execute(book_select, {'fld_value': self.book_id})
                data = c.fetchone()
                if data:
                    break
                else:
                    print("ERROR! Book ID is unavailable")
        return self.book_id


    def input_bookId_reserve(self,c):
        while True:
            self.book_id = input("Please enter in the Book ID: ")
            book_select = "SELECT * FROM book_master WHERE book_id = :fld_value and reserve = '';"
            c.execute(book_select, {'fld_value': self.book_id})
            data = c.fetchone()
            if data is not None:
                break #if book is available
            else:
                print("ERROR! Book ID is unavailable. Please choose another book.")
        return self.book_id

    def input_bookId_unreserve(self,c):
        while True:
            self.book_id = input("Please enter in the Book ID: ")
            book_select = "SELECT * FROM book_master WHERE book_id = :fld_value and reserve = 'R';"
            c.execute(book_select, {'fld_value': self.book_id})
            data = c.fetchone()
            if data is not None:
                break
            else:
                print("ERROR! Enter the correct Book ID.")
        return self.book_id

    def get_checkout_date(self):
        return self.checkout_dt


    def checkout_date(self):
        self.checkout_dt = datetime.date.today()


    def get_return_date(self):
        return self.e_return_dt

    def return_date(self):
        self.e_return_dt = self.checkout_dt + datetime.timedelta(weeks=2)

    def update_bookmaster_avbl_no(self,conn):
        conn.execute("""UPDATE book_master SET availability = :avbl_no 
                WHERE book_id = :book_id""",
                {'book_id': self.book_id, 'avbl_no': "N"})
        conn.commit()

    def update_book_master_status(self, avilStatus, rsvStatus,conn):
        conn.execute("""UPDATE book_master SET availability = :avbl, reserve = :rsv
                WHERE book_id = :book_id""",
                {'book_id': self.book_id, 'avbl': avilStatus, 'rsv': rsvStatus})
        conn.commit()

    def get_update_book_master(self):
        return self.update_bookmaster_avbl_no

    def reserve_book(self,bk_id,mem_id,conn):
        conn.execute("""UPDATE book_master SET reserve = :res, availability = :avbl
            WHERE book_id = :book_id""",
            {'book_id': bk_id, 'res': "R", 'avbl': "N"})
        conn.commit()

    def unreserve_book(self,bk_id,mem_id, book_status, conn):
        conn.execute("""UPDATE book_master SET reserve = :res, availability = :avbl
                            WHERE book_id = :book_id""",
                  {'book_id': bk_id, 'res': "", 'avbl': book_status})
        conn.commit()

def Book_Txn_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    Flag = False
    while Flag == False:
        Choice = input("Would you like to:\n1. Check out a book\n2. Return a book\n3. Reserve a book\n4. Unreserve a book\n5. Go Back To Main Menu\nEnter in option: ")

        #CHECKOUT
        if Choice == "1":
            x = Transaction()
            b_id = x.input_bookId(cur)
            m_id = x.input_memberId(cur)
            status = validate_CheckOut(b_id, m_id, cur)
            if status[0] == 'Yes':
                x.checkout_date()
                x.return_date()
                z = x.get_memberId()
                y = x.get_bookId()
                q = x.get_checkout_date()
                v = x.get_return_date()
                print(z, y, q, v)
                x.status = "O"
                #To ensure that when a user checks out a book they reserved the reserve status is changed to "U" which means available
                if status[1] == 'Update':
                    old_status = "R"
                    update_booktxn(x,conn,old_status)
                    x.update_book_master_status("N","",conn)
                else:
                    insert_booktxn(x, conn)
                    x.update_bookmaster_avbl_no(conn)
                    x.get_update_book_master()
                print("Book has been checked out successfully.")
                cont = input("Would you like to continue? Type Y or N: ")
                cont = cont.upper()
                if cont == "Y":
                    Flag = False
                elif cont == "N":
                    Flag = True
                else:
                    print("Wrong value entered. Please try again")
                    Flag = False
            else:
                print("Sorry the book is unavailable")
        # CHECK IN
        elif Choice == "2":
                x = Transaction()
                bk_id = x.input_bookId_check_in(cur)
                mem_id = x.input_memberId(cur)
                x.check_in(bk_id, mem_id,cur,conn)
                x.status = "I"
                x.Set_a_return_dt()
                x.Get_a_return_dt()
                old_status = "O"
                #insert_booktxn(x,conn)
                update_booktxn(x,conn,old_status)
                cont = input("Would you like to continue? Type Y or N: ")
                cont = cont.upper()
                if cont == "Y":
                    Flag = False
                elif cont == "N":
                    Flag = True
                else:
                    print("Wrong value entered. Please try again")
                    Flag = False

        #RESERVE
        elif Choice == "3":
            x = Transaction()
            bk_id = x.input_bookId_reserve(cur)
            mem_id = x.input_memberId(cur)
            x.checkout_date()
            x.status = "R"
            x.reserve_book(bk_id,mem_id,conn)
            insert_booktxn(x,conn)
            print("Book has been reserved successfully.")
            cont = input("Would you like to continue? Type Y or N: ")
            cont = cont.upper()
            if cont == "Y":
             Flag = False
            elif cont == "N":
             Flag = True
            else:
             print("Wrong value entered. Please try again")
             Flag = False
        #UNRESERVE
        elif Choice == "4":
            x = Transaction()
            bk_id = x.input_bookId_unreserve(cur)
            mem_id = x.input_memberId_unreserve(bk_id, cur)
            x.status = "U"
            x.Set_a_return_dt()
            book_status = validate_UnReserve(bk_id, cur)
            x.unreserve_book(bk_id, mem_id, book_status, conn)
            old_status = "R"
            update_booktxn(x, conn, old_status)
            print("Book has been unreserved successfully.")
            cont = input("Would you like to continue? Type Y or N: ")
            cont = cont.upper()
            if cont == "Y":
                Flag = False
            elif cont == "N":
                Flag = True
            else:
                print("Wrong value entered. Please try again")
                Flag = False
        #Go Back To Menu
        elif Choice == "5":
            break
        #ERROR
        else:
            print("ERROR. Wrong value entered")
            Flag = False

    conn.close()
