import pandas as pd
import numpy as np
##a1=pd.Series()
##print(a1)
##a=pd.Series([1,2,3])
##print(a)
##b=pd.Series([1,2,3],index=['A','B','C'])
##print(b)
##data={'a':0.,'b':1.,'c':2.}
##s=pd.Series(data)
##print(s)
##data={'a':0.0,'b':1.0,'c':2.0}
##s1=pd.Series(data,index=['b','c','d','a']) #only possible for dictionary 
##print(s1)
##list=['g','e','e','k','s']
##s2=pd.Series(list)
##print(s2)
###print(pd.__version__)
##
##
##a=pd.Series(np.arange(6))
##a=np.array([1,2,3])
##b=pd.Series(a)

##a=pd.Series([1,2,3])
##print(a)
##b=pd.Series([[1,2,3],[4,5,6]])
##print(b)
##c=pd.Series([[1,2,3],[4,5]])
##print(c)
##d=pd.Series([[1,2,3],['A']])
##print(d)

#default type of numpy variable is float
#default type of pd.Series variable is object 

##a=pd.Series(np.arange(6))
##print(a)
##a=np.array([1,2,3])
##b=pd.Series(a)
##print(b)
##
##a1=np.array([1,2,3,4,5])
##a2=np.array([6,7,8,9,0])
##a3=pd.Series(a1,a2)
##a4=pd.Series([a1,a2])
##print(a3)
##print(a4)


##ser1=pd.Series(np.linspace(3,33,3))
##print(ser1)
##ser2=pd.Series(np.linspace(1,100,10))
##print(ser2)
##arr=pd.Series(np.arange(6))
##print(arr)
##
##arr1=pd.Series([22,33,44,55],index=['a','b','c','d'])
##print(arr1)
##print('b' in arr1)
##print('f' in arr1)
##
###series operations 
##
ds1=pd.Series([2,4,6,8,10])
##ds2=pd.Series([1,3,5,7,9])
##add = ds1 +  ds2
##sub = ds1 -  ds2
##mul = ds1 *  ds2
##div = ds1 /  ds2
##print("Add two Series:",add)
##print("Sub two Series:",sub)
##print("Mul two Series:",mul)
##print("Div two Series:",div)
##print("Compare the elements of the said Series:")
##print("Equals: ",ds1==ds2)
##print("Greater than: ",ds1>ds2)
##print("Less than: ",ds1<ds2)

#dataframe and series operations
df=pd.DataFrame([[1,4,7],[2,5,8],[3,6,9]],columns=[0,1,2])#can be written as({0:[1,2,3],1:[4,5,6],2:[7,8,9]})
print(df)
a=ds1+df
print(a)



































