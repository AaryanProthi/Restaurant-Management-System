import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()


def Employee():
    L=[]
    ename=input("Enter the Employee Name: ")
    L.append(ename)
    emp_g=input("Enter Employee Gender : ")
    L.append(emp_g)
    eage=int(input("Enter Employee age: "))
    if eage<18:
        print('age invalid')
        while eage<18:
            eage=int(input("Enter Employee age: "))
    else:
        L.append(eage)

    emp_phone=int(input("enter employee phone number: "))
    L.append(emp_phone)
    pwd=input("Enter the password : ")
    L.append(pwd)
    EMP=(L)
    sql="insert into Employee (ename,emp_g,eage,emp_phone,pwd) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,EMP)
    mydb.commit()
    
    
    

