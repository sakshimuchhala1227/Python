#data structures play an important role in programming the different data structures 
# included in python are array,list,tupple,dictionary. the difference btw an array and
# a list is that the array is the collection of similar data type where as a list can be 
# collection of different data types while array and list can be modified by adding
# deleting and modifying the existing elements . it is not possible to modify a tupple

# creating a list programm to add numner using list
print("please enter 5 decimal numbers")
total=0
finallist=[]
for i in range(0,5):
    value=float(input("enter no "+str(i+1)+":"))
    finallist+=[value]
    total+=value
print("the number entered are:")
for num in finallist:
       print(num,end="  ")
    
print()
print("sum of numbers is", total)
    
list1=list(range(12,19))
print("first list:\n",list1)

list2=list(range(-3,5))
print("secomd list\n:",list2)

list3=list(range(30,-10,-2))
print("third list\n",list3)

list4=list(range(0,300,50))
print("list fourth\n:",list4)

list5=list(range(0,11))
list6=list(range(11,21))
list7=list5+list6
print("the new list is:\n",list7)
print("the class of list7 is:",type(list7))

#programm for accessing numbers of list
list8=[15,-3,10,14,-55]
#using for loop to display all numbers of a list
for num in range(0,5):
    print("the ",num+1," number is :",list8[num])

#using for loop and negative indexing to display all numbers of list
print("......using negative indexing........")
for val in range(-1,-6,-1):
    print("the number is:",list8[val])

#programm for accessing elements of heterogeneous list
list9=[12.56,-345,["india","africa","uk","us"],"countries"]

#using for loop to display all the elements of the list
for val in range(0,4):
    print("the element ",val+1," is:",list9[val])

#accessing individualnitem of nested list
for x in range (0,4):
    print("list item are:",list9[2][x])

#programm for showing the use of list slicing
list10=[0,1,2,3,4,5,6,7,8,9]

#elements between the starting and ending index are displayed
print("elements from third index and before sixth index:",list10[3:6])

#an empty list is returned,if user enters a negative value for index
print("elements starting from negative index not shown:",list10[-4:2])

#the strat value default to 0 if the begin argumnet is missing
print("the list is:",list10[:4])

#if end value is missing it defaults to the length of the list
print("the list is :",list10[5:])

#end value graeter than length of list is consideres length of list
print("the list is :",list10[3:12])
#empty list will be printed coz we cann't went from 4 to 0
print("the list is :",list10[4:0])

#programm for modifying the existing list elements
list11=[100,200,300,400,500,600,700]
print("the original list is:\n",list11)
list11[1]=110
list11[4]=120
print("the new list after modification is:\n",list11)

list1=list(range(12,19))
print("first list is:\n",list1)

list2=list(range(-3,5))
print("second list:\n",list2)

list3=list(range(30,-10,-2))
print("third list is:\n",list3)

list4=[2,3,2,4,2,5,6,5,2,8,9]
print("max number of list4 ",max(list4))
print("min number of list4 ",min(list4))
print("length of list4 ",len(list4))
print("number of 2's in list ",list4.count(2))
print("first position of 5 in list4: ", list4.index(5))
list4.remove(4)
print("list after removing 4: \n ",list4)
list4.append(30)
print("add 30 to the list: \n", list4)
list4.insert(3,10)
print("insert 10 in the list :\n",list4)
print("last element of the list :\n",list4.pop())
print("third element of the list :\n",list4.pop(2))
list4.reverse()
print("reverse the list:\n",list4)
list4.sort()
print("sort the list:\n",list4)

list5=list4.copy()
list6=list([10,20,30,40])
list5.extend(list6)
print("extended list is:\n",list5)

#program for adding removing and modifying list items using slicing
list12=[[165,345],"java",12,13,13,"a"]
print("list12 is:\n",list12)

#replacing the desired list values
list12[2:4]=["mp","up","ap"]
print("list after replacing multiple elements is:\n",list12)

#insreting the multiple  items at 3rd index
list12[3:3]=[12,13,14]
print("list after replacing elements at index 3 with a list:\n",list12)

# #deleting some elements from list


#sort mult strings
namelist=[]
num=int(input("enter the numbers of countries:"))

#adding elements
for i in range(1,num+1):
    name=input("enter the name of countries:")
    namelist.append(name)

#sorting and displaying the new list outside the for loop
print(namelist)
namelist.sort()
print("the sorted order is:\n",','.join(namelist))