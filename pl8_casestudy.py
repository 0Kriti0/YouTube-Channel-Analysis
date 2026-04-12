#CA1#read
#info,head etc
#df.fillna,ffill,bfill
#df.head,tail,isnull.sum,info



import pandas as pd

#df = pd.read_excel('tips.xls') #97-2003 
df = pd.read_excel('tips.xlsx')#workbook
#df = pd.read_csv('tips.csv')
#1. Read CSV
print("Data Loaded Successfully!\n")
#2.Display first 10 rows
print("First 10 rows: \n",df.head(10),"\n")
#3.Display last 5 rows
print("Last 5 rows:\n", df.tail(),"\n")
#4.DataFrame summary
print("dataFrame Info:\n")
df.info()
#5. Descriptive Statistics
print("Descriptive statistics:\n",df.describe(),"\n")
#6. Shape of dataFrame
print("Shape of DataFrame:",df.shape,"\n")
#7. Column names
print("Column Names:\n",df.columns,"\n")
#8. Checking for missing values
print("Missing Values:\n",df.isnull().sum(),"\n")
#9. Drop rows with missing values 
df_cleaned = df.dropna()
print("Data after dropping missing values:\n",df_cleaned.head(),"\n") #this is used for checking if there has been an update with the missing values
#can use .tail(), .info() and .isnull().sum() function too in this case
#10. Fill missing values with 0
df_filled = df.fillna(0)
print("Data after filling missing values:\n",df_filled.head(),"\n")
#11. Group by a column and aggregate
grouped_data = df.groupby('day')['total_bill'].sum() #groupby(1. should be categorical)[ 2. should be numerical]
print("Total Bill by Day:\n",grouped_data,"\n")
#12. Sort values by total_bill in descending order
sorted_df=df.sort_values(by='total_bill',ascending=False) #values is the function whatever written before it will be applied for example sort,count etc
#if sorting applied again the previous condition for sorting is overwritten
print("Top 5 Total Bill Records:\n",sorted_df.head(),"\n")
#13. Apply function to transform total_bill column
df['total_bill_in_hundreds']=df['total_bill'].apply(lambda x:x/100)
print("Transformed Total Bill Data:\n",df[['total_bill','total_bill_in_hundreds']].head(),"\n")


#14. Merge operation(Assuming df1 and df2 are available for merging)
#df_merged=df1.merge(df2,on='Customer_ID',how='inner')
#print(df_merged.head())
#15. Concatenation (Assuming df1 and df2 exist)
#df-combined = pd.concat([df1,df2],axis=0)
#print(df_combined.head())


#16.Pivot Table Example
pivot_table = df.pivot_table(values='total_bill',index='day',columns='Gender',aggfunc='sum')
print("Pivot Table:\n",pivot_table,"\n")
#17. Accessing a column
print("Total Bill Column:\n",df['total_bill'].head(),"\n")
#18. Filtering using loc
filtered_df = df.loc[df['total_bill']>20] #1st value should be pandas variable and 2nd can be pandas variable or a value
print("Filtered Data (Total Bill > 20):\n",filtered_df.head(),"\n")
#19. Accessing rows with iloc
print("First 5 rows using iloc:\n",df.iloc[0:5],"\n") #this works as head() if you want tail then iloc[-5:-1]or[-5:]
#20. Renaming columns
df_renamed=df.rename(columns={'total_bill':'Total_Bill_Amount'})
print("Renamed Column Names:\n",df_renamed.columns,"\n")
print(df_renamed.head()) #doesnt give full data in idle so info is preferred 
print(df_renamed.info())



