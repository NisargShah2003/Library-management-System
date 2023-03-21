from datetime import datetime 
class success:
    @staticmethod
    def time():
        """Returns the current time in string format"""

        now = datetime.now()
        current_time = now.strftime("%d/%m/%y %H:%M:%S")

        return current_time
    
    def logged_out(name):
        """Entry in record file when user logs out"""

        with open("Records.txt",'a') as f:
                f.write(f"{success.time()} : {name} have logged out.\n")

    def logged_in(name):
        """Entry in record file when user logs in"""

        with open("Records.txt",'a') as f:
                f.write(f"{success.time()} : {name} have logged in.\n")

    def getAvailableBooks(name):
        """Entry in record file when user gets the list of available books in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} have checked the list of availabled books.\n")

    def AddUser(name):
        """Entry in record file when new user is added into database"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} has been added as user.\n")

    def RemoveUser(name):
        """Entry in record file when user is been removed from the database"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} has been removed from user.\n")

    def AddBook(name,price):
        """Entry in record file when new book is added into database"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} book has been added with price as {price}.\n")

    def BorrowBook(uname,bname):
        """Entry in record file when user borrows book in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {uname} have borrowed {bname}.\n")

    def ReturnBook(uname,bname):
        """Entry in record file when user returns book in library"""
        
        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {uname} have returned the borrowed {bname} book.\n")

    def getBorrowedBooks(uname):
        """Entry in record file when user gets the list of borrowed books in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {uname} have checked the borrowed books.\n")



"""Failed Operations"""
class failed:
    def logged_out(name,error):
        """Entry in record file when user fails to logs out"""

        with open("Records.txt",'a') as f:
                f.write(f"{success.time()} : {name} have failed to logged out due to {error}.\n")

    def logged_in(name,error):
        """Entry in record file when user fails to logs in"""

        with open("Records.txt",'a') as f:
                f.write(f"{success.time()} : {name} have failed to logged in due to {error}.\n")

    def getAvailableBooks(name,error):
        """Entry in record file when user fails to get the list of available books in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} have failed to check the list of availabled books due to {error}.\n")

    def AddUser(name,error):
        """Entry in record file when new user is failed to add into database"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} has been failed to add user due to {error}.\n")

    def RemoveUser(name,error):
        """Entry in record file when user has been fail to remove from the database"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} has been failed to removed user due to {error}.\n")

    def AddBook(name,error):
        """Entry in record file when new book is fail to add into database"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {name} book has failed to add due to {error}.\n")

    def BorrowBook(uname,bname,error):
        """Entry in record file when user fails to borrow book from library"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {uname} have been failed to borrow {bname} due to {error}.\n")

    def ReturnBook(uname,bname,error):
        """Entry in record file when user fails to return book to library"""
        
        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {uname} have been failed to return the borrowed {bname} book due to {error}.\n")

    def getBorrowedBooks(uname,error):
        """Entry in record file when user fails to get the list of borrowed books in library"""

        with open("Records.txt",'a') as f:
            f.write(f"{success.time()} : {uname} have been failed to check the borrowed books due to {error}.\n")