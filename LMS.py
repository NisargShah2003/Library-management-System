from datetime import datetime 
import db

class Library :
    def __init__(self):        
        print()
        print('''\t Welcome to the Custom Library\t''')
        print()

    
    def getAvailableBooks(self,name):
        """Function for getting the available books"""
        
        db.getAvailableBooks()
        print("The available books are :")
        record.getAvailableBooks(name)


    def AddBook(self):
        """Function to add book in Library"""

        name = input("Enter name of the book:")
        price= input("Enter price of the book:")

        db.AddBook(name,price)
        print(f"The {name} book has been added in custom Library with price {price}. Thank you for your support!")
        record.AddBook(name,price)


    def AddUser(self):
        """Add new user to user record"""

        name = input("Enter your username :")
        Pass = input("Enter your Password :")
        email = input("Enter your email :")

        db.AddUser(name,Pass,email)
        record.AddUser(name)


    def RemoveUser(self):
        """Remove user from user record"""

        name = input("Enter username :")

        db.RemoveUser(name)
        record.RemoveUser(name)

class Students:
    def BorrowBook(self,uname):
        """USer can borrow the book

        Args:
            uname (string): user name
        """
        bname = input("Enter the book you want to borrow: ")
        db.BorrowBook(uname,bname)
        record.BorrowBook(uname,bname)

   
    def ReturnBook(self,uname):
        """User can return the borrowed book
        
        Args:
            uname (string): User name
        """
        bname = input("Enter the book you want to return: ")
        record.ReturnBook(uname,bname)
        db.ReturnBook(uname,bname)


    def signin(self):
        """User authentication function -> checks for username and password

        Returns:
            List: Returns the true and false for successful and unsuccessful try. When it is successful also returns the name of the user
        """
        name = input("Enter Your name :")
        Pass = input("Enter Your Password:")

        val = db.checkUser(name,Pass)
        if val:
            print(f"\nWelcome {name},We wish you great time in custom Library.\n")
            record.logged_in(name)
            return [True,name]
        else :
            return [False]

   
    def getBorrowedBooks(self,name):
        """print all the borrowed books

        Args:
            name (String): User name
        """
        record.getBorrowedBooks(name)

        print("The borrowed books are :")
        db.getBorrowedBooks(name)


class record:
    @staticmethod
    def time():
        """Returns the current time in string format"""

        now = datetime.now()
        current_time = now.strftime("%d/%m/%y %H:%M:%S")

        return current_time
    
    def logged_out(name):
        """Entry in record file when user logs out"""

        with open("Records.txt",'a') as f:
                f.write(f"{record.time()} : {name} have logged out.\n")

    def logged_in(name):
        """Entry in record file when user logs in"""

        with open("Records.txt",'a') as f:
                f.write(f"{record.time()} : {name} have logged in.\n")

    def getAvailableBooks(name):
        """Entry in record file when user gets the list of available books in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {name} have checked the list of availabled books.\n")

    def AddUser(name):
        """Entry in record file when new user is added into database"""

        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {name} has been added as user.\n")

    def RemoveUser(name):
        """Entry in record file when user is been removed from the database"""

        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {name} has been removed from user.\n")

    def AddBook(name,price):
        """Entry in record file when new book is added into database"""

        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {name} book has been added with price as {price}.\n")

    def BorrowBook(uname,bname):
        """Entry in record file when user borrows book in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {uname} have borrowed {bname}.\n")

    def ReturnBook(uname,bname):
        """Entry in record file when user returns book in library"""
        
        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {uname} have returned the borrowed {bname} book.\n")

    def getBorrowedBooks(uname):
        """Entry in record file when user gets the list of borrowed books in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{record.time()} : {uname} have checked the borrowed books.\n")
        
student = Students()
custom = Library()

inp = input("Press 1, If you want to sign in.\nPress 2, If you want to sign up.\n\nEnter the number: ")

if inp == "2":
    custom.AddUser()
    
    choice = input("\nPress 1, If you want to exit the Library\nPress 2, If you want to sign in.\n\nEnter the number: ")

    if choice == "1":
        exit()
        
if inp == "1" or choice == "2":
    ret = student.signin()
    check = ret[0]

    while(True):
        if check == True:
            
            name = ret[1]
            a = input('''Press 1 for getting the list of the available books.
Press 2 for adding any book to the Library.
press 3 for borrowing the book from the Library.
Press 4 for getting list of borrowed books.
Press 5 for returning the book you have borrowed.
Press 6 for remove user from database.
Press 7 for exit the Library.

        Enter the Number: ''')
                
            if a == "1":
                custom.getAvailableBooks(name)
                print()
            elif a == "2":
                custom.AddBook()
                print()
            elif a == "3":
                student.BorrowBook(name)
                print()
            elif a == "4":
                student.getBorrowedBooks(name)
                print()
            elif a == "5":
                student.ReturnBook(name)
                print()
            elif a == "6":
                custom.RemoveUser()
                print()
            elif a == "7":
                print(f"Thank you {name}, for visiting the Custom Librabry.Have a good day!")
                record.logged_out(name)
                break 
            else:
                print("The invalid input is given.Please try again!")

        else :
            print("\nYou have enter either Roll No. or name Wrong.\nPress 1, if you want to try once again!\nPress 2, If you want to sign up for custom Library.\nPress 3, If you want to exit the Library.\n")

            b = input("Enter the number :")
            if b == "1":
                check = student.signin()
                continue
            elif b == "2":
                custom.AddUser()
                continue
            elif b == "3":
                record.logged_out(name)
                print(f"Thank you {name}, for visiting the Custom Librabry.Have a good day!")
                break
            else:
                print("Invalid Input!")
