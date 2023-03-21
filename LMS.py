import db
from log import success
from log import failed

class Library :
    def __init__(self):        
        print('''\t Welcome to the Custom Library\t''')
        print()

    
    def getAvailableBooks(self,name):
        """Function for getting the available books"""
        
        print("The available books are :")
        ret = db.getAvailableBooks()
        if ret[0]:
            success.getAvailableBooks(name)
        else:
            failed.getAvailableBooks(name)
            

    def AddBook(self):
        """Function to add book in Library"""

        name = input("Enter name of the book:")
        price= input("Enter price of the book:")

        ret = db.AddBook(name,price)
        if ret[0]:
            print(f"The {name} book has been added in custom Library with price {price}. Thank you for your support!")
            success.AddBook(name,price)
        else:
            failed.AddBook(name,ret[1])
            

    def AddUser(self):
        """Add new user to user record"""

        name = input("Enter your username :")
        Pass = input("Enter your Password :").encode('utf-8')
        email = input("Enter your email :")

        ret = db.AddUser(name,Pass,email)
        if ret[0]:
            print(f"{name} has been added sucessfully!")
            success.AddUser(name)
        else:
            failed.AddUser(name,ret[1])
            
            
    def RemoveUser(self):
        """Remove user from user success"""

        name = input("Enter username :")

        ret = db.RemoveUser(name)
        if ret[0]:
            print(f"{name} has been removed successfully!")
            success.RemoveUser(name)
        else:
            failed.RemoveUser(name,ret[1])
            

class Students:
    def BorrowBook(self,uname):
        """USer can borrow the book

        Args:
            uname (string): user name
        """
        
        bname = input("Enter the book you want to borrow: ")
        ret = db.BorrowBook(uname,bname)

        if ret[0]:
            print(f"{bname} Book has been added successfully.")
            success.BorrowBook(uname,bname)
        else:
            failed.BorrowBook(uname,bname,ret[1])
            print("The requested book is not available")
            print()
            print("Here are the available books:")
            custom.getAvailableBooks(uname)


    def ReturnBook(self,uname):
        """User can return the borrowed book
        
        Args:
            uname (string): User name
        """
        
        bname = input("Enter the book you want to return: ")
        ret = db.ReturnBook(uname,bname)

        if ret[0]:
            print(f"{bname} has been return successfully!")
            success.ReturnBook(uname,bname)
        else:
            print(ret[1])
            failed.ReturnBook(uname,bname,ret[1])
            print("Here is the list of borrowed books:")
            self.getBorrowedBooks(uname)


    def signin(self):
        """User authentication function -> checks for username and password

        Returns:
            List: Returns the true and false for successful and unsuccessful try. When it is successful also returns the name of the user
        """
        name = input("Enter Your name :")
        Pass = input("Enter Your Password:").encode('utf-8')

        val = db.checkUser(name,Pass)
        
        if val[0]:
            print(f"\nWelcome {name},We wish you great time in custom Library.\n")
            success.logged_in(name)
            return [True,name]
        else:
            return [False,name]

   
    def getBorrowedBooks(self,name):
        """print all the borrowed books

        Args:
            name (String): User name
        """

        print("The borrowed books are :")
        ret = db.getBorrowedBooks(name)
        if ret[0]:
            success.getBorrowedBooks(name)
        else:
            print(ret[1])
            failed.getBorrowedBooks(name,ret[1])
            
            
#Main Function            
if __name__ == "__main__":
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
                    success.logged_out(name)
                    break 
                else:
                    print("The invalid input is given.Please try again!")

            else :
                print("\nYou have enter either username or password Wrong.\nPress 1, if you want to try once again!\nPress 2, If you want to sign up for custom Library.\nPress 3, If you want to exit the Library.\n")

                b = input("Enter the number :")
                if b == "1":
                    check = student.signin()[0]
                    continue
                elif b == "2":
                    custom.AddUser()
                    continue
                elif b == "3":
                    success.logged_out(name)
                    print(f"Thank you {name}, for visiting the Custom Librabry.Have a good day!")
                    break
                else:
                    print("Invalid Input!")