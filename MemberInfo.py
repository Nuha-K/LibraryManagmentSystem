class member_info:

    def __init__(self):
        self.member_id = ' '
        self.first_name = ' '
        self.last_name = ' '
        self.email = ' '

    def get_member_id(self):
        return self.member_id

    def set_member_id(self):
        while True:
            self.member_id = input("Enter in Member ID. The first two characters are alphabets in caps followed by 5 numbers: ")
            length = len(self.member_id)
            if (length == 7) and (self.member_id[0:2].isalpha())and (self.member_id[0:2].isupper()) and self.member_id[2:8].isnumeric() == True:
                break
            else:
                print("ERROR, INVALID MEMBER ID! The first two characters are alphabets in caps followed by 5 numbers. Please try again")

    def get_first_name(self):
        return self.first_name

    def set_first_name(self):
        while True:
            try:
                self.first_name = str(input("Please enter the members first name: "))
                break
            except ValueError:
                print("ERROR! Please input a valid name")

    def get_last_name(self):
        return self.last_name

    def set_last_name(self):
        while True:
            try:
                self.last_name = str(input("Please enter the members last name: "))
                break
            except ValueError:
                print("ERROR! Please input a valid name")

    def get_email(self):
        return self.email

    def set_email(self):
        while True:
            try:
                self.email = str(input("Please enter the members email id: "))
                break
            except ValueError:
                print("ERROR! Please input a valid email")
