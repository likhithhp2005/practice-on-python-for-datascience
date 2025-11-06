                                                        #MONTHLY SALES
import numpy as np 
s=np.array([
      [120,135,150,160,145,155],
      [80,95,100,110,105,115],
      [150,160,170,175,180,190]
])
ts=np.sum(s,axis=1)
t=print("total sales:",ts)
ta=np.mean(s,axis=1)
print("average sales:",ta)
hs=np.max(s,axis=1)
print("high sales:",hs)
bp=np.argmax(s,axis=1)
print("best performing product:",bp)



                                                 #RANDOM DATA DISTRIBUTION
from numpy import random
x=random.rand()
print(x)


from numpy import random
x=random.randint(100)
print(x)


                                                      #dimenssions
import numpy as np 
a=np.array(42)
b=np.array([1,2,3,4,5,6])
c=np.array([[1,2,3],[5,6,7]])
d=np.array([[[1,2,3],[4,5,6],
             [1,2,3],[4,5,6],
             [1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


                                                           # PANDAS
import pandas as pd
print(pd.__version__)  


                                                         #EXAMPLES OF PANDAS 
import pandas as pd 
d={
    "name":["kusuma","lishi","ananya"],
    "age":[19,7,20],
    "city":["newyork","london","paris"]

}
df=pd.DataFrame(d)   #FRAMES IN DATA LIST FORMAT 
print(df)

print("Data Frame:\n")
print('Names Colums:\n',df["name"])  #DESPLAYS ONLY NAMES 

print("first 2 rows\n",df.head(2))  #DISPLAYS THE NUMBER OF ROWS SELECTED 

                                                            #MATPLOTLIB

import matplotlib
print(matplotlib.__version__)
                                                #CREATES XY GRAPH IN SINGLE DIMENSION
import matplotlib.pyplot as plt
import numpy as np
 
x=np.array([0,6])
y=np.array([0,50])

plt.plot(x,y)
plt.show()       




                                                    