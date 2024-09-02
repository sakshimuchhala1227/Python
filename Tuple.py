#tuple
tup=tuple((22,46,24,5,24.4))
print("length of tuple:",len(tup))
print(tup.count(22))
print(sorted(tup))
print(max(tup))
print(sum(tup))
print(tup[1:4])
print("some more functions in tuple")
print(tup[:4])
print(tup[4:])
print(tup[:])
print(tup[::2])
print(tup[-4:-1])

mytuple1=()
print(type(mytuple1))
print("empty tuple is:",mytuple1)

#creating tuple with single element
mytuple2=(400,)
print("tuple with single elements is:",mytuple2)

mytuple3=tuple(range(5,60,10))
print(mytuple3)

#tuple from list
mylist_1=[10,4,67,3,55,40]
mytuple4=tuple(mylist_1)
print(mytuple4)

#tuple concatenation
mytuple5=(10,20,30)
mytuple6=mytuple4+mytuple5
print("sixth tuple after concatenation is",mytuple6)

# accessing tuple elements
mytuple7=(-7.14,34,"india","USA",("java","python"),"russia")
#use for to display first four elements of tuple
for val in range(0,5):
    print("the tuple element ",val+1," is:",mytuple7[val])

#accessing individual item of nested tuple
print("the first element of nested tuple:",mytuple7[4][0])
print("the first element of nested tuple:",mytuple7[4][1])

print("the elements second and before fourth of nested tuple:",mytuple7[1:3])

#program for repetation and determining existence in tuple
tuple8=(22,34,1,24,56,43.3)
print("repeat tuple\n",tuple8*2)
newtuple=tuple8*2
print("newtuple\n",newtuple)
print("22 in tuple",22 in tuple8)

# prog to determine the minimum element of tuple
tuple9=(10,20,30,40,50,1,3,5,8,96)
min=tuple9[0]
for i in range(len(tuple9)):
    if tuple9[i]<min:
        min=tuple9[i]

print("the min element is:",min)