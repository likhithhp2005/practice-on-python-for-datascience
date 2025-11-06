                                            #  SETS
f={"apple","banana","cheer"}
f.add("mango")
f.add("apple")
print(f)
 
#add method                                 #SET METHODS
f={"apple","banana"}
f.add("cheery")
print(f)

#update
f={"apple","banana"}
f.update(["cheery","grape"])
print(f)

#remove method 
f={"apple","banana","cherry"}
f.remove("cheery")
print(f)

#UNION unique 
a={1,2,3}
b={3,4,5}
print(a.union(b))

#intersection adding both
a={1,2,3}
b={3,4,5}
print(a.intersection(b))

#DIFFERENCE   only set 1 is considered and comparing with set2 
a={1,2,3}
b={3,4,5}
print(a.difference(b))

                           # "'two different courses have student lists:
                            #  pthon calss:{ravi,anitha,kiran,rahul}   java class:{ kiran, rahul,sneha,meena}
                           # writw a python program to : a)find the students who are learning both python and jqva
                             # b)students learning only python c)students learning only java    d)all unique students"'
p={"Ravi","anita","Kiran","Rahul"}
j={"Kiran","Rahul","Sneha","Meena"}
print("students learning both python and java =",p.intersection(j))
print("students learning python =",p.difference(j))
print("students learning java =",j.difference(p))
print("all unique students are =",p.union(j))

p={"milk","bread","eggs","butter"}
j={"butter","bread","jam","cheese"}
print("things we both bought :",p.intersection(j))
print("things only you bought :",p.difference(j))
print("things your friend bought:",j.difference(p))
print("unique things we bought:",p.union(j))

    