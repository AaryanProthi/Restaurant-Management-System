from foodmodule import *
from viewmodule import *
from employeemodule import *
from customermodule import *
from orderfoodmodule import *
from bill import *
import mysql.connector
from tabulate import *
import platform
import os
mydb=mysql.connector.connect(host='localhost', user='root', passwd='1337@aaryan', database='food')
mycursor=mydb.cursor()


def MenuSet():
    print("Enter 1 : Employee module")
    print("Enter 2 : Customer module")
    print("Enter 3 : Food module ")
    print("Enter 4 : To search the database")
    print("Enter 5 : To generate bill")
    print('Enter 6:  To view billed items')

    print()

    try:
        userInput = int(input("Please Select An Above Option: ")) 
    except ValueError:
        exit("\nHey! That's Not A Number") 
    else:
        print("\n")

    if (userInput==1):
        print("Enter 1 : To Add Employee")
        print("Enter 2 : To display all employees")
        print("Enter 3 : To update employee record")
        print("Enter 4 : To delete employee record")
        
        try:
            x = int(input("Please Select An Above Option: ")) 
        except ValueError:
            exit("\nHey! That's Not A Number") 
        else:
            print("\n")

        if x==1:
            Employee()
            print('Employee details added successfully')

        elif x==2:
            mycursor.execute('select * from employee')
            myresult = mycursor.fetchall()
            print(tabulate(myresult, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))


        elif x==3:
            while True:
                empid=int(input("enter employee id - "))
                ch=int(input("enter choice 1: employee name, 2: gender, 3: age, 4: phone number, 5: password - "))

                if ch==1:
                    n=input("enter new name - ")
                    s="update employee set ename=%s where Emp_id=%s;"
                    val = (n, empid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==2:
                    n=input("enter new gender - ")
                    s="update employee set emp_g=%s where Emp_id=%s;"
                    val = (n, empid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==3:
                    n=int(input("enter new age - "))
                    s="update employee set eage=%s where Emp_id=%s;"
                    val = (n, empid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==4:
                    n=int(input("enter new phone number - "))
                    s="update employee set emp_phone=%s where Emp_id=%s;"
                    val = (n, empid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==5:
                    n=input("enter new password - ")
                    s="update employee set pwd=%s where Emp_id=%s;"
                    val = (n, empid)
                    mycursor.execute(s, val)
                    mydb.commit()

                else:
                    print("entered wrong choice")

                a=input("do you want to update more data y: yes, n: no - ")
                if a.lower()=='n' or a.lower()=='no':
                    break

            s="select * from Employee where Emp_id=%s"
            val=[empid]
            print("updated employee details are:")
            mycursor.execute(s, val)
            res = mycursor.fetchall()
            print(res)

        elif x==4:
            while True:
                empid=int(input("enter employee id which is to be deleted - "))
                sql = 'delete from employee where Emp_id=%s'
                val = [empid]
                mycursor.execute(sql, val)
                mydb.commit()
                print('record deleted')

                a=input("do you want to delete more data y: yes, n: no - ")
                if a.lower()=='n' or a.lower()=='no':
                    break

        
    elif (userInput==2):
        print("Enter 1 : To Add Customers")
        print("Enter 2 : To display all customers")
        print("Enter 3 : To update customer record")
        print("Enter 4 : To delete customer record")

        try:
            x = int(input("Please Select An Above Option: ")) 
        except ValueError:
            exit("\nHey! That's Not A Number") 
        else:
            print("\n")

        if x==1:
            Customer()
            print('Customer details added succesfully')

        elif x==2:
            mycursor.execute('select * from customer')
            myresult = mycursor.fetchall()
            print(tabulate(myresult, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))

        elif (x==3):
            while True:
                cid=int(input("enter customer id to be updated: "))
                ch=int(input("enter choice 1: customer name, 2: phone number, 3: email id"))
                

                if ch==1:
                    n=input("enter new name: ")
                    s="update customer set name=%s where c_id=%s"
                    val = (n, cid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==2:
                    n=int(input("enter new phone number: "))
                    s=("update customer set cphone=%s where c_id=%s")
                    val = (n, cid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==3:
                    n=input("enter new email id: ")
                    s=("update customer set email=%s where c_id=%s")
                    val = (n, cid)
                    mycursor.execute(s, val)
                    mydb.commit()

                else:
                    print("entered wrong choice")
                
                a=input("do you want to update more data y: yes, n: no - ")
                if a.lower()=='n' or a.lower()=='no':
                    break
            
            s="select * from customer where c_id=%s"
            val = [cid]
            print("updated customer details are:")
            mycursor.execute(s, val)
            res = mycursor.fetchall()
            print(res)

        elif x==4:
            while True:
                cid=int(input("enter customer id which is to be deleted - "))
                sql = 'delete from customer where c_id=%s'
                val = [cid]
                mycursor.execute(sql, val)
                mydb.commit()
                print('record deleted')

                a=input("do you want to delete more data y: yes, n: no - ")
                if a.lower()=='n' or a.lower()=='no':
                    break
            

    elif (userInput==3):
        print('enter 1 for adding to food menu')
        print('enter 2 for adding food order details')
        print('enter 3 to view food menu')
        print('enter 4 to view food orders')
        print('enter 5 to update food menu')
        print('enter 6 to delete items from food menu')

        try:
            x = int(input("Please Select An Above Option: ")) 
        except ValueError:
            exit("\nHey! That's Not A Number") 
        else:
            print("\n")

        if x == 1:
            Food()
            print('Food details added successfully')
        elif x == 2:
            OrderFood()
            print('Food order added')
        elif x == 3:
            mycursor.execute('select * from food')
            myresult = mycursor.fetchall()
            print(tabulate(myresult, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))

        elif x == 4:
            mycursor.execute('select * from Orderfood')
            myresult = mycursor.fetchall()
            print(tabulate(myresult, headers = [i[0] for i in mycursor.description], tablefmt = 'psql'))

        elif x == 5:
            while True:
                foodid=int(input("enter food id - "))
                ch=int(input("enter choice 1: food name, 2: food price"))

                if ch==1:
                    n=input("enter new name - ")
                    s="update Food set Foodname=%s where Food_id=%s;"
                    val = (n, foodid)
                    mycursor.execute(s, val)
                    mydb.commit()

                elif ch==2:
                    n=int(input("enter new price - "))
                    s="update Food set price=%s where Food_id=%s;"
                    val = (n, foodid)
                    mycursor.execute(s, val)
                    mydb.commit()

                else:
                    print("entered wrong choice")

                a=input("do you want to update more data y: yes, n: no - ")
                if a.lower()=='n' or a.lower()=='no':
                    break

            s="select * from Food where Food_id=%s"
            val=[foodid]
            print("updated food details are:")
            mycursor.execute(s, val)
            res = mycursor.fetchall()
            print(res)

        elif x == 6:
            while True:
                fid=int(input("enter food id which is to be deleted - "))
                sql = 'delete from food where Food_id=%s'
                val = [fid]
                mycursor.execute(sql, val)
                mydb.commit()
                print('record deleted')

                a=input("do you want to delete more data y: yes, n: no - ")
                if a.lower()=='n' or a.lower()=='no':
                    break


    elif (userInput==4):
        View()


    elif userInput==5:
        billgenerator()


    elif userInput==6:
        Orderfid = int(input('enter orderid to be searched:'))
        sql = 'select group_concat(fooditem) from bill group by orderid having orderid=%s'
        val = (Orderfid,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers = ['food items'], tablefmt = 'psql'))

        print()

        sql2 = 'select Total_price, date, c_id, emp_id from orderfood where orderid=%s'
        mycursor.execute(sql2, val)
        myresult2 = mycursor.fetchall()
        print(tabulate(myresult2, headers = ['price', 'date', 'cid', 'empid'], tablefmt = 'psql'))


    else:
        print("Enter a valid choice...")

def RunAgain():
    RunAgn=input("\nwant to run again Y/N")
    while RunAgn.lower()=='y':
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
        RunAgn=input("\nwant to run again Y/N")
    else:
        print("Good Bye... HAVE A NICE DAY")


MenuSet()
RunAgain()
    



            
