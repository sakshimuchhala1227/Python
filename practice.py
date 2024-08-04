print(5)
print("hello sakshi")
print("hello my\' name is \"sakshi muchhala\" i am a student")
print("sakshi","muchhala",8959,sep="@",end="hemlo ")
print("hey there ")
d=None
print(d,type(d))
c=1
while(c!=0):
    a=int(input("enter first number to perform the operations "))
    b=int(input("enter  second number to perform the operations "))
    choice=int(input("enter 1 for addition,2 for subtraction,3 for division,4 for multiplication,5 for modulus,6 for floor division:"))
    if(choice==1):
         print(a+b)
    if(choice==2):
        print(a-b)
    if(choice==3):
         print(a*b)
    if(choice==4):
        print(a/b)
    if(choice==5):
        print(a%b)
    if(choice==6):
        print(a//b)
    c=int(input("enter 1 to continue or 0 to exit"))

print("programm ends")n/ n/ 
    
h='''hello mu  maeb  ddbddc snv'''
print(h)
for cha in h:
    print(cha)
name="hattu"    
print(name[-4:-2])
a="!!sakshi muchhala!!!  mtech"
print(a.upper())            
print(a.lower())    
print(a.capitalize())
print(a.replace("much","saks"))
print(a.rstrip("!"))
print(a.split(" "))
print(a.count("!"))
print(a.endswith("mtech"))
print(a.endswith("much",5,16))
print(a.find("shi"))
print(a.find("mmshi"))#it will return -1
print(a.index("hhal"))
# isalnum( )return true if their is  alpha numeric character their in the string like A-Z a-z 0=9
b="heytheiriamsakshi9"
b="heytheiriam sakshi 9"#it will retun false cause their is space in between
print(b.isalnum())
# similarly isalpha() only for alphabets 
c="iamsakshi"
print(c.isalpha())
print(c.islower())
d="hello i am sakshi"
e="hello i am sakshi\n"
print(d.isprintable())
print(e.isprintable())
d="  "
print(d.isspace())#return true if only whitespace is their
e="Hello World "
print(e.istitle())#return true when all the 1st letters are capital 
print(e.startswith("Hel"))
print(e.swapcase())#convert upper case in lower case and vice versa
f="my name is sakshi muchhala"
print(f.title())


#like switch case their is match case in python
c=int(input("enter the value 1 ,2,3 "))
match c:
    case 1:
        print("1 is printed")
    case 2:
        print("2 is printed")
    case 3:
        print("3 is printed")
    case _ if(c>10):
        print("number is greater than 10")
    case _:
        print("multiple default case can be used ")
