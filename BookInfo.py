class book_info:

    def __init__(self):
        self.book_id = ' '
        self.isbn = ' '
        self.book_name = ' '
        self.author = ' '
        self.genre = ' '
        self.availability = ' '
        self.reserve = ' '

    def Get_available(self):
        return self.availability

    def Set_availability(self):
        self.availability = "Y"

    def Set_reserve(self):
        self.reserve = ""

    def Get_reserve(self):
        return  self.reserve

    def Get_BookID(self):
        return self.book_id

    def Set_BookID(self):
        while True:
            self.book_id = input("Please enter in the book ID. The first two characters are alphabets in caps followed by 5 numbers:  ")
            length = len(self.book_id)
            if (length == 7) and (self.book_id[0:2].isalpha()) and (self.book_id[0:2].isupper()) and self.book_id[2:8].isnumeric() == True:
                break
            else:
                print("ERROR, INVALID BOOK ID! The first two characters are alphabets in caps followed by 5 numbers. Please try again")

    def Get_ISBN(self):
        return self.isbn

    def Set_ISBN(self):
       while True:
            self.isbn = input("Please enter in the book's ISBN: ")
            length = len(self.isbn)
            if length == 13 and self.isbn.isnumeric():
                break
            else:
                print("ERROR! Please input an valid ISBN, which is 13 digits")

    def Get_Book_Name(self):
        return self.book_name

    def Set_Book_Name(self):
        while True:
            try:
                self.book_name = str(input("Please enter in the book's name: "))
                break
            except ValueError:
                print("ERROR! Please input an valid name")

    def Get_Author(self):
        return self.author

    def Set_author(self):
       while True:
           try:
               self.author = str(input("Please enter in the name of the book's author: "))
               break
           except ValueError:
               print("ERROR! Please input an valid name")

    def Get_genre(self):
        return self.genre

    def Set_genre(self):
       while True:
           try:
               self.genre = str(input("Please enter in the genre of the book: "))
               break
           except ValueError:
               print("ERROR! Please input an valid genre")
