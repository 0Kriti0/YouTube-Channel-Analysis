##ca1 series is a collection of one d array

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
iris = sns.load_dataset("iris")
print(iris.info())

###incase the iris variable is found to be not a dataframe after info function checking, then convert it to a dataframe using iris=pd.DataFrame("iris")
##
####BAR diagram
###matplotlib
##species_count = iris["species"].value_counts()
##plt.figure()
##plt.bar(species_count.index,species_count.values)
##plt.title("Species Count(Metplotlib)")
##plt.xlabel("Species")
##plt.ylabel("Count")
##plt.show()
##
####plt.text(#,#,#)
###seaborn
##
##plt.figure()
##sns.countplot(x="species",data=iris)
##plt.title("Species Count (Seaborn)")
##plt.show()
##
####LINE diagram, used for showing forecast or predictions or trends using date, time etc or in terms of time series (continuosly changing data with respect to time.
##
##mean_sepal = iris.groupby("species")["sepal_length"].mean()
###matplotlib
##plt.figure()
##plt.plot(mean_sepal.index,mean_sepal.values,marker="o")
##plt.title("Mean Sepal Length by Species ")
##plt.xlabel("Species")
##plt.ylabel("Sepal Length")
##plt.show()
###seaborn
##plt.figure()
##sns.lineplot(x="species",y="sepal_length",data=iris,estimator="mean")
##plt.title("Mean Sepal Length by Species ")
##plt.show()
##
####HISTOGRAM
###metplotlib
##plt.figure()
##plt.hist(iris["sepal_length"],bins= 10 )#bins value is default 
##plt.title("Sepal Length Distribution")
##plt.xlabel("Sepal Length")
##plt.ylabel("Frequency")
##plt.show()
###seaborn
##plt.figure()
##sns.histplot(iris["sepal_length"],bins=10,kde=True)#kerneldensityestimator
##plt.title("Sepal Length Distribution")
##plt.show()
##
####Pie Chart
###matplotlib
##plt.figure()
##plt.pie(species_count,labels=species_count.index,autopct="%1.1f%%")
##plt.title("Species Distribution")
##plt.show()

####Scatter Plot
###matplotlib
##plt.figure()
##plt.scatter(iris["sepal_length"],iris["petal_length"])
##plt.title("Sepal Length vs Petal Length")
##plt.xlabel("Sepal Length")
##plt.ylabel("Petal Length")
##plt.show()
##
###seaborn
##plt.figure()
##sns.scatterplot(x= "sepal_length",y="petal_length",hue="species",data=iris)#example display ---- wise find the relationship between --- and --- , in this ---- is species and ---s are sepallength and petallength
##plt.title("Sepal Length vs Petal Length")
##plt.show()
##
####Pair Plot
##sns.pairplot(iris, hue="species")
##plt.show()
##
####Heat Map #correlation between numerical as well as catagorical in numbers 
###matplotlib
##corr = iris.corr(numeric_only = True)#numeric_only is optional 
##plt.imshow(corr)
##plt.colorbar()
##plt.xticks(range(len(corr.columns)),corr.columns, rotation = 45)
##plt.yticks(range(len(corr.columns)),corr.columns)
##plt.title("Correlation Heatmap")
##plt.show()
##
###seaborn
##plt.figure()
##sns.heatmap(corr, annot = True)
##plt.title("Correlation Heatmap")
##plt.show()

#Box plot
#matplotlib
iris.boxplot(column="sepal_length",by="species")
plt.title("Sepal Length by Species")
plt.suptitle("")
plt.show()

#seaborn
plt.figure()
sns.boxplot(x="species",y="sepal_length",data =iris)
plt.title("Sepal Length by Species")
plt.show()

