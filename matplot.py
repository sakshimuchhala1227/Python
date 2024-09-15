import matplotlib.pyplot as plt
plt.plot([16,12,11,10,12,8,4,17,9,11,15,14,13])
plt.ylabel("random numbers")
plt.show()

import matplotlib.style
matplotlib.style.use('ggplot')
plt.plot([16,12,11,10,12,8,4,17,9,11,15,14,13])
plt.ylabel("random numbers")
plt.xlabel("numbers")
plt.show()

# programm for creating line chart with grids and special effects
plt.plot([7,5,8,11,13,9,11],[5,7,9,21,15,16,17],color='g',linewidth=5)
# plt.plot([1,2,3,4,5,6,7],[1,2,3,4,5,6,7],color='g',linewidth=5)
plt.title("chart with user defined color and width of line ")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True) #if we give false here then grid lines will not be shown
plt.text(5,12,'hello world ',color='brown') #it will print the text from 5 on x axis and from 12 on y axis and the colour is green
plt.show()

# program to draw dot and lines on the same chart with axes limit
plt.plot([6,9,7,11,13],[8,11,13,12,15],'ro',[6,9,7,11,13],[8,11,13,12,15],'m')# m is magenta colour ro is red dotted
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("dot and line chart together")
plt.axis([5,15,5,17]) #???
plt.grid(True)
plt.show()

# program to display multiple lines with different shapes and colors
a=list(range(1,11))
b=list(range(5,55,5))
c=list(range(10,110,10))
d=list(range(20,210,20))
print("first list ",a)
print("second list ",b)
print("third list ",c)
print("fourth list ",d)

#creating a chart with different colors and effects for different data
plt.plot(a,a,'g^',a,b,'bs',a,c,'r--',a,d,'mo')
plt.xlim(0,11)
plt.ylim(0,220)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("multiple lines with different shapes and colors")
plt.grid(True,color='k') # k means black colour 
plt.show()
 
# program for creating a pie chart
list1=[10,30,40,30,50,70,80,100,40,60]
plt.pie(list1, labels=list1)
plt.show()


ecom=['myntra','snapdeal','alibaba','amazon','flipkart']
q1_profit=[35,45,100,75,40]
q2_profit=[83,37,28,78,98]
q3_profit=[67,73,93,60,61]
q4_profit=[20,85,92,90,22]

plt.scatter(ecom,q1_profit,color='blue')
plt.scatter(ecom,q2_profit,color='purple')
plt.scatter(ecom,q3_profit,color='pink')
plt.scatter(ecom,q4_profit,color='yellow')
plt.plot(ecom,q1_profit,'ro',ecom,q1_profit,'m')
plt.show()

list1=[5,10,15,20,25]
list2=[10,20,30,40,50]
plt.hist2d(list1,list2)
plt.show()

#creating different barcharts using differnent function
ecom=['myntra','snapdeal','alibaba','amazon','flipkart']
q1_profit=[35,45,100,75,40]
q2_profit=[83,37,28,78,98]
q3_profit=[67,73,93,60,61]
q4_profit=[20,85,92,90,22]

# bar chart
plt.barh([2,3,4,5,6],width=[1,2,3,2,1])
plt.show()

plt.figure(1, figsize=(10,10))
#creating barchart in 1st cell of figure 
plt.subplot(221)    
plt.bar(ecom,q1_profit)
plt.title("quarter 1 pro")

plt.subplot(222)    
plt.bar(ecom,q2_profit)
plt.title("quarter 2 pro")

plt.subplot(223)    
plt.bar(ecom,q3_profit)
plt.title("quarter 3 pro")

plt.subplot(224)    
plt.bar(ecom,q4_profit)
plt.title("quarter 4 pro")
plt.show()

# program to craete a stacked bar chart
plt.figure(1, figsize=(15,10))
country=['A','B','C','D','E']
pop_1930=[10,20,30,40,50]
pop_1940=[11,45,87,35,26]
pop_1950=[17,46,27,38,84]
pop_1960=[76,48,29,94,39]
pop_1970=[69,90,35,62,77]
pop_1980=[22,66,44,88,77]
pop_1990=[87,45,76,45,86]
pop_2000=[54,37,92,63,38]
pop_2010=[64,82,90,40,22]
plt.bar(country,pop_2010,color='green')
plt.bar(country,pop_2000,color='red')
plt.bar(country,pop_1990,color='yellow')
plt.bar(country,pop_1980,color='orange')
plt.bar(country,pop_1970,color='blue')
plt.bar(country,pop_1960,color='brown')
plt.bar(country,pop_1950,color='purple')
plt.bar(country,pop_1940,color='pink')
plt.bar(country,pop_1930,color='magenta')
plt.xlabel("countries")
plt.ylabel("population and different years")
plt.title("stacked bar chart")
plt.show()

from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()

