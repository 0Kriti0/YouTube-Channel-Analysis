import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("youtube_top_1000_by_subscribers.csv")
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())

#EDA
#DATA CLEANING
#Checking missing values
print("Missing values:\n", df.isnull().sum())

#Creating a copy of the original dataset
df_clean = df.copy()

#Converting published_at to datetime
df_clean['published_at'] = pd.to_datetime(df_clean['published_at'], errors='coerce', utc=True)

#Creating channel age (in years)
reference_date = pd.Timestamp('2026-01-01', tz='UTC')
df_clean['channel_age_years'] = (reference_date - df_clean['published_at']).dt.days / 365.25

#Optional (for efficiency detection)
df_clean['views_per_video'] = df_clean['views'] / df_clean['videos'].replace(0, np.nan)

##print("Missing published_at:", df_clean['published_at'].isnull().sum())
##print("Missing age:", df_clean['channel_age_years'].isnull().sum())
##print("Missing subscribers:", df['subscribers'].isnull().sum())
##print("Missing views:", df['views'].isnull().sum())

#Drop rows with missing important values
df_clean = df_clean.dropna(subset=['subscribers', 'views', 'channel_age_years'])

#Create dataset with known country
df_country = df_clean.dropna(subset=['country']).copy()

#Dataset sizes after cleaning
print("\nAfter cleaning:")
print("Full dataset :", df_clean.shape) #for general purpose analysis
print("With country :", df_country.shape) #for country based analysis

#Summary statistics for key variables only
print("\nSummary Statistics:")
print(df_clean[['subscribers', 'views', 'videos']].describe())

#CORRELATION
numeric_cols = ['subscribers', 'views', 'videos', 'channel_age_years']

corr = df_clean[numeric_cols].corr()
print("\nCorrelation Matrix:")
print(corr)
plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

#BOXPLOT
plt.figure()
plt.boxplot(df_clean['subscribers'], vert=False)
plt.title("Outliers in Subscribers")
plt.xlabel("Subscribers")
plt.show()


#IQR METHOD (Data not normal)
subs_arr = np.array(df_clean['subscribers'])

Q1 = np.percentile(subs_arr, 25)
Q3 = np.percentile(subs_arr, 75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = subs_arr[(subs_arr < lower) | (subs_arr > upper)]

print("Outliers count (IQR):", len(outliers))


