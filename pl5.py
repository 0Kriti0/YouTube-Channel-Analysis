##INdexing, Slicing, Loc & Iloc
import pandas as pd
##a1=pd.Series()
##print(a1)
##a=pd.Series([1,2,3])
##print(a)
b=pd.Series([1,2,3],index=['A','B','C'])
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
##
##s3=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
##l=['c','e']
##print(s3['b'])
##print(s3['e'])
##print(s3[l])
##print(s3[['a','e']])#passing a list as indexing 
###print(s3.loc[0])#this wont work because we passed a,b,c,d,e and not 0,1,2,3,4
##print ("location of b")
##print(s3.loc['b'])#shows according to the indexing passed by us ie explicit with the use of index = 
###print(s3.iloc['b'])#this wont work bcz python only passes 0,1,2 etc.
##print("index location of b")
##print (s3.iloc[1])#shows according to the indexing allocated by python ie implicit

##
##x=a.iloc[ : ,1:4] => a[['Reg no','ca1','ca2']]  (this is input)
##y=a['marks'] (this is output)

##Data Frame
c1=pd.DataFrame()
print(c1)
c2=pd.DataFrame([1,2,3],columns=['CA1'])
print(c2)
c=pd.DataFrame(b)
print(c)
d=pd.DataFrame(c,columns=['Roll No'])
print(d)
d1=pd.DataFrame(b,columns=['Roll No'])
print(d1)

