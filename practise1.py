import numpy as np
#q3
a= np.arange(12).reshape(3,4)
a=np.array([[90,91,81,45],[85,89,95,99],[88,87,81,93]])
h= np.max(a)
l= np.min(a)
t= np.sum(a,axis = 1)
avg = np.mean(a,axis = 1)
sqrt = np.sqrt(a)
r= a.cumsum(axis = 1)
c= a.cumsum(axis = 0)
t= a.transpose()

m = a/10
st1=a[1]
ps=a[:,2]
n= int(input("Enter"))
l=[]
for i in range(n):
    l.append(int(input("enter")))
a= np.array(l)
#q1
import pandas as pd 
df=pd.read_csv("rainfall.csv")
print(df.info())
print(df.describe())
print(df.head())

missing_values = df.isnull().sum()
print(missing_values)

missing_percent = df.isnull().sum()*100
print(missing_percent)

og_shape=df.shape
drop=df.dropna()
new_shape=drop.shape
print(og_shape)
print(new_shape)

mean = df['Annual'].mean()
median = df['Annual'].median()
std = df['Annual'].std()
print(mean)
print(median)
print(std)

regionly_avg = df.groupby('Subdivision')['Annual'].mean()
highest=regionly_avg.idxmax()
lowest = regionly_avg.idxmin()
print(regionly_avg)
print(highest)
print(lowest)

yearly_avg= df.groupby('Year')['Annual'].mean()
print(yearly_avg)

total = df['Annual'].sum()
print(total)

seasonal_avg = df[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']].mean()
print(seasonal_avg)
highest=seasonal_avg.idxmax()
lowest = seasonal_avg.idxmin()
print(highest)
print(lowest)

seasonal_variation = df.groupby('Subdivision')[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']].std()
print(seasonal_variation)

##df_mean=df.fillna(df.mean())
##df_median=df.fillna(df.median())
df_ffill=df.ffill()
##df_bfill=df.bfill()
##print(df_mean['Annual'].mean())
##print(df_median['Annual'].mean())
print(df_ffill['Annual'].mean())
##print(df_bfill['Annual'].mean())
##fill= df.ffill()
###
#xxx#fillna = df.fillna({'Annual':df['Annual'].mean(),['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']:df[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']].ffill})
##print(fillna)

# Separate numeric and non-numeric columns
num_cols = df.select_dtypes(include=[np.number]).columns
cat_cols = df.select_dtypes(exclude=[np.number]).columns

# Fill numeric columns with mean
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical columns with forward fill
df[cat_cols] = df[cat_cols].fillna(method='ffill')

#12. Sort values by total_bill in descending order
sorted_df=df.sort_values(by='total_bill',ascending=False)

#13. Apply function to transform total_bill column
df['total_bill_in_hundreds']=df['total_bill'].apply(lambda x:x/100)

#16.Pivot Table Example
pivot_table = df.pivot_table(values='total_bill',index='day',columns='Gender',aggfunc='sum')
print("Pivot Table:\n",pivot_table,"\n")

df_renamed = df.rename(columns={'Annual':'annual'})




##
###S
###q1
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset("titanic")
print("data loaded")
print(titanic.info())
print(titanic.head())
print(titanic.columns)
print(titanic.dtypes)
print(titanic.shape)

s=pd.Series(titanic['age'])
print(s)
print(s.describe())
print(titanic.isnull().sum())
fill_mean=titanic['age'].fillna(titanic['age'].mean())
print(fill_mean.head(10))

#bar
flights = sns.load_dataset("flights")
print(flights.head(10))
print(flights.info())
plt.figure()
sns.countplot(x="month",data=flights)
plt.title("Bar(s)")
plt.show()

mt_count=flights["month"].value_counts()
plt.figure()
plt.bar(mt_count.index,mt_count.values)
plt.xlabel("months")
plt.ylabel("count")
plt.title("Bar(M)")
plt.show()

#line
#q2
plt.figure()
sns.lineplot(x="year",y="passengers",data=flights,estimator="mean")
plt.title("Line(s)")
plt.show()

year=flights.groupby('year')['passengers'].mean()
plt.figure()
plt.plot(year.index,year.values,marker="o")
plt.xlabel("years")
plt.ylabel("passengers")
plt.title("Line(M)")
plt.show()

month_avg = flights.groupby("month")["passengers"].mean()

highest = month_avg.sort_values(ascending=False)

print("Month with highest average passengers:")
print(highest.index[0])

#Histo

plt.figure()
sns.histplot(flights['passengers'],bins=10,kde=True)
plt.title("Hist(s)")
plt.show()

pie
plt.figure()
count = flights['month'].value_counts()
plt.pie(count,labels=count.index,autopct="%1.1f%%")
plt.show()







