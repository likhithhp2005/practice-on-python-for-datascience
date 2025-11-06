import time
ct=time.ctime()
print("current time",ct)
                                         #SLEEP MODE
import time
print("hi i am sleeping")
time.sleep(4)
print("now i woke up")

                                    #PRINTING LOCAL TIME AND DATE 

import time
ctime=time.localtime()
print("full date and time:",time.strftime("%Y-%m-%d  %H:%M:%S",ctime))
print("only date: ",time.strftime("%d/%m/%Y",ctime))
print("only time :",time.strftime("%I:%M:%p",ctime))
print("day name :",time.strftime("%A",ctime))


import random
print(random.randint(1,7))

f=["mango","apple","cheery","blueberry","drangonfruit"]
print(random.choice(f))
 
                                     # PRINTING PARTICULAR MOTH OF THE YEAR

import calendar
#print(calendar.month(year,))
 
                                         #PRINTING CALENDAR OF THE YEAR

import calendar
year=int(input("enter the year:"))
print(calendar.calendar(year))

                                        # PRINTING PARTICULAR DATE DAY TIME
import calendar
d=int(input("enter the day:"))
m=int(input("enter the month:"))
y=int(input("enter the year:"))
daynumber=calendar.weekday(y,m,d)
day_name=calendar.day_name[daynumber]
print(f"the day on {d}/{m}/{y} is {day_name}")

                                                  # RANDOM WINNERS
import random
s=["ravi","anu",'kiran',"priya","vishal","meena","arjun","sita","rahlu"]
random.shuffle(s)
print("shuffled lis:",s)
w=random.sample(s,3)
print("the winners are:",w)    

                                                     #IMPORTING MATH
import math
print(math.sin(90))
print(math.sqrt(9))
                                       
                                                        #OOPS
                                                        #CALSS

class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color


my_car=car("toyota","red")
print("the brand of the car is ",my_car.brand)
print("the color of the car is ",my_car.color)

                                                  #DEPOSIT AND WITHDRAWAL 
class bank_account:
    def __init__(self):
        self.balance=0
        print("Hello!! Welcome to the deposit and withdraw machine")

    def deposit(self):
        amount=float(input("enter the amount to be DEPOSITTED:"))
        self.balance += amount
        print("\n Amount depositted!!",amount)
    
    def withdraw(self):
        amount =float(input("enter the amount to be withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("amount has been withdrew!",amount)
        else:print("\n Insufficient balance!")

    def display(self):
        print("\n Net avaliable balance is :",self.balance)   
        
s=bank_account()
s.deposit()
s.withdraw()
s.display()




                       