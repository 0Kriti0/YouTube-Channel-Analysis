#Unit 6
#Machine Learning -> Supervised -> ((i/p-numerical/Text/Audio/Video/Image, o/p - categorical)) Classification (if output is categorical)
                            #   ->KNN,NB,DT,SUM,NN,RF,Logistic regression
                            
#                               ->((i/p,o/p- Numerical)) Regression (if output is numerical)
#                               ->Simple linear regression, Multiple linear reg, Polynomial reg

#                 -> Unsupervised
                # -> K means,  H-Clustering

#Reinforcement not used in machine learning bcz you have to start again and again
#In ai rules are alaways known when it comes to supervised and unsupervised learning, Strong ai
#In ml rules are not known , Weak ai

#Input is called as feature, independent variable , input must be independent if they are not they are multicoliniarity which can hamper our data
#Output is called as label, dependent variable

#6CRISPDM
#Buisness Understanding
#Data Understanding
#Data Preprocessing - EDA
#Modelling -> Classification -> Accuracy
        #  -> Regression -> Error/R^2

#Evaluation
#Deployment



#/*
##df = pd.read_csv("ABC.csv")
###EDA
##print(df.info())
##print(df.describe())
##print(df.isnull().sum())
##print(sns.histogram()) #Only apply if there were outliers in the boxplot or if statistical is mentioned we need to use so as to find whelther data is normal or not and then aplly  z score or Iqr accordingly
##print(boxplot())
###|^ Statistical Analysis


#2.Inferential Analysis
#2.1
#x=df{'A'] or df[['A','B','C','D']] or iloc or loc (iloc 0:n-1,loc 0:n)
#y=df['B']
#2.2
#Train & Test
#2.3
#Model
#a = LinearRegression()
#a.fit() example say y= mx+c
#y_pred = a.predict()
#2.4
#Performance Measure
#MAE = say example 20-18
#MSE
#R^2
#2.5
#Visualization
#*/

##x = np.array([1,2,3,4,5]) #feature
##y= np.array([3,4,2,4,5]) #label
##x= x.reshape(-1,1)
##model = LinearRegression()
##model.fit(x,y)
##y_pred = model.predict(x)
##mse = mean_squared_error(y,y_pred)
##r_sq=r2_score(y,y_pred)
##print(mse,r_sq)

#/*##for provided not random selection , ex first 100 train last 50 for test
###x_train=x.iloc[0:100,:]
###x_test = x.iloc[101:151,:]*/ Hypothetically this is wrong 


#model = LinearRegression()
#model.fit(x_train,y_train)
#y_pred(x_test)
#Evaluation(y_test)
#plot()
##
        
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[500],[750],[1000],[1250],[1500],[1750],[2000],[2250],[2500]])
y = np.array([150,200,250,275,300,325,350,375,400])
X_train,X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2,random_state=42)

#model
model = LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

#error
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print(mse)
print(r2)
print(f"Intercept:{model.intercept_:.2f}")
print(f"Coefficient:{model.coef_[0]:.2f}")

#Plotting the results
plt.scatter(X,y,color = 'blue' , label = 'Actual Data')
plt.plot(X,model.predict(X), color = 'red' , linewidth = 2 , label = 'Regression Line')
plt.xlabel("House Size(sq ft)")
plt.ylabel("Price ($1000s)")
plt.title("Linear Regression: House Size vs. Price")
plt.legend()
plt.grid(True)
plt.show()

a= np.array([[3500]])
predicted_price = model.predict(a)
print(predicted_price)

            

##import pandas as pd
##from statsmodels.stats.outliers_influence 
