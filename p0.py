x=10.0
y=20
sum=x+y
print("sum=",sum)
print(type(x))
print(type(sum))

#multiple assignment
a,b,c=1,2,3
print(c)

x=y=z="lilly"
print(x)
print(y)
print(z)


name="bob"
age=25
height=5.7
print("name:",name)
print("age:",age)
print("height:",height)


name=input("enetr your name: ")
branch=input("enter your branch:")
usn=input("enter your USN: ")
print(name)
print(branch)
print(usn)

a="3.14"
print(type(a))
b=float(a)
print(type(b))


#converting a value to a string type
a=10
print(type(a))
b=str(a)
print(type(b))

#example for lis 
a=["ab",1,"kk",24]
print(type(a))


#tuple example
b = (20,24)
print(type(b))


#example of dictinory
c={}#--->empty dictionary
print(type(c))
d={3}#--->it will be considered as set, if the elements are inside 
print(type(d))

#strings
#accesing character by index value
name='kusuma gowda'
print(name[0])
print(name[6])

#string operations
#string concatination
name="kusuma"
surname="gowda"
fullname=name+surname
print(fullname)

name="kusuma"
surname="gowda"
fullname=name+""+surname
print(fullname)

#repeated printing
message="hahe" *4
print(message)

#slicing and length


name="kusuma gowda"
print(name,len(name))
name="kusuma gowda"
name=name[0:6]
surname=name[7:]
print(name,len(name))
print(surname,len(surname))


name='kusuma gowda'
b=name.split()
print(b)


s="  The quick brown fox jumps over the lazy dog.The dog is not so lazy after all!  "
#to convert to lower case
low=s.lower()
print(low)
#to convert to upper case
print(s.upper())
#to print strip remove the exyra white space 
print(s.strip())
#to split
print(s.split())
#replace one word with another 
print(s.replace("dog","cat"))
#capitalize the first letter of each word
print(s.title())


text="hello python"
print(len(text))
print(text.index("python"))
print(text.index("hello python"))
print("first=",text[0])
print("last=",text[len(text)-1])

#counting how many times a letter is repeated
l="babana"
print(l.count("a"))


#replace 
l="I love python"
print(l)
print(l.replace("python","java"))

#reverse
l="welcome"
r="".join(reversed(l))  
print(r) #[or]
print(l[::-1])

#operators 
#arithmetic operations
a=int(input("enter the value of A:"))
b=int(input("enter the value of B:"))
print(a)
print(b)
print("sum=",a+b)
print("difference=",a-b)
print("product=",a*b)
print("mod=",a%b)
print("floor division:",a//b)
print("exponential=",a**b)
print("quotient=",a/b)

#comparision operators
a=int(input("enter the value of A:"))
b=int(input("enter the value of B:"))
print("a==b",a==b)
print("a>b",a>b)
print("a<b",a<b)
print("a!=b",a!=b)
print("a>=b",a>=b)
print("a<=b",a<=b)


#logical operators
a=True
b=False
print("a and b ",a and b) 
print("a or b", a or b)
print("a not b ", not a)   

#area of circle
area=int(input("enter the radius:"))
a=3.14*area**2
print("area=",a)