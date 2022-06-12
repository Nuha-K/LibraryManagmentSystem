import sqlite3

def Create_Lib_Tables(conn):
    conn.execute("drop table book_master")
    conn.execute("""CREATE TABLE book_master (
               book_id text primary key,
               ISBN text not null,
               book_name text not null,
               author text not null,
               genre text not null,
               availability text not null,
               reserve text,
               unique (book_id)
               )""")

    conn.execute("drop table member_master")
    conn.execute("""CREATE TABLE member_master (
           member_id text primary key,
           first_name text not null,
           last_name text not null,
           email text not null,
           unique (member_id)
           )""")

    conn.execute("drop table book_trans")
# For status the valid values are R-Reserved, O-Check-out, I-Check-in, "U"-Unreserve
    conn.execute("""CREATE TABLE book_trans (
               book_id text,
               member_id text,
               checkout_dt date,
               e_return_dt date,
               a_return_dt date,
               status text
               )""")
    conn.commit()

def Upload_Sample_Data(conn):
    conn.execute("INSERT INTO book_master VALUES ('HP19901', '0764598342123', 'Harry Potter and the Philosophers Stone', 'J. K. Rowling', 'Fantasy', 'Y', '')")
    conn.execute("INSERT INTO book_master VALUES ('HP19902', '0764598343321', 'Harry Potter and the Philosophers Stone', 'J. K. Rowling', 'Fantasy', 'Y', '')")
    conn.execute("INSERT INTO book_master VALUES ('PJ19903', '0764598344213', 'Percy Jackson and the Lightning Thief', 'Rick Riordan', 'Greek mythology', 'Y', '')")
    conn.execute("INSERT INTO member_master VALUES ('NK00001', 'John', ' Doe', 'john@email.com')")
    conn.execute("INSERT INTO member_master VALUES ('NK00002', 'Jane', 'Doe', 'jane@email.com')")
    conn.execute("INSERT INTO member_master VALUES ('NK00003', 'Jerry', 'Doe', 'jerry@email.com')")

    conn.commit()


def Delete_Data(conn):
    #delete contents of book trans
    conn.execute("DELETE FROM BOOK_TRANS")
    #delete contents of book master
    conn.execute("DELETE FROM book_master ")
    #delete contents of member master
    conn.execute("DELETE FROM member_master ")
    conn.commit()

def Print_All_Data(cur):
    #execute and print book master table
    cur.execute("SELECT * FROM book_master ")
    print("BOOK MASTER:")
    for row in cur.fetchall():
        print(row)
    print("\n")
    #execute and print member master table
    cur.execute("SELECT * FROM member_master ")
    print("MEMBER MASTER:")
    for row in cur.fetchall():
        print(row)
    print("\n")
    #execute book trans
    cur.execute("SELECT * FROM BOOK_TRANS")
    print("BOOK TRANSACTION:")
    for row in cur.fetchall():
        print(row)
    print("\n")
    print(cur.fetchall())

def Create_DB_Main():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    while True:
        Choice = input("Would you like to\n1. Create Database and Tables\n2. Upload Sample Data\n3. Delete Data\n4. Print Tables\n5. Go Back To Menu\nEnter in Option: ")
        if Choice == "1":
            Answer = input("WARNING. IF YOU USE THIS OPTION ALL THE DATA FROM THE TABLES WILL BE LOST. DO YOU WANT TO CONTINUE? PRESS 'Y' ELSE PRESS 'N':  ")
            Answer = Answer.upper()
            if Answer == "Y":
                Create_Lib_Tables(conn)
                print("Tables Created")
        elif Choice == "2":
            Delete_Data(conn)
            Upload_Sample_Data(conn)
            print("Sample Data Uploaded")
        elif Choice == "3":
            Delete_Data(conn)
            print("Data Deleted")
        elif Choice == "4":
            Print_All_Data(cur)
        elif Choice == "5":
            break
        else:
            print("ERROR! INCORRECT OPTION ENTERED")

    conn.close()