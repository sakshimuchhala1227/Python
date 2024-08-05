# operators (programm to show the usage of arithmetic operators)
num1=int(input("enter first number "))
num2=int(input("enter second number "))
#adding two numbers
print(num1,"+",num2 ,"=", num1+num2) 

#substract two numbers
print(num1,"-",num2 ,"=", num1-num2) 

#multiplication two numbers
print(num1,"x",num2 ,"=", num1*num2)

#modulas two numbers
print(num1,"%",num2 ,"=", num1%num2)

#pow two numbers
print(num1,"^",num2 ,"=", num1**num2)

#quotient12 two numbers
print(num1,"//",num2 ,"=", num1//num2)

#relational operators
num1,num2=3,4
#== checks if the value of the two operants are equal or not
print("the result of == is ",num1==num2)
print("the result of not equal to operator ",num1!=num2)
print("num1>num2 ",num1>num2)
print("num1>=num2 ",num1>=num2)
print("num1<num2 ",num1<num2)
print("num1<=num2 ",num1<=num2)

#add AND operator  y+=x same as y=y+x
num5=int(input('enter first number:'))
num6=int(input("enter second number:"))
result=num6
result+=num5
print("the resukt of addition is:",result)

num5=int(input('enter first number:'))
num6=int(input("enter second number:"))
result=num6
result*=num5
print("the result of multiplication is:",result)

#the equals operator check if the values of two operants are equal
#relational operator
num7=46
num8=34
print("the result of equals to operator is :",num7==num8)

# programm to showlogical operators
r,s,t=33,45,89
#use of AND logical operator
print("the use of and operator",r>s and s>t)
print("the use of and operator",r<s or s>t)
print("the use of and operator",not s>t)

#program to show the use of logical operators or boolean 
var_1=True
var_2=False
print("use of and operator returns: ",var_1 and var_2)
print("use of and operator returns: ",var_1 or var_2)
print("use of and operator returns: ",var_1 and var_1)

#operator precedence
#operator                                details
#  ()                               pharanthesis
#  **                                exponential(power)
#  /,*,//,%                         div,mult,interal,remainder
#   +,-                              add,sub
#  >,<,>=,<=,!=,==                    relational
#  =,+=,-=,*=,**=,/=,//=             assignment operators
# not or and                         logical boolean operators

#program to show the precedence of operators
p=2
q=5
r=10
print("pharenthesis has highest precedence",(p+q)*(q+r))
print("pharenthesis has highest precedence",(p+q)*r)
print("relational has highest precedence",p>q and q>r)