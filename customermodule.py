import mysql.connector
from tabulate import *
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()


def Customer():
    L=[]
    name=input("Enter the Customer Name: ")
    L.append(name)
    cphone=int(input("Enter customer phone number: "))
    L.append(cphone)
    payment=int(input("Enter payment method ((1) credit card/(2) Debit Card/(3) Cash): "))
    L.append(payment)
    email=input("Enter the email id: ")
    L.append(email)
    date=input("Enter the Date: ")
    L.append(date)
    cust=(L)
    sql="insert into customer (name,cphone,paymenttype,email,date) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()
    sql2 = 'select * from customer where c_id=(SELECT LAST_INSERT_ID())'
    mycursor.execute(sql2)
    print('Details:', mycursor.fetchall())
    


    
