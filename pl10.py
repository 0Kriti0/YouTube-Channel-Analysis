#EDA(Exploratory Data Analysis) ->info()
##                              ->describe()

##->Univariant ->Histogram

##->Bivariant  ->corr()
##             ->cov()
##             ->Bar
##             ->Pie
##             ->Line
             
##->Multivariant ->corr()
##               ->pairplot()

##->Handling the missing values ->isnull()
##                              ->mean, median, mode
##                              ->ffill, bfill, interpolate
##                              ->dropna, fillna

##->Visualization ->Bar
##                ->Pie
##                ->line
##                ->Histogram
##                ->Scatterplot
##                ->Heatmap
##                ->Boxplot
##                ->Pairplot
                
##->Outlier Detection ->Boxplot                   in ca2 and end term apply BoxPlot first and if there are circles proceed with the IQR and ZScore tests,
                                    #if questin says statistical then first find whelther the data is normal or not if it is normal proceed with z score if not then apply iqr

##                    ->IQR
##                    ->ZScore

##->Feature Engineering ->Feature Selection
##                      ->Feature Extraction
##                      ->PCA
##                      ->Dimensionlity reduction

#ca2
#1 question from simple linear regression
#rest from hypothesis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##math_scores = np.array([85,90,78,92,88])
##science_scores = np.array([80,85,88,92,86])
##df=pd.DataFrame({'Math':math_scores,'Science':science_scores})
##print(df.describe())
##cov_matrix = df.cov()
##print("Covariance Matrix:\n",cov_matrix) #both variable must be numerical
##corr_matrix = df.corr()
##print("\nCorrelation Matrix:\n",corr_matrix) #one of them can be categorical 
##print(df.describe())

#Sample size (/n-1)
#Population size (/n)
#Best fit - Good Accuracy - above 70 % 
#Avg fit - Avg Accuracy - 50 - 70 %
#Worst fit - Bad Accuracy - below 50 %

#Data Analysis and Machine Learning not possibe for population size, way too much attributes

#Simulations- 1st parameter = Sample Test
            #  2nd = Train & Test
            #  3rd = K / Cluster
            
#Sample Dataset
data = np.array([1,2,2,2,3,3,4,5,5,5,6,6,6,6,7,8,8,9,27])
data1 = pd.DataFrame(data)
print(data1.describe())

#1. IQR Method (small dataset, if dataset not normal)
Q1 = np.percentile(data,25)#can use different percents say 55 too, though not needed only for viva
Q3 = np.percentile(data,75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = data[(data < lower_bound) | (data > upper_bound)]
print(outliers_iqr)

#2. Z- Score Method (Using sample standard dev) - (bulky dataset, if dataset normal)
mean = np.mean(data)
std_dev = np.std(data, ddof = 1) # use sample standard dev
z_scores = (data-mean)/ std_dev
outliers_z = data[np.abs(z_scores) > 3] # Outliers : Z>3 or Z<3
print(outliers_z)

#3. Box Plot Visualization
plt.figure(figsize=(6,4))
plt.boxplot(data,vert=False)
plt.xlabel("Values")
plt.title("Box Plot for Outlier Detection")
plt.show()


























































































