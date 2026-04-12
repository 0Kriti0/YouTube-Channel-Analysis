import pandas as pd
##a=pd.read_csv("ABC.csv")#incase the file is in a diff folder->go to properties->copy the path->paste in green part-> change \ to \\ or /
##a=pd.read_csv("C:\\Users\\kriti\\OneDrive\\Pictures\\Screenshots\\ABC.csv")
a=pd.read_csv("D:\\ABC.csv")
print(a.info()) #can only be used for pandas dataframe , used for pre processing (identifying the missing values)
print(a.describe()) #used for statistical analysis (identifying the outliers)
print(a.head())#gives first five enteries in the file
print(a.tail())#gives last five enteries in the file
print(a.head(10))#the number written in parameters gives the exact amount of enteries, works for tail(10) too

#Note: when the mean and 2nd quartile values are same that means that there are no outliers


import numpy as np
#Creating primary data with missing values
data={
    'ID':[1,2,3,4,5],
    'Name':['Alice','Bob',np.nan,'David','Eve'],
    'Age':[25,np.nan,30,np.nan,40],
    'City':['New York','Los Angeles','Chicago',np.nan,'Houston'],
    'Salary':[50000,60000,np.nan,80000,70000]
}

df=pd.DataFrame(data)#type casting data variable to DataFrame
print("Original dataframe with missing values:")
print(df)

#Detecting missing values
print("\nMissing values in each column:")
print(df.isnull().sum()) #gives a total no of missing values in every column

#types of data = Numeric ->Continous(always updating,modifying like tgpa) , Discrete(fixed like pincode) = Categorical ->Nominal(any order), Ordinal(order is fixed like grade calculation - 0 ... G)
#cont-mean()->function used -> interpolate() ; discrete-median() ; categorical-mode() ->function used ->ffill(),bfill();  for missing data filling  ; functions only available in python not R

#Dropping rows with missing values
df_dropped_rows = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped_rows)

#Dropping columns with missing values
df_dropped_cols= df.dropna(axis=1)
print("\nDataFrame after dropping columns with missing values:")
print(df_dropped_cols)

#Filling missing values with specific values
df_filled = df.fillna({'Age': df['Age'].mean(),'City':'New York','Salary':df['Salary'].median()})
print("\n DataFrame after filling missing values:")
print(df_filled)

#Forward fill (updated to avoid FutureWarning)
df_ffill=df_filled.ffill()
print("\n DataFrame after forward filling:")
print(df_ffill) #missing value is filled (the same as the previous value) which wasn't filled previously

#Backward fill(updared to avoid FutureWarning)
df_bfill= df_filled.bfill()
print("\n DataFrame after backward filling:")
print(df_bfill) #missing value is filled (the same as the next value) which wasn't filled previously

#Interpolating missing values (upadted to avoid FutureWarning) #need to have before and after values 
df_numeric = df.select_dtypes(include =[np.number])
df_interpolated = df_numeric.interpolate()
#Merge back non-numeric columns
df_final = df.copy()
df_final[df_numeric.columns]=df_interpolated
print("\nDataFrame after interpolation:")
print(df_final)

#saving cleaned data
cleaned_file_path = "ABC.csv"
df_final.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to:{cleaned_file_path}")

