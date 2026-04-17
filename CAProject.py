import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats

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

#Question-4
#Predict subscribers based on number of videos

#Independent and dependent variables
X = df_clean[['videos']].values
y = df_clean['subscribers'].values

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Model
model = LinearRegression()
model.fit(X_train, y_train)

#Prediction
y_pred = model.predict(X_test)

#Error
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2 Score:", r2)
print(f"Intercept:{model.intercept_:.2f}")
print(f"Coefficient:{model.coef_[0]:.2f}")

#Plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Number of Videos")
plt.ylabel("Subscribers")
plt.title("Linear Regression: Videos vs Subscribers")
plt.legend()
plt.grid(True)
plt.show()

#Prediction
new_value = np.array([[50000]])
predicted = model.predict(new_value)
print("Predicted subscribers:", predicted)

#Predict subscribers based on number of views
#Independent and dependent variables
X = df_clean[['views']].values
y = df_clean['subscribers'].values

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Model
model = LinearRegression()
model.fit(X_train, y_train)

#Prediction
y_pred = model.predict(X_test)

#Error
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2 Score:", r2)
print(f"Intercept:{model.intercept_:.2f}")
print(f"Coefficient:{model.coef_[0]:.2f}")

#Plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Number of Views")
plt.ylabel("Subscribers")
plt.title("Linear Regression: Views vs Subscribers")
plt.legend()
plt.grid(True)
plt.show()

#Prediction
new_value = np.array([[1_000_000_000]])
predicted = model.predict(new_value)
print("Predicted subscribers:", predicted)

#Question-5
#Compare subscribers before and after 2015

#H0 (Null Hypothesis): Mean subscribers of channels created before 2015 
#                      = Mean subscribers of channels created in/after 2015
#H1 (Alternative Hypothesis): Mean subscribers of channels created before 2015 
#                            ≠ Mean subscribers of channels created in/after 2015

from scipy import stats

#Significance level (5%)
alpha = 0.05

#Creating two groups based on year
group1 = df_clean[df_clean['year'] < 2015]['subscribers']   #Before 2015
group2 = df_clean[df_clean['year'] >= 2015]['subscribers']  #2015 and after

#Two-sample independent t-test
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=True)

print("Two-sample t-test (Before vs After 2015):")
print(f"T-statistic = {t_stat:.4f}")
print(f"P-value = {p_value:.4f}")

#Decision rule
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis.")
else:
    print("Conclusion: Fail to reject the null hypothesis.")

# Question-6
# Which are the top 10 YouTube channels based on subscribers, views, and number of videos?

# Top 10 by Subscribers
top_subs = df_clean.sort_values(by='subscribers', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.barh(top_subs['title'], top_subs['subscribers']/1e7)
plt.gca().invert_yaxis()
plt.title("Top 10 Channels by Subscribers (in Crores)")
plt.xlabel("Subscribers (Crores)")
plt.ylabel("Channel Name")
plt.show()


# Top 10 by Views
top_views = df_clean.sort_values(by='views', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.barh(top_views['title'], top_views['views']/1e9)
plt.gca().invert_yaxis()
plt.title("Top 10 Channels by Views (in Billions)")
plt.xlabel("Views (Billions)")
plt.ylabel("Channel Name")
plt.show()


# Top 10 by Number of Videos
top_videos = df_clean.sort_values(by='videos', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.barh(top_videos['title'], top_videos['videos'])
plt.gca().invert_yaxis()
plt.title("Top 10 Channels by Number of Videos")
plt.xlabel("Number of Videos")
plt.ylabel("Channel Name")
plt.show()