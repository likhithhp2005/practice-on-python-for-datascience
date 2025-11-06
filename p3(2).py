                                                         # ERRORS
try:
     num=int(input("enter the number:"))
     print("you entered:",num)

except ValueError:
     print("please print only numbers!!")


try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second  number:"))
    r=a/b
    print("result=",r)
except ValueError:
    print("please enter only integers!🧐")
except ZeroDivisionError:
    print("you have enetred zero as dinominator!!🤯")
finally:
    print("program trminated!!")



try:
    n=[10,20,30,40,50]
    index=int(input("enter an index(0-4:)"))
    print("value at index:",n[index])
except ValueError:
    print("please enter only integers!🧐")
except IndexError:
    print("index out of range!🧐")
finally:
    print("program teminated!!")




                                                                #RAISING ERROR 
try:
    m = int(input("Enter the marks (0–100): "))
    if m < 0 or m > 100:
        raise ValueError("Please enter marks only between 0 and 100.")
    else:
        print("Marks accepted successfully!!")
except ValueError as e:
    print("ERROR",e)
except Exception:
    print("please enter numbers only")
finally:
    print("Program finished!")


import numpy
print(numpy.__version__)


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr)
print(type(arr))