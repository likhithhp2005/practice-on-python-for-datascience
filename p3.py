                                                    #OOPS INHERITANCE


class animal:
    def sound1(self):
        print("Animal make sounds")

class dog(animal):
    def sound(self):
        print("dog barks 🐶")

class cat(dog):
    def sound2(self):
        print("cat mewos 😺")


c=cat()
c.sound1()
c.sound()
c.sound2()



                                                      #INHERITANCE EXAMPLE 2

class person:
    def __init__(self, name):
        self.name=name

    def display(self):
        print("Name:",self.name)

class student:
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def show(self):
        print("Grade:",self.grade)

s1=student("KusumaGowda","A++")

s1.display()
s1.show()



                                                        #OOPS ENCAPUSALATION


class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks=marks
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
s1=student("kusuma",90)
print("name:",s1.get_name())
print("marks:",s1.get_marks())
s1.set_name("kushi")
print("updated name:","kushi")
s1.set_marks(90)
print("updated marks:",95)

                                             #OOPS ENCAPUSALATION with out get and set 



class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def __display_info(self):
        print("Name:",self.__name)
        print("Marks:",self.__marks)
    
    def show(self):
        print("student details:")
        self.__display_info()

s=student("kusuma",90)
s.show()
        


                                                            #POLYMORPHISM AND ITS EXAMPLE

 
class Dog:            #declaring class
    def sound(self):
        return 'bark'

class Cat:
    def sound(self):
        return 'meow'
    

                      #funcyion that shows polymorphism
def make_sound(animal):
    print(animal.sound())

d=Dog()                #creating the object and calling the function
c=Cat()

make_sound(d)
make_sound(c)





class shape:
    def area(self):
        return 0
    
class rect(shape):
    def area(self):
         length=5
         width=4
         return length*width
    
class circle(shape):
    def area(self):
        radius=5
        return 3.14*radius*radius
    
shape=[rect(),circle()]

for s in shape:
    print("area=",s.area())

                                                        # ABSTRACTINONS
                                 
from abc import ABC,abstractmethod
class animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        return "boo boo"
    
class cat(animal):
    def sound(self):
        return "meow meow"
    
d=dog()
c=cat()
    
print("sound of dog",d.sound())
print("sound of cat",c.sound())

