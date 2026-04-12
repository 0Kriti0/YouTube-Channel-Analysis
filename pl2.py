#Array creation
import numpy as np

#np.array can create array 1d and more.
a1=np.array([1,2,3,])
print("Array a1:",a1) #1d array
print(a1.shape)

#2d array implementation.
a2= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Array a2:",a2) #2d array

b1=np.arange(12)
print("Arange b1:",b1) #usually used for 1d array but can alter it to 2d and more using reshape.

#arange is 1d array but we can forcefully alter it to 2d etc using reshape.
b2=np.arange(12).reshape(3,4) #3*4(rows*columns)  should be equal to 12.
print("Arange b2:",b2)

#String input
c2=np.matrix('1 2; 3 4') #the no of digits before and after ; should be equal.
print("Via string input : \n", c2) #usually used for 2d array but can be 1d too.

c1=np.matrix('1 2 3 4')
print("Matrix c1:",c1) #1d array
print(c1.shape)

#3d array

b3=np.arange(12).reshape(3,2,2)
print(b3)

print("\n")

b3.shape=(3,2,2)#does not work with matrix for more than 2d array.
print(b3)

d=np.eye(3,3)
print("Identity:",d)

d=np.eye(3,3,dtype=int)
print("Identity with int : ",d)

d=np.zeros((3,3),dtype=int)
print("Zeros:",d)

d=np.ones([3,3],dtype=int)
print("Ones:",d)

d=np.empty([3,3],dtype=int)

print("Empty:",d)

d=np.full([3,3],25)
print("Full:",d)
