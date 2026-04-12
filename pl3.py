#Array operations
import numpy as np

a=np.array([[1,2,3],
           [4,5,6]])
print("Array a:",a)

b=np.array([[5,6],
           [8,9],
           [10,11]])
print("Array b:",b)

#element by element
print(a*2)
print(a**2)
print(a+2)

#matrix multiplication
print(a@b)
print(a.dot(b))

INdexing & SLicing

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print("a[1,0] ->",a[1,0])
print("a[0:2,0:1] ->",a[0:2,0:1])
a=np.arange(12).reshape(3,4)
print(a)
print("a[-1:,-1:] ->",a[-1:,-1:])
print("a[-1:,-1] ->",a[-1:,-1])
print("a[-1][-1] ->",a[-1][-1])
print("a[2:2,3:3] ->",a[2:2,3:3])
a=np.arange(1,13).reshape(3,4)
print(a)
print("a[1:2,0:2] ->",a[1:2,0:2])
print("a[-2:-1,-4:-2] ->",a[-2:-1,-4:-2])

print("a[-3:-1,-4:-2] ->",a[-3:-1,-4:-2])
print(a[-2:-3:-1]) #-1 is to move in a reverse order otherwise the correct order is from the first to last both in 0 and -1 indexing (0 is from the first but -1 is from the last)


#Functions
##min() build in python function
##np.min() is a library function

print(a)
print("max",np.max(a))
print("min",np.min(a))
print("sum",np.sum(a))
print("sort",np.sort(a))
print("abs",np.abs(-4))
print("sqrt",np.sqrt(a))
print("Cumulative sum column wise",a.cumsum(axis=0))
print("Cumulative sum row wise",a.cumsum(axis=1))
print("Flatten func",a.flatten())
print("Transpose func",a.transpose())
print(a.max(axis=1))
print(a.max(axis=0))
print(a.min(axis=1))
print(a.min(axis=0))






