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
df_clean['published_at'] = pd.to_datetime(df_clean['published_at'], errors='coerce',utc=True)
dropna_count = df_clean['published_at'].isnull().sum()
print(f"Missing published_at after conversion: {dropna_count}")
df_clean = df_clean.dropna(subset=['published_at'])

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
#HeatMap
plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

#Outlier Detection
#HISTOGRAM
'''plt.figure()
sns.histplot(df_clean['subscribers'], bins=50, kde=True)
plt.title("Subscriber Distribution")
plt.xlabel("Subscribers")
plt.show()'''

subs_crores = df_clean['subscribers'] / 1e7

plt.figure(figsize=(10, 5))
sns.histplot(subs_crores, bins=50, kde=True, color='skyblue')
plt.title("Subscriber Distribution (in Crores)")
plt.xlabel("Subscribers (Crores)")
plt.ylabel("Frequency")
plt.show()

'''#BOXPLOT
plt.figure()
plt.boxplot(df_clean['subscribers'], vert=False)
plt.title("Outliers in Subscribers")
plt.xlabel("Subscribers")
plt.show()'''

plt.figure(figsize=(10, 4))
plt.boxplot(subs_crores, vert=False, patch_artist=True)
plt.title("Outliers in Subscribers (in Crores)")
plt.xlabel("Subscribers (Crores)")
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


#Question-1 
#How has YouTube channel creation evolved over the years among the top 1000 channels?
df_clean['year'] = df_clean['published_at'].dt.year
yearly_counts = df_clean[df_clean['year'] >= 2005]['year'].value_counts().sort_index()
plt.figure()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values)
plt.title("YouTube Top Channel Creation Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Channels Created")
plt.show()

#Question-2
#Which countries dominate the top 1000 channels by total subscribers?

#Grouping by country
country_subs = df_country.groupby('country')['subscribers'].sum().sort_values()

#Taking top 10 countries
top_countries = country_subs.tail(10)/1e7 #Converting to crores for better visualization
plt.figure()
plt.barh(top_countries.index, top_countries.values)
plt.title("Top Countries by Total Subscribers")
plt.xlabel("Total Subscribers (In Crores)")
plt.ylabel("Country")
plt.show()

#Question-3
#Which content categories dominate the top 1000 channels by total subscribers?

'''#Category Extraction
df_clean['category'] = df_clean['topic_categories'].str.split('/').str[-1]
df_clean['category'] = df_clean['category'].str.replace('_', ' ')
df_clean['category'] = df_clean['category'].str.title()'''

# Improved Category Extraction
df_clean['category'] = df_clean['topic_categories'].str.split('|').str[0].str.split('/').str[-1]
df_clean['category'] = df_clean['category'].str.replace('_', ' ').str.title().str.strip()

#Group data
category_subs = df_clean.groupby('category')['subscribers'].sum().sort_values()

#top 10
top_categories = category_subs.tail(10)/1e7 #Converting to crores for better visualization

plt.figure()
plt.barh(top_categories.index, top_categories.values)
plt.title("Top Categories by Total Subscribers")
plt.xlabel("Total Subscribers (In Crores)")
plt.ylabel("Category")
plt.show()
