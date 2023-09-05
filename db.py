import sqlite3
import bcrypt

def getAvailableBooks():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Query for all available books
        cursor.execute("Select * from books where isBorrow=0")
        print(cursor.fetchall())
        
        conn.commit()
        conn.close()
        return [True]

    except Exception as e:
        print(e)
        return [False,e]
        
def AddBook(name,price):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Create table if not exists
        cursor.execute("""Create table if not exists books
                    (name text,
                    costPerDay INTEGER,
                    isBorrow NUMBER(1))""")
        
        #Enter values into table
        cursor.execute("insert into books(name,costPerDay,isBorrow) values (?,?,?)",(name,price,0))

        conn.commit()
        conn.close()
        return [True]

    except Exception as e:
        print(e)
        return [False,e]
        
def AddUser(name,Pass,email):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Create table if not exists
        cursor.execute("""Create table if not exists users
                    (name text,
                    Pass text,
                    email text)""")
        
        hashed = bcrypt.hashpw(Pass,bcrypt.gensalt())
        
        #Enter values into table
        cursor.execute("""insert into users values (?,?,?)""",(name,hashed,email,))

        conn.commit()
        conn.close()
        return [True]
        
    except Exception as e:
        print(e)
        
        return [False,e]
        
def RemoveUser(name):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Enter values into table
        cursor.execute("delete from users where name=(?)",(name,))

        conn.commit()
        conn.close()
        return [True]

    except Exception as e:
        print(e)
        return [False,e]

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
            conn.commit()
            conn.close()
            return [True]
        else:
            conn.commit()
            conn.close()
            return [False,"There is no book available which you want"]
            
    except Exception as e:
        conn.commit()
        conn.close()
        return [False,e]


def getBorrowedBooks(name):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Query for all available books
        cursor.execute("Select book_name from borrow_books where user_name = (?)",(name,))
        print(cursor.fetchall())
        conn.commit()
        conn.close()
        return [True]

    except Exception as e:
        conn.commit()
        conn.close()
        return [False,e]

def checkUser(name,Pass):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute("select Pass from users where name = (?)",(name,))
        val = cursor.fetchone()
        if val == []:
            conn.commit()
            conn.close()
            return [False,"Username does not exist!"]
        else:
            val = val[0]

            conn.commit()
            conn.close()

            if bcrypt.checkpw(Pass,val):
                return [True]
            else:
                return [False,"Password does not match!"]

    except Exception as e:
        print(e)
        return [False,e]
        
def ReturnBook(uname,bname):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        #Enter values into table if book is availbale
        cursor.execute("select rowid from borrow_books where book_name=(?) and user_name=(?)",(bname,uname,))
        temp = cursor.fetchall()
        num = temp[0]
        
        if num != []:
            #Mark borrowed false for books in library
            cursor.execute("select book_name from borrow_books where rowid=(?)",(num)) 
            temp = cursor.fetchall()
            
            num1 = temp[0]
            cursor.execute("update books set isBorrow=0 where name = (?)",(num1)) 
            cursor.execute("delete from borrow_books where rowid =(?)",(num)) #Mark borrowed false for books in library
            
            conn.commit()
            conn.close()
            return [True]
        else:
            conn.commit()
            conn.close()
            return [False,"you cannot return the book you have not borrowed!"]
    
    except Exception as e:
        return [False,e]
    