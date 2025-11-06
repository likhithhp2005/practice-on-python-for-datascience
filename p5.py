                                       # PLOATING GRAPHS USING MATPLOTLIB

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,5,7,8,9])
y=np.array([2,3,4,5,6,8])
plt.plot(x,y)
plt.show()


                                               # for marking the points 
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,5,7,8,9])
plt.plot(y,marker="o")
plt.show()


                                         #TO CHANGE THE LINE STYLE,COLOR WIDTH ETC 
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,5,7,8,9])
x=np.array([9,8,7,5,3])
plt.plot(y,marker="o",linestyle="dotted",color="grey")
plt.plot(x,marker="o",linestyle="dashed",color="black")
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,5,7,8,9])
x=np.array([9,8,7,5,3])
plt.plot(y,marker="o",linestyle="dotted",color="grey",linewidth="0.5")
plt.plot(x,marker="o",linestyle="dashed",color="black",linewidth="0.5")
plt.show()

                                             # PLOTING MULTIPLE LINES TOGETHER
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,5,7,8,9])
x=np.array([9,8,7,5,3])
y1=np.array([3,4,6,7,10])
x1=np.array([10,7,6,4,3])
plt.plot(y,marker="o",linestyle="dotted",color="grey",linewidth="0.5")
plt.plot(x,marker="o",linestyle="dashed",color="black",linewidth="0.5")
plt.plot(y1,marker="o",linestyle="dotted",color="skyblue",linewidth="0.5")
plt.plot(x1,marker="o",linestyle="dashed",color="red",linewidth="0.5")
plt.show()



                                              # LABLES ON X AND Y AXIS
import matplotlib.pyplot as plt
import numpy as np 
y=np.array([3,5,7,8,9])
x=np.array([9,8,7,5,3])
y1=np.array([3,4,6,7,10])
x1=np.array([10,7,6,4,3])
plt.plot(y,marker="o",linestyle="dotted",color="grey",linewidth="0.5")
plt.plot(x,marker="o",linestyle="dashed",color="black",linewidth="0.5")
plt.plot(y1,marker="o",linestyle="dotted",color="skyblue",linewidth="0.5")
plt.plot(x1,marker="o",linestyle="dashed",color="red",linewidth="0.5")
plt.xlabel("x-axis values")     #to lable on x axis 
plt.ylabel(("y-axis values"))    #to lable on y axis 
plt.title("COLORFUL GRAPH!",color="grey",size="30") #to give the main heading
plt.show()


              # TO CREATE A DICTINORY OUT SIDE AND CALL IT INSIDE 
import matplotlib.pyplot as plt
import numpy as np 
y=np.array([3,5,7,8,9])
x=np.array([9,8,7,5,3])
y1=np.array([3,4,6,7,10])
x1=np.array([10,7,6,4,3])
plt.plot(y,marker="o",linestyle="dotted",color="grey",linewidth="0.5")
plt.plot(x,marker="o",linestyle="dashed",color="black",linewidth="0.5")
plt.plot(y1,marker="o",linestyle="dotted",color="skyblue",linewidth="0.5")
plt.plot(x1,marker="o",linestyle="dashed",color="red",linewidth="0.5")


f1={"family":"serif","color":"black","size":"20"} #dict is declared outside and called inside
f2={"family":"serif","color":"grey","size":"30"}  #dict is delcared out side and called inside 
plt.xlabel("x-axis values",fontdict=f1)  #f1 is the dict called so it gets the properties of f1   
plt.ylabel("y-axis values",fontdict=f1)    #same 
plt.title("COLORFUL GRAPH!",fontdict=f2)  #f2 is the dict called 
plt.show()



                          #TO DISPLAY GRIDS 

import matplotlib.pyplot as plt
import numpy as np 
y=np.array([3,5,7,8,9])
x=np.array([9,8,7,5,3])
y1=np.array([3,4,6,7,10])
x1=np.array([10,7,6,4,3])
plt.plot(y,marker="o",linestyle="dotted",color="grey",linewidth="0.5")
plt.plot(x,marker="o",linestyle="dashed",color="black",linewidth="0.5")
plt.plot(y1,marker="o",linestyle="dotted",color="skyblue",linewidth="0.5")
plt.plot(x1,marker="o",linestyle="dashed",color="red",linewidth="0.5")


f1={"family":"serif","color":"black","size":"20"} #dict is declared outside and called inside
f2={"family":"serif","color":"grey","size":"30"}  #dict is delcared out side and called inside 
plt.xlabel("x-axis values",fontdict=f1)  #f1 is the dict called so it gets the properties of f1   
plt.ylabel("y-axis values",fontdict=f1)    #same 
plt.title("COLORFUL GRAPH!",fontdict=f2)  #f2 is the dict called 
plt.grid(axis="y")
plt.grid(axis="x")
plt.show()




                       # to display two graphs in one page 
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6])
y=np.array([9,8,7,6,3,2])
plt.subplot(2,3,1)
plt.title("graph 1") 
plt.plot(x,y)

x1=np.array([3,4,5,6,2,1])
y1=np.array([3,4,5,2,1,7])
plt.subplot(2,3,2)
plt.title("graph 2")  #(1,2,1)1 page 2 sides 2nd side 
plt.plot(x1,y1)

x=np.array([1,2,3,4,5,6])
y=np.array([9,8,7,6,3,2])
plt.subplot(2,3,3) 
plt.title("graph 3")
plt.plot(x,y)

x1=np.array([3,4,5,6,2,1])
y1=np.array([3,4,5,2,1,7])
plt.subplot(2,3,4) 
plt.title("graph 4") #(1,2,1)1 page 2 sides 2nd side 
plt.plot(x1,y1)

x=np.array([1,2,3,4,5,6])
y=np.array([9,8,7,6,3,2])
plt.subplot(2,3,5) 
plt.title("graph 5")
plt.plot(x,y)

x1=np.array([3,4,5,6,2,1])
y1=np.array([3,4,5,2,1,7])
plt.subplot(2,3,6)  
plt.title("graph 6")#(1,2,1)1 page 2 sides 2nd side 
plt.plot(x1,y1)
plt.show()


                                                # SCATTERS
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,17,3,13,5,6,7,8,28,10,11,12])
y=np.array([91,118,93,113,95,96,97,98,112,100,110,111])

plt.scatter(x,y)
plt.show()     


                    #different colors
import matplotlib.pyplot as plt
import numpy as np

x=np.array([5,17,81,13,5,17,71,93,28,10,11,12])
y=np.array([99,118,93,113,95,96,97,98,112,100,110,111])
color=np.array([0,10,20,30,40,50,60,70,80,90,100,110])
size=np.array([100,30,90,50,200,300,60,400,500,110,150,180])

plt.scatter(x,y, c=color,s=size,alpha=0.5)
plt.colorbar()
plt.show()


             #giving random numbers and colors
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
color=np.random.randint(100,size=(100))
size=10*np.random.randint(100,size=(100))

plt.scatter(x,y, c=color, s=size ,alpha=0.5,cmap="nipy_spectral")
plt.colorbar()
plt.show()


                                 #bar chart representation
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([3,4,5,6])

plt.bar(x,y) #vertival representation
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([3,4,5,6])

plt.barh(x,y) #horizontal representation
plt.show()


                                    #pie chart representation

import matplotlib.pyplot as plt
import numpy as np


y=np.array([1,2,3,4,5])
ml=["apple","banana","cheery","blueberry","strawberry"] #labeling the chart
exp=(0,0,0,0.3,0)  #used to seprate the block from the chart 0's are used to keep in place values are used to seprate
plt.pie(y , labels=ml, explode=exp) # pie chart representation

plt.show()


import matplotlib.pyplot as plt
import numpy as np


y=np.array([1,2,3,4,5])
ml=["apple","banana","cheery","blueberry","strawberry"] #labeling the chart
exp=(0,0,0,0.3,0)  #used to seprate the block from the chart 0's are used to keep in place values are used to seprate
plt.pie(y , labels=ml, explode=exp,shadow=True) # pie chart representation
plt.legend() #used to give side box with content of the cart
plt.show()
