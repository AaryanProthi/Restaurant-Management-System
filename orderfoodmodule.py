import mysql.connector
import random
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()

def OrderFood():
    L=[]
    OrderF_id=random.randint(1,(2**63)-1)
    L.append(OrderF_id)
    Total_price=input("Enter total price: ")
    L.append(Total_price)
    date = input('enter date: ')
    L.append(date)
    C_id=input("Enter the customer id: ")
    L.append(C_id)
    Emp_id=input("Enter employee id: ")
    L.append(Emp_id)
    OrderFood=(L)
    sql="insert into orderfood values (%s, %s, %s, %s, %s)"
    mycursor.execute(sql,OrderFood)
    mydb.commit()



