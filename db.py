import sqlite3

def getAvailableBooks():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Query for all available books
        cursor.execute("Select * from books where isBorrow=0")
        print(cursor.fetchall())
        
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
        
def AddBook(name,price):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        # cursor.execute("""drop table books""")
        
        #Create table if not exists
        cursor.execute("""Create table if not exists books
                    (name text,
                    price INTEGER,
                    isBorrow NUMBER(1))""")
        
        #Enter values into table
        cursor.execute("insert into books(name,price,isBorrow) values (?,?,?)",(name,price,0))

        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
        
def AddUser(name,Pass,email):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Create table if not exists
        cursor.execute("""Create table if not exists users
                    (name text,
                    Pass text,
                    email text)""")
        
        #Enter values into table
        cursor.execute("""insert into users values (?,?,?)""",(name,Pass,email,))

        conn.commit()
        conn.close()
        
    except Exception as e:
        print(e)
        
def RemoveUser(name):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Enter values into table
        cursor.execute("delete from users where name=(?)",(name,))

        conn.commit()
        conn.close()
        
    except Exception as e:
        print(e)

def BorrowBook(uname,bname):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Create table for borrowed books
        cursor.execute("""Create table if not exists borrow_books
                (user_name text,
                book_name text)""")
        
        #Enter values into table if book is availbale
        cursor.execute("select rowid from books where isBorrow=False and name=(?)",(bname,))
        num = cursor.fetchone()
        
        if num != []:
            val = num[0]
            cursor.execute("""insert into borrow_books(user_name,book_name) values (?,?)""",(uname,bname,)) #add into borrowed list
            cursor.execute("update books set isBorrow=1 where rowid = (?)",(val,)) #Mark borrowed true for books in library
            print("The book has been added successfully!")
        else:
            print("The requested book is not available")
            print()
            print("Here are the available books:")
            getAvailableBooks()

        conn.commit()
        conn.close()

    except Exception as e:
        print(e)


def getBorrowedBooks(name):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Query for all available books
        cursor.execute("Select book_name from borrow_books where user_name = (?)",(name,))
        print(cursor.fetchall())
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)

def checkUser(name,Pass):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute("select Pass from users where name = (?)",(name,))
        val = cursor.fetchall()[0][0]
        print(val)

        conn.commit()
        conn.close()
        
        if val == (Pass):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        
def ReturnBook(uname,bname):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Enter values into table if book is availbale
        cursor.execute("select rowid from borrow_books where book_name=(?) and user_name=(?)",(bname,uname,))
        temp = cursor.fetchall()
        num = temp[0]
        print(num)
        
        if num != []:
            #Mark borrowed false for books in library
            cursor.execute("select book_name from borrow_books where rowid=(?)",(num)) 
            temp = cursor.fetchall()
            print("temp:",temp)
            num1 = temp[0]
            cursor.execute("update books set isBorrow=0 where name = (?)",(num1)) 
            cursor.execute("delete from borrow_books where rowid =(?)",(num)) #Mark borrowed false for books in library
            
        else:
            print("you cannot return the book you have not borrowed!")
            print()
            print("Here is the list of borrowed books:")
            getBorrowedBooks(uname)

        conn.commit()
        conn.close()

    except Exception as e:
        print(e)