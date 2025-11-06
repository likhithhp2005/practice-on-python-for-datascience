                                           #CREATING A DICTIONARY
                                        #COMMON DICTIONARY METHODS
#claear  claears the dictionary
s={"name":"jhon","age":20,"country":"USA"}
s.clear()
print(s)
print(type(s))  #if elements are there then it is set ortherwise it willbe dictionary

#copy()  it copies the data from one dict to another 
s={"name":"jhon","age":20,"country":"USA"}
print(type(s))
n=s.copy()
print(n)
print(type(n))

#get () it gets the specified element if the element is not there it prints the default value we have to give the default value in prior 
s={"name":"jhon","age":20,"country":"USA"}
print(s.get("age","XYZ"))
print(s.get("course","xyz"))

#items shows all the data in the set
s={"name":"jhon","age":20,"country":"USA"}
print(s.items())
print(s.keys())
print(s.values())

                                                 # EXAMPLE 1
s={"Name":"Ravi","Age":21,"course":"BBA"}
print("keys are :",s.keys())
print("values are :",s.values())
print("items are :",s.items())
print("the name is :",s.get("Name","ABC"))
s.update({"grade":"A"})
print(s)
print("age is removed :",s.pop("Age"))
print("every thing is erasssed:",s.clear())


                                                  # EXAMPLE 2
m={"math":90,"science":85,"english":88}
print(m)
print(m.popitem())
print(m)   
                                                 # WHILE LOOP EXAMPLE 
#stdent details 
s={}
while True:
    print("\n1.Add students to the list.")
    print("2.view the list of students.")
    print("3.exit")

    c=input("enter your choice:")
    
    if c=="1":
        id=input("enter student ID:")
        name=input("Enter student name:")
        s[id]=name
        print("Studend added successfully!!")
    elif c=="2":
        if not s:
             print("no student found!")
        else:
             for id,name in s.items():    
                print(f"Student name is :{name},  Student ID is :{id}")  
    elif c=="3":
         print("you have exited!!")
         break
         
    else:
         print("invalid choice, try again!!!")     


                                               # FUNCTIONS
print("hi")
def greet(name="xyz"):#default value 
    print("hello!,welcome to",name,"!!") 
greet("python")#passing the parameters 
greet()


def arth(x,y):
    a=x
    b=y
    c=a+b
    print(c)
x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
arth(x,y)


def add(a,b):
    return(a+b)
r=add(100,200)
print(r)


def square(num):
    return num*num
a=int(input("enter number:"))
print("square of number is :",square(a))



def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def quo(a,b):
    if b!=0:
       return a/b
    else:
        return"division  not possible"
a=int(input("enter first number:"))
b=int(input("enter the second number :"))
print("addition :",add(a,b))
print("subtraction:",diff(a,b))
print("multiplication:",mul(a,b))
print("division:",quo(a,b))





                                    #SIMPLE CALCULATOR
print("SIMPLE CALCULATOR")
c={}
while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit ")


    c=input("enter your choice:")
    a=int(input("enter first number:"))
    b=int(input("enter the second number :"))
      
    if c=="1":
        def add(a,b):
           return a+b
        print(add(a,b))
    elif c=="2":
        def deff(a,b):
           return a-b
        print(deff(a,b)) 
    elif c=="3":
         def mul(a,b):
           return a*b
         print(mul(a,b)) 
    elif c=="4":
         def quo(a,b):
            if b!=0:
                return a/b
            else:
               return"division not possible"
         print(quo(a,b))
    elif c=="5":
         print("you have exited!!")
         break
    
    else:
         print("invalid choice!!")