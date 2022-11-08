import random
import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()



def Food():
    L=[]
    Foodname=input("Enter the Food Name: ")
    L.append(Foodname)
    price=int(input("Enter Price of Food: "))
    L.append(price)
    Food=(L)
    sql="insert into Food (Foodname,price ) values (%s,%s)"
    mycursor.execute(sql,Food)
    mydb.commit()


 
