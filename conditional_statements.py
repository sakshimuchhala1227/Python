name="sam"
print(name.capitalize())
sent="my house\\is in indore"
print(sent)

# conditional statements
i=int(input("number is :"))
if(i>15):
    print("number is greater than 15")
elif(i==15):
    print("number is equal to  15")
else:
    print("number is less than 15")

    # programm to compare share prices of two firms
p1,p2=eval(input("enter the share prices"))
if(p1>p2):
    print("the first firm is performing better")
else:
     print("the second firm is performing better")

sales=float(input("input the sales amount"))
expenses=float(input("input the sales amount"))
profit=sales-expenses
if profit>9000:
    print('''good profit
    congratulations''')
else:
    print('''poor profit
     work hard''')

# nested if
pro1,pro2,pro3=eval(input("the prices of three products are"))
if(pro1>pro2):
    if(pro1>pro3):
        print("first product is expensive")
    else:
        print("third product is expensive")
else:
    if(pro2>pro3):
        print("second product is expensive")
    else:
         print("third product is expensive")

std1, std2=eval(input("enter the name of students "))
if std1=="sakshi":
    print("enrollment number is 35")
else:
    print("enrollment number is 24")

x=int(input("enter the value of x:"))
if x>50:
    print("false,statement skipped")
elif x>20:
    print("true,block executed")
elif x>10:
    print("true,but block will not executed")
else:
    print("if all fails")

y=int(input("enter the value of x:"))
if y>900:
    print("excellence performance")
elif y>600:
    print("average performance")
elif y>200:
    print("below average")
else:
    print("poor")

salary=eval(input("input the salary"))
if salary<=0|salary>=300000:
    print("invalid salary")
if salary<50000&salary>0:
    print("junior manager")
if salary>100000&salary<300000:
    print("senior manager")

salary=eval(input("input the salary"))
if salary<0:
    print("invalid salary")
# elif salary>0:
#     print("junior level manager")
elif salary>50000:
    print("middle level manager")
elif salary>100000:
    print("senior level manager")