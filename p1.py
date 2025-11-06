#area of circle
import math
area=int(input("enter the radius:"))
a=math.pi*area**2
print("area=",a)

 #       OR
area=int(input("enter the radius:"))
a=3.14*area**2
print("area=",a)


#using if else positive or negative
a=int(input("enter the number:"))
if a>0:
    print(a,"is a positive  umber")
else:
    print(a,"is a negative number")

a=int(input("enter the number:"))
if a>0:
     print(a,"is a positive  umber")
elif a<0:
     print(a,"is a negative number")
else:
     print("user entered zero.")

#even or odd using if else
a=int(input("enter the number:"))
if a%2==0:
    print(a,"is a even number.")
elif a%2!=0:
    print(a,"is odd")
else:
    print("user entered zero")

a=int(input("enter the number:"))
if a==0:
    print("user entered zero")
elif a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")

#square and cube
a=int(input("enter the number:"))
print("the square of number is:",a**2)
print("cube of number is :",a**3)

#                                  print the result
a=int(input("enter the marks:"))
if a>=60:
     print("you have scored first class")
elif a>=45:
     print("you have scored second class:")
elif a>=35:
     print("you have passed the exam")
else:
     print("you have failed!!")



#                               looping syntax
for a  in range (1,5):
    print("hello----->",a)

fruits=["apple","orange","cherry"]
for i in fruits:
    print(i)


s=["bob","jhon","oggy","jack"]
for n in s:
    print(n,"is present at the event!!!")

t=["wake up","exercise","study","reading book","sleep"]
for n in t:
    print(n,"is my daily routine")

s=["milk","Bread","Rice","eggs"]
for n in s:
    print(n,"is in cart")




#                       multiplication table 
a = int(input("Enter the number to be multiplied: "))
for i in range(1, 11): 
    print(a, "x", i, "=", a * i)

 #                      printing total using for loop 







  #                             fibonecci series

a = int(input("Enter the elements: "))
t1 = 0
t2 = 1
print("Fibonacci series:")
for i in range(a):
    print(t1)
    fibo = t1 + t2
    t1 = t2
    t2 = fibo
print("The last Fibonacci number is:", t1)



   #                             square pattern
a=int(input("enter the number:"))
for i in range(a):
    for j in range(a):
      print("*",end="")
    print()


    #                           triangle pattern  left
b=int(input("enter the number:"))
for i in range(b+1):
   print("*"*i)
  
     #                           swapping of numbers 
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("before",a,b)
temp=a
a=b
b=temp
print("after",a,b)
     

      #                                 triangle right
b=int(input("enter the number:"))
for i in range(b+1):
   print("" * (b-i) + "*"*i)


       #                                 triangle revers
b=int(input("enter the number:"))
for i in range(b):
    for j in range(b-i):
      print("*",end="")
    print()

b=int(input("enter the number:"))
for i in range(b):
     for j in range(b):
       if j < b - i - 1:
            print(" ", end="")   
       else:
            print("*",end="")
     print()



#                                     match variable
d=int(input("enter the day:"))
match d:
    case 1:
       print("sunday")
    case 2:
       print("monday")
    case 3:
       print("tuesday")
    case 4:
       print("wednesday")
    case 5:
       print("thursday")
    case 6:
       print("friday")
    case 7:
       print("sunday")
    


d=int(input("enter the day:"))
match d:
    case 1:
       print("sunday 💕")
    case 2:
       print("monday 😒")
    case 3:
       print("tuesday 😢")
    case 4:
       print("wednesday 🙄")
    case 5:
       print("thursday 🙂")
    case 6:
       print("friday 😍")
    case 7:
       print("sunday ❤️")


d=int(input("enter your favourite food "))
match d:
    case 1:
       print("coffee☕")
    case 2:
       print("pizza 🍕")
    case 3:
       print("ice cream 🍦")
    case 4:
       print("cake 🍰")
    case 5:
       print("meals 🍴")



                              #LISTS
#append method
fruits=["strawberry","apple"]
fruits.append("cherry")
print(fruits)

#insert method in 4th position print 5
f=[1,2,3,4,6]
f.insert(4,5)
print(f)

#extend extended by using another list and values to extended
k=[1,2,3,4,5]
k.extend([0,6])
print(k)

#remove removed by using elements 
k=[1,2,3,4,5]
k.remove(4)
print(k)

#pop  removed by using  index values 
k=[1,2,3,4,5]
k.pop(1)
print(k)

#clear clears everything inside the list and displayes empty list
k=[1,2,3,4,5]
k.clear()
print(k)

#sorting 
k=[1,4,8,5,2,9]
k.sort()
print(k)

l=["apple","1","APPLE","banana","BANANA"]
l.sort()
print(l)


#reverse 
n=[1,2,3,4]
n.reverse()
print(n)


#index  shows the index value 
f=[1,2,3,4,5,6,7,8]
print(f.index(8))

#count it shows the number of times elements is repeted 
f=[1,2,3,4,5,5,6,3,6,7,8,6]
print(f.count(6))


            #question:create a list and add mango at end and orange at index 1

f=["apple","cherry","banana"]
print(f)
f.append("mango")
f.insert(1,"orange")
print(f)
             #take the list of colors and remove(green) and pop last element
c=["red","blue","green","yello"]
print(c)
c.pop(3)
print(c)
c.remove("green")
print(c)

              # you are going shopping start with a list of milk bread and eggs 
              # butter and jam to the list remove bread from the list 
s=["milk 🥛","bread 🍞","eggs 🥚"]
print(s)
s.append("jam ")
s.append("butter 🧈")
print(s)
s.remove("bread 🍞")
print(s)
s.sort()
print(s)


                                                    # TUPLES
#methods of tuples
m=(10,20,30,40)
print(len(m))
print(min(m))
print(max(m))
print(sum(m))
print( 30 in m)
print(m[1:3])

                                                    #  SETS
f={"apple","banana","cheer"}
f.add("mango")
f.add("apple")
print(f)