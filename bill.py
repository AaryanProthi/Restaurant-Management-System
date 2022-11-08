import mysql.connector
from tabulate import *
import random
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()

def billgenerator():
    s = 0
    Orderfid = random.randint(1,(2**63)-1)
    cid = int(input('enter customer id for bill:'))
    empid = int(input('enter employee id for bill:'))
    date = input('enter date of order:')
    mycursor.execute('select * from food')
    result = mycursor.fetchall()
    print(tabulate(result, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))
    l = []
    ch = 'y'
    while True:
        order = input("enter food item to be ordered: ")
        q = int(input("enter quantity: "))
        q1 = q
        if order.lower() == "coffee":
            q1 *= 40
            b = q1
            s += q1
            a = ['  ' + order + '  ', q, b]
            l.append(a)
            list = [Orderfid, 'coffee('+str(q)+')']
            val = (list)
            sql = 'insert into bill values(%s, %s)'
            mycursor.execute(sql, list)
            mydb.commit()
            
    
        elif order.lower() == "dal makhani":
            q1 *= 300
            b = q1
            s += q1
            a = ['' + order + '', q, b]
            l.append(a)
            list = [Orderfid, 'dal makhani('+str(q)+')']
            val = (list)
            sql = 'insert into bill values(%s, %s)'
            mycursor.execute(sql, val)
            mydb.commit()

        elif order.lower() == "tea":
            q1 *= 30
            b = q1
            s += q1
            a = ['   ' + order + '    ', q, b]
            l.append(a)
            list = [Orderfid, 'tea('+str(q)+')']
            val = (list)
            sql = 'insert into bill values(%s, %s)'
            mycursor.execute(sql, val)
            mydb.commit()
            
        elif order.lower()=="chicken tikka":
            q1*=250
            b = q1
            s += q1
            a = [order, q, b]
            l.append(a)
            list = [Orderfid, 'chicken tikka('+str(q)+')']
            val = (list)
            sql = 'insert into bill values(%s, %s)'
            mycursor.execute(sql, val)
            mydb.commit()

        elif order.lower()=="paneer tikka":
            q1*=220
            b = q1
            s += q1
            a = [order, q, b]
            l.append(a)
            list = [Orderfid, 'paneer tikka('+str(q)+')']
            val = (list)
            sql = 'insert into bill values(%s, %s)'
            mycursor.execute(sql, val)
            mydb.commit()

        else:
            print("entered wrong food item")
    
    
        ch = input("do you want to order more food: y/Y=yes, n/N=no - ")
        if ch.lower() == "n" or ch.lower() == 'no':
            break

    print('customer id:', cid)
    print('employee id:', empid)
    print('date:', date)
    print('    order id      ', '        food items     ') 
    sql2 = 'select orderid, group_concat(fooditem) from bill group by orderid having orderid=%s'
    val2 = (Orderfid,)
    mycursor.execute(sql2, val2)
    result = mycursor.fetchall()
    print(result)

    sql3 = 'insert into orderfood values(%s, %s, %s, %s, %s)'
    val3 = (Orderfid, s, date, cid, empid)
    mycursor.execute(sql3, val3)
    mydb.commit()

    print('total bill is:', s)


         
            
        
            
        
            