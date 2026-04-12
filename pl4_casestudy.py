import numpy as np
n=int(input("no of elements"))
l= []
for i in range (0,n):
      l.append(int(input("Enter value:")))
a= np.array(l)
a.reshape(2,2)

##a=... b=a , in this case the memory address will be the same for both
## in copy and view function the memory address will be completly different
##if i modify the copy variable the original variable will remain same but the view function's variable will be changed too
##Shallow copy - view, Deep Copy - copy

a = np.arange(6).reshape(3,2)
b=a
print(id(a))
print(id(b))
print(a is b)

print("COPY-")

c= a.copy()
print(c)
print(id(c))
c[0][0]=55
print(c)
print(a)
print(a is c)

print("VIEW-")

d= a.view()
print(d)
print(id(d))
d[0][0]=65
print(d)
print(a)

##
##Question 1: Data Transformation and Analysis
##You are working as a data analyst for a company that deals with large datasets. Your team receives a 2D NumPy array containing customer transaction data, where each row represents a different customer, and columns represent transaction amounts in different months.
##Using NumPy functions:
##1.	Find the maximum, minimum, and total transaction amount across all customers.
##2.	Compute the cumulative sum of transactions column-wise.
##3.	Flatten the 2D array into a 1D array and sort the transactions in ascending order.
##4.	Transform the dataset by reshaping it into a different structure.
##Write Python code to achieve these tasks and explain the significance of each function in data transformation.
### Sample transaction data (4 customers, 5 months)

##n= int(input("Enter the no of elements- "))#20
##l=[]
##for i in range(0,n):
##      l.append(int(input("Enter value- ")))
##a= np.array(l)
##a.shape=(4,5)
##print(a)
##print("max=",a.max(axis=1))
##print("min=",a.min(axis=1))
##print("sum=",a.sum(axis=1))
##print("Cumulative sum column wise=",a.cumsum(axis=0))
##print("Flatten=",a.flatten())
##print("sort=",np.sort(a.flatten()))
##print(a.reshape(2,2,5))#a=np.arange().reshape() #a.shape = (2,2,5)

##Question 2: Matrix Operations and Computation
##A company is working on an AI-based recommendation system and needs to perform several matrix operations. The dataset consists of two matrices:
##•	Matrix A (User-Product Interaction): Contains ratings given by users to different products.
##•	Matrix B (Product-Feature Mapping): Contains product attributes that help in recommendations.
##Using NumPy:
##1.	Perform element-wise multiplication of the user-product interaction matrix with another similar matrix.
##2.	Compute the matrix multiplication of A and B using two different NumPy functions.
##3.	Find the transpose of matrix A .
##4.	Identify the shape, number of dimensions, and data type of matrix B.
##Write Python code to perform these operations and explain how these transformations are used in recommendation systems.
### Defining matrices
##A = np.array([[5, 3, 2], [4, 1, 5], [3, 2, 4]])  # User-Product Interaction
##B = np.array([[1, 2], [3, 4], [5, 6]])  # Product-Feature Mapping


##a = np.array([[5, 3, 2], [4, 1, 5], [3, 2, 4]])
###c=np.array([[1, 2, 2], [3, 1, 5], [3, 2, 4]])
###print(a*c)
##b = np.array([[1, 2], [3, 4], [5, 6]])
##a1=a
##b1=b
##print(a*a1)
##print(b*b1)
##print(a@b)
##print(a.dot(b))
##print(a.transpose())
##print(b.shape)
##print(b.ndim)
##print(b.dtype)

#a=np.array([85,92,78,88,90]
n= int(input("Enter the no of elements- "))
l=[]
for i in range(0,n):
      l.append(int(input("Enter value- "))) #can do list(map(int,input("enter".split())
a= np.array(l)
a.shape=(1,5)
s=np.sum(a) #can take mean function directly too , np.mean(a)
avg = s/n
print("Average Grade: ",avg)
if(avg<60):
      print("Letter Grade: F")
elif(avg>=60 and avg<=69):
      print("Letter Grade: D")
elif(avg>=70 and avg<=79):
      print("Letter Grade: C")
elif(avg>=80 and avg<=89):
      print("Letter Grade: B")
else:
      print("Letter Grade: A")



































