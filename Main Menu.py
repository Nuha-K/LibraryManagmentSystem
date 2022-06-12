from CreateBook import Create_Book_Main
from SearchBook import Search_Book_Main
from UpdateBook import Update_Book_Main
from DeleteBook import delete_book_Main
from CreateMemberInfo import Create_Member_Main
from SearchMem import Search_Member_Main
from MemberUpdate import Member_Update_Main
from BookTXNInfo import Book_Txn_Main
from CreateLibDB import Create_DB_Main

def Main_Menu():
    Flag_Main = False
    while Flag_Main == False:
        print("LIBRARY MANAGEMENT SYSTEM")

        print("1. Book Maintenance \n2. Members Maintenance\n3. Book Transaction\n4. Database Maintenance\n5. Exit Program")
        choice = input("Select Option: ")
        #BOOK MAINTENANCE MENU
        if choice == "1":
            Flag_Bk = False
            while Flag_Bk == False:
                choice2 = input("Would you like to:\n1. Create Book\n2. Search Book\n3. Update Book\n4. Delete Book\n5. Go Back To Main Menu\nEnter in Option: ")
                if choice2 == "1":
                    Create_Book_Main()
                elif choice2 == "2":
                    Search_Book_Main()
                elif choice2 == "3":
                    Update_Book_Main()
                elif choice2 == "4":
                    delete_book_Main()
                elif choice2 == "5":
                    Flag_Bk = True
                else:
                    print("ERROR! INCORRECT OPTION ENTERED")
                    Flag_Bk = False

        #Members Maintenance Menu
        elif choice == "2":
            Flag_Mem = False
            while Flag_Mem == False:
                choice2 = input("Would you like to:\n1. Create Member\n2. Search Member\n3. Update Member\n4. Go Back To Main Menu\nEnter in Option:  ")
                if choice2 == "1":
                    Create_Member_Main()
                elif choice2 == "2":
                    Search_Member_Main()
                elif choice2 == "3":
                    Member_Update_Main()
                elif choice2 == "4":
                    Flag_Mem = True
                else:
                    print("ERROR! INVALID OPTION ENTERED")
                    Flag_Mem = False
        #Book Transaction Menu
        elif choice == "3":
            Book_Txn_Main()
        #Database/Table Maintenance Menu
        elif choice == "4":
            Create_DB_Main()
        #Exit Program
        elif choice == "5":
            print("Thanks for using the LIBRARY MANAGEMENT SYSTEM")
            Flag_Main = True
        else:
            print("ERROR. INVALID OPTION ENTERED")


if __name__ == "__main__":
    Main_Menu()
