from datetime import datetime 

class Library :
    def __init__(self,AvailableBooks):
        self.books = AvailableBooks
        self.borrowList=[]
        
        print()
        print('''\t Welcome to the Custom Library\t''')
        print()

    def getAvailableBooks(self):
        with open("Records.txt",'a') as f:
            f.write(f"{log.time()} : {name1} have checked the list of available books in custom Library.\n")

        print("The available books are :")
        for book in self.books:
            print(f"    {book}")

    def getBorrowedBooks(self):
        log.borrow_book()

        print("The borrowed books are :")
        for book in self.borrowList:
            print(f"{book}, ")

    def AddBook(self,add):
        with open("Records.txt",'a') as f:
            f.write(f"{log.time()} : {name1} have add {add}.\n")

        print(f"The {add} book has been added in custom Library. Thank you for your support!")
        self.books.append(add)

    def BorrowBook(self,name,borrow):
        if borrow in self.books:
            print(f"The {borrow} book is successfully borrowed by {name}. Please make sure to return it safely within 30 days.")

            with open("Records.txt",'a') as f:
                f.write(f"{log.time()} : {name1} have borrowed {borrow}.\n")

            self.books.remove(borrow)
            self.borrowList.append(borrow)
            
            print("Available books after changes being made:")
        else :
            print(f"Sorry {name}, The book you are asking is not available.\nYou can check for that book later.")
            
        self.getAvailableBooks()

    def ReturnBook(self,returnbook):
        
        if returnbook in self.borrowList:
            print(f"The {returnbook} has been return successfully. Thank you for returning safe and wish you a good day!")

            with open("Records.txt",'a') as f:
                f.write(f"{log.time()} : {name1} have returned {returnbook}.\n")

            self.books.append(returnbook)
            self.borrowList.remove(returnbook)
        else :
            print("You can't return the book you have not borrow. Please check the book name once again .")

class Students:
    def __init__(self):
        self.studentList = {"Kaushik":"2",
                           "Supan":"3",
                           "Hetal":"1"}

    def AddStudent(self):
        n = input("Enter your name :")
        if n in self.studentList:
            print("The username already exists! please try again")
            print()
            self.AddStudent()
        else:
            p = input("Enter the password:")
            self.studentList[n] =  p

    def getdetails(self):
        global name1
        name1 = input("Enter Your name :")
        rollNo = input("Enter Your RollNo. :")

        if self.studentList.get(name1) == rollNo:
            print(f"\nWelcome {name1},We wish you great time in custom Library.\n")
            log.logged_in()
            return True
        else :
            return False

    def RequestBook(self):
        req_book = input("Enter the book you want to request for : :")
        return req_book

    def ReturnBooks(self):
        ret_book = input("Enter the book you want to return :")
        return ret_book

class record :
    @staticmethod
    def time():
        now = datetime.now()
        current_time = now.strftime("%d/%m/%y %H:%M:%S")

        return current_time
    def logged_out(self):
        with open("Records.txt",'a') as f:
                f.write(f"{log.time()} : {name1} have logged out.\n")
    def logged_in(self):
        with open("Records.txt",'a') as f:
                f.write(f"{log.time()} : {name1} have logged in.\n")
    def borrow_book(self):
        with open("Records.txt",'a') as f:
            f.write(f"{log.time()} : {name1} have checked the list of borrowed books.\n")
        
student = Students()
custom = Library(["Python","C","C++","Java","PHP"])
log = record()

try:
    inp = int(input("Press 1, If you want to sign in.\nPress 2, If you want to sign up.\n\nEnter the number: "))
except:
    print("Invalid Input!")

if inp == 2:
    student.AddStudent()
    try:
        choice = int(input("\nPress 1, If you want to exit the Library\nPress 2, If you want to sign in.\n\nEnter the number: "))
    except:
        print("Invalid Input!")

    if choice == 1:
        exit()
if inp == 1 or choice == 2:
    check = student.getdetails()

    while(True):
        if check == True:
            try:
                a = int(input('''\tPress 1 for getting the list of the available books.
        Press 2 for adding any book to the Library.
        press 3 for borrowing the book from the Library.
        Press 4 for geeting list of borrowed books.
        Press 5 for returning the book you have borrowed.
        Press 6 for exit the Library.

    Enter the Number : '''))
            except:
                print("Invalid Input!")
                
            if a == 1:
                custom.getAvailableBooks()
                print()
            elif a == 2:
                b = input("Enter the book you want to add :")
                custom.AddBook(b)
                print()
            elif a == 3:
                custom.BorrowBook(student.name(),student.RequestBook())
                print()
            elif a == 4:
                custom.getBorrowedBooks()
                print()
            elif a == 5:
                custom.ReturnBook(student.ReturnBooks())
                print()
            elif a == 6:
                print(f"Thank you {name1}, for visiting the Custom Librabry.Have a good day!")
                log.logged_out()
                break 
            else:
                print("The invalid input is given.Please try again!")

        else :
            print("\nYou have enter either Roll No. or name Wrong.\nPress 1, if you want to try once again!\nPress 2, If you want to sign up for custom Library.\nPress 3, If you want to exit the Library.\n")
            try:
                b = int(input("Enter the number :"))
            except:
                print("Invalid Input!")
            if b == 1:
                check = student.getdetails()
                continue
            elif b == 2:
                student.AddStudent()
                continue
            elif b == 3:
                print(f"Thank you {name1}, for visiting the Custom Librabry.Have a good day!")
                break
            else:
                print("Number must be between 1 to 3")