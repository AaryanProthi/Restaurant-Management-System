import mysql.connector
from tabulate import *
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()

def View():
    print("Select the search criteria : ") 
    print("1. Employee")
    print("2. Customer")
    print("3. Food")
    ch=int(input("Enter the choice 1 to 3 : "))

    if ch==1:
        s=int(input("enter Employee ID:"))
        rl=(s,)
        sql="select * from Employee where Emp_id=%s" 
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        print(tabulate(res, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))
        if not res:
            print('no employee found')

    elif ch==2:
        s=int(input("Enter Customer id : "))
        rl=(s,)
        sql="select * from customer where c_id=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        print(tabulate(res, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))
        if not res:
            print('no customer found')

    elif ch==3:
        sql1="select * from Food"
        mycursor.execute(sql1)
        res1=mycursor.fetchall()
        print(tabulate(res1, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))
        
        
        s=int(input("Enter Food id : "))
        a=(s,)
        sql="select * from Food where Food_id=%s"
        mycursor.execute(sql,a)
        res2=mycursor.fetchall()
        print(tabulate(res2, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))
        if not res2:
            print('no food item found')




