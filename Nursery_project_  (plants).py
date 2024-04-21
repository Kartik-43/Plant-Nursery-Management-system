import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',password='kartik',database='nursery')
mycursor = mydb.cursor()
mycursor.execute('create table if not exists user_table(username varchar(25) primary key,password varchar(25)not null)')
print('===================welcome to nursery management system================')


def bin_nursery():
    import pickle
    d=['THIS WILL SHOW YOU ALL THE RECORD EARLIER ADDEDIN THE TABLE NURSERY CATEGORIZED BY THE ORDER:-',
       ('pid','pname','lifespan','price','ptype'),
       (1,'snake plant',15,300,'indoor'),
       (2,'money plant',10,250,'outdoor'),
       (3,'dahlia plant',5,150,'flowering'),
       (4,'areca palm',10,400,'indoor'),
       (5,'aloe vera',12,280,'outdoor')]

    f=open('bnursery.dat','wb')
    pickle.dump(d,f)
    print('binary file written')
    f.close()
bin_nursery()

print('THESE RECORDS ARE INSERTED IN THE FORM TABLE NURSERY BY ME:')


def binary_file3():
    import pickle
    f=open("bnursery.dat",'rb')
    x=pickle.load(f)
    f.close()

    print(x)


binary_file3()


def proj():
    import time
    print("\t\t\t",time.ctime())

    import mysql.connector as sql
    mydb = sql.connect(host='localhost', user='root', password='kartik', database='nursery')
    mycursor = mydb.cursor()
    mycursor.execute("show databses")
    for x in mycursor:
        print(x)

#INSERTIONS
    mycursor=mydb.cursor()

    mycursor.execute("create table login_id(user_id varchar(30),password varchar(30) primary key)")
    mycursor.execute("create table nursery(pid int primary key, pname varchar(30),lifespan integer,price integer,ptype varchar(30)")

    mycursor.execute("insert into nursery values(1,'snake plant',15,300,'indoor')")
    mycursor.execute("insert into nursery values(2,'money plant',10,250,'outdoor')")
    mycursor.execute("insert into nursery values(3,'dahlia plant',5,150,'flowering')")
    mycursor.execute("insert into nursery values(4,'areca palm',10,400,'indoor')")
    mycursor.execute("insert into nursery values(5,'aloe vera',12,280,'outdoor')")
    mydb.commit()
    print(mycursor.rowcount)
    print("record added in table")


def details():
    import mysql.connector as sql
    mydb=sql.connect(host='localhost',user='root',password='kartik',database='nursery')
    mycursor=mydb.cursor()
    mycursor.execute('select * from nursery')
    result=mycursor.fetchall()
    mydb.commit()
    for x in result:
        print("\n",x, "\n")


def delete():
    import mysql.connector as sql
    mydb=sql.connect(host='localhost',user='root',password='kartik',database='nursery')
    mycursor=mydb.cursor()
    a=input("\nenter the nuame of plant whose record should be deleted:")
    mycursor.execute("delete from nursery where name='" + a + "'")
    result=mycursor.fetchall()
    mydb.commit()
    for x in result:
        print(x)


def INCprice():
    import mysql.connector as sql
    mydb=sql.connect(host='localhost',user='root',password='kartik',database='nursery')
    mycursor=mydb.cursor()
    name=input("\nEnter the plant name: ")
    mycursor.execute("update nursery set price=price+price*5/100 where pname='" + name + "'")

    mydb.commit()


def UPDname():
    import mysql.connector as sql
    mydb=sql.connect(host='localhost',user='root',password='kartik',database='nursery')
    mycursor=mydb.cursor()
    name=input("\nenter old name:")
    nam=input("\nenter new name:")
    d=input("\nenter pid:")
    mycursor.execute("update nursery set pname='" + name + "' where pid='" + d + "'")

    mydb.commit()


def NOcount():
    import mysql.connector as sql
    mydb=sql.connect(host='localhost',user='root',password='kartik',database='nursery')
    mycursor=mydb.cursor()
    mycursor.execute("select count(distinct pname) from nursery")
    count=mycursor.fetchall()
    for x in count:
        print(" number of plants ", x)
    mydb.commit()


def SHOWprice():
    name=input("\nenter the plant name:")
    a="select price from nursery where pname='" + name + "'"
    mycursor.execute(a)
    price=mycursor.fetchall()
    for x in price:
        print( x, "is the current price of", name)
    mydb.commit()


def menu():
    print("     NURSERY MANAGEMENT      ")
    c=input("START THE PROGRAM (yes or no):")
    while(c=='yes'):
        print("TASK THAT THIS PROJECT CAN DO")
        print("1.Details of the nursery:")
        print("2.Delete nursery record:")
        print("3.Update price(5%):")
        print("4.Update the name of plant:")
        print("5.Know the number of plants:")
        print("6.Show the prices of plant:")
        print("7.Exit the code:")

        choice=int(input("enter the choice:"))
        if choice==1:
            details()
        elif choice==2:
            delete()
        elif choice==3:
            INCprice()
        elif choice==4:
            UPDname()
        elif choice==5:
            NOcount()
        elif choice==6:
            SHOWprice()
        elif choice==7:
            print("exiting the code")
            break


import datetime as dt
print(dt.datetime.now())
print("1.REGISTER")
print()
print("2.LOGIN")
print()

n=int(input('enter your choice='))
print()

if n==1:
    name=input('enter a username=')
    id=(input('enter id:'))
    print()
    password=(input('enter a 4 digit password ='))
    print()
    mycursor.execute("insert into login_id values('" + id + "','" + str(password) + "')")
    mydb.commit()
    print()
    print('user created succesfully')

if n==2:
    name=input('enter your username=')
    id=(input('enter id:'))
    print()
    password=(input('enter your 4 digit password='))
    mycursor.execute("select * from login_id")
    if mycursor.fetchall() is None:
        print()
        print('invalid username or password')
    else:
        print()
        menu()
