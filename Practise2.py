##Use "Sample super store excel dataset .xlsx" dataset to answer the following questions:
##    answer the following questions:
##        A Eda
##        b Corr()
##        c detect and handle the missing data and outliers
##        d Perform Slr to predict the profit

import pandas as pd 
#example df=pd.read_excel("sample_superstore_excel_dataset.xlsx", sheet_name="Orders")
df=pd.read_csv("StudentsPerformance.csv")
print(df.info())
print(df.describe())
print(df.tail())
