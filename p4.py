                                                        # EXAMPLES OF NUMPY
import numpy
arr=numpy.array([1,2,3,4,5,6,7])
print(arr)
print(type(arr))


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr)



import numpy as np
arr=np.array([["a","b"],["c","d"],[5,6]])
print(arr)
print(type(arr))


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[::-1])

import numpy as np
arr=np.array([1,2,3,4])
print(arr[2]+arr[3])



import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[-2,-2])
 
import numpy as np
arr=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,11,12]]])
print(arr[0,1,0])


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])


import numpy as np
a=np.array([[[]]])
print("array",a)
print("dimension",a.ndim)


                                                           # ARRAY ITERATION 
import numpy as np
a=np.array([10,20,30])
print("1d array")
for x in a:
    print(x)



import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print("2d array")
for r in b:
    print("row",r)
    for x in r:
        print(x)


import numpy as np
b=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("3d array")
for bck in b:
    print("row",bck)
    for row in bck:
      for a in row:
          print(a)
                                                        #CONCATINATING THE ARRAYS 
import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
r=np.concatenate((a,b))
print("concat:",r)



                                                              #concatination 
import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[5,6]])
r=np.concatenate((x,y),axis=1)
print("concatination",r)

                                                            # horizontal and vertical
import numpy as np
a=np.array([1,2,3,7,8])
b=np.array([4,5,6,8,9])
r=np.stack((a,b),axis=0)
print(r)
rr=np.stack((a,b),axis=1)
print(rr)



import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
h=np.hstack((a,b))
v=np.vstack((a,b))
print(h)
print(v)


                                                            # splitting
import numpy as np
a=np.array([1,2,4,5,6,7])
r=np.array_split(a,3)
print(r)



                      #colom wise slpitting 
import numpy as np
b=np.array([[1,2,3,4],
           [5,6,7,8]])
h=np.hsplit(b,2)
print(h)


import numpy as np
b=np.array([[1,2,3,4],
           [5,6,7,8]])
h=np.vsplit(b,2)
print(h)


           #splitting method
import numpy as np
b=np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]])
h=np.hsplit(b,2)
print(h)

import numpy as np
a=np.array([10,20,30,40,50,60])
r=np.where(a==40) #where is a inbulit word to search
print(r)# out put will be in index vallue 

import numpy as np
a=np.array([10,15,20,25,30])
e=np.where(a%2==0)
print(e)

import numpy as np
a=np.array([10,20,30,40,50])
p=np.searchsorted(a,35)
print(p)
 
import numpy as np
a=np.array([5,2,9,1,7])
print(a)
s=np.sort(a)
print(s)
print(s[::-1])
f=np.flip(s)
print(f)


import numpy as np 
s=np.array([
    [85,78,92],
    [74,88,90],
    [90,94,89],
    [65,70,72],
    [80,85,85],
])
m=np.mean(s,axis=0)
print("averange marks in math:",m)
print("highest marks:",np.max(m,axis=0))
print("lowest marks :",np.min(m,axis=0))
t=np.argmax(m)
print("topper students index:",t)
print("topper's avg:",m[t])


