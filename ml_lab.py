# -*- coding: utf-8 -*-
"""ML LAB(BE).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A2vJst99-bU_hKjrI2VdGDEoUaQiUK3p
"""

# Commented out IPython magic to ensure Python compatibility.
# %%html
# <marquee style='width: 55%; color: blue;'><b> Machine Learning Lab by Dr.T.Bhaskar  !</b></marquee>

"""# **ASSIGNMENT-1:SIMPLE LINEAR REGRESSION**

"""

#STEP-1: Import Libraries
# Code to read csv file into colaboratory:
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

#STEP-2: Autheticate E-Mail ID
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

## IMPORT CSV FILES FROM DRIVE INTO GOOGLE-COLAB
downloaded = drive.CreateFile({'id':'1ORTNkZgo6uc5VSYopHxl787fPdrs7-LT'}) # replace the id with id of file you want to access
downloaded.GetContentFile('SLR-Data.csv')
#https://drive.google.com/file/d/1ORTNkZgo6uc5VSYopHxl787fPdrs7-LT/view?usp=sharing

#installation of python libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = pd.read_csv('SLR-Data.csv')
print(data.shape)
print(data.head())
#print(data.describe())

# Collecting X and Y
X = data['No of Hours Spent During(X)'].values
Y = data['Risk Score on a scale of 0-100(Y)'].values

# Calculate Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)
#print(mean_x)
#print(mean_y)
# Total number of values
m = len(X)
# Using the formula to calculate b1(slope) and b0(intercept)
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# Print coefficients:b1,b0
print("Slope,Intercept:",b1,b0)

# Plotting Values and Regression Line
max_x = np.max(X)
min_x = np.min(X)

# Calculating line values x and y
x = np.linspace(min_x, max_x)
y = b0 + b1 * x

# Ploting Line
plt.plot(x, y, color='green', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='blue', label='Scatter Plot')
plt.xlabel('No of Hours Spent During')
plt.ylabel('Risk Score on a scale of 0-100')
plt.legend()
plt.show()

#For  Calculating Root Mean Squares Error
rmse = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/m)
print("Root Mean Squares Error:",rmse)
# Calculating Accuracy Score
ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print("Accuracy:",r2*100)
#predicting a o/p (y) for new value of x
predict_x=int(input('Enter No Hours Spent in Driving:'))
predict_y=(4.58789861*predict_x)+12.584627964022907
plt.scatter(X,Y)
plt.scatter(predict_x,predict_y)
plt.xlabel('No Hours Spent Driving(Predicted_x)')
plt.ylabel('Risk Score on a Scale of 0-100(Predicted_y)')
 #plotting the regression line
plt.scatter(X, Y, c='blue')
plt.plot(x, y, color='green')
# function to show plot
plt.show()

#Home Assignment Height & Weight Problem

downloaded = drive.CreateFile({'id':'1e10Ynfgrc35FtMl2V5qpzTGyuWF4KQsZ'}) # replace the id with id of file you want to access
downloaded.GetContentFile('hw.csv')

#Read file Height & Weight csv as panda dataframe
import pandas as pd
xyz = pd.read_csv('hw.csv')
print(xyz.head(5))

#Running Height & Weight Program(SLR)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
dataset=pd.read_csv("hw.csv")
# To display dataset
print(dataset)
x=dataset.iloc[:,:-1].values
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
print(X)
print(y)
#from sklearn subpackage import linear regression model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
#To get the slop
regressor.coef_
#To get the y intercept
regressor.intercept_
#To print the equation of line
print("y= "+ str(regressor.coef_) + "X + " + str(regressor.intercept_))

#To get the slop
print("Accuracy:",regressor.score(X,y)*100)
#To plot graph
plt.plot(X,y,'o')
plt.plot(X,regressor.predict(X));
plt.show()
predict_x=int(input('Enter Height:'))
predict_y=(0.67461045*predict_x)-38.45508707607698
plt.scatter(X,y)
plt.scatter(predict_x,predict_y)
plt.xlabel('Enter Height:(Predicted_x)')
plt.ylabel('Enter Weight:(Predicted_y)')
#plotting the Predicted regression line
plt.plot(X,regressor.predict(X),color='green');
plt.show()

"""#**ASSIGNMENT -2:Principal Component Analysis for feature reduction**

"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# %matplotlib inline

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url
                 , names=['sepal length','sepal width','petal length','petal width','target'])
df.head()
#downloaded = drive.CreateFile({'id':'12BY34aCbYLoLjy3gDUMrZEBUf7l5FZsd'}) # replace the id with id of file you want to access
#downloaded.GetContentFile('iris.csv')
#dataset=pd.read_csv("iris.csv")
#dataset
#https://drive.google.com/file/d/12BY34aCbYLoLjy3gDUMrZEBUf7l5FZsd/view?usp=share_link

"""**Standardize the Data**

Since PCA yields a feature subspace that maximizes the variance along the axes, it makes sense to standardize the data, especially, if it was measured on different scales. Although, all features in the Iris dataset were measured in centimeters, let us continue with the transformation of the data onto unit scale (mean=0 and variance=1), which is a requirement for the optimal performance of many machine learning algorithms.
"""

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values

y = df.loc[:,['target']].values

x = StandardScaler().fit_transform(x)

pd.DataFrame(data = x, columns = features).head()

#PCA Projection to 2D
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
principalDf.head(5)

df[['target']].head()

finalDf = pd.concat([principalDf, df[['target']]], axis = 1)
finalDf.head(5)

"""**Visualize 2D Projection**"""

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)


targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

#Explained Variance:The explained variance tells us how much information (variance)
#can be attributed to each of the principal components.
pca.explained_variance_ratio_

"""Together, the first two principal components contain 95.80% of the information. The first principal component contains 72.77% of the variance and the second principal component contains 23.03% of the variance. The third and fourth principal component contained the rest of the variance of the dataset.

# **ASSIGNMENT-3: Decision Tree**
"""

downloaded = drive.CreateFile({'id':'1jql2mwV15BCFeX52G1PGSCr8Y4jLdn8f'}) # replace the id with id of file you want to access
downloaded.GetContentFile('DT-Data.csv')

#import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading Dataset
dataset=pd.read_csv("DT-Data.csv")
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,5].values

#Perform Label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()

X = X.apply(LabelEncoder().fit_transform)
print (X)

from sklearn.tree import DecisionTreeClassifier
regressor=DecisionTreeClassifier()
regressor.fit(X.iloc[:,1:5],y)

#Predict value for the given expression
X_in=np.array([0,1,0,1])

y_pred=regressor.predict([X_in])
print ("Prediction:", y_pred)

from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
# Create DOT data
dot_data = StringIO()

export_graphviz(regressor, out_file=dot_data, filled=True, rounded=True, special_characters=True)
# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Decision_Tree.png')
# Show graph
Image(graph.create_png())

"""# **ASSIGNMENT-4:Naive Bayes**"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

#from sklearn.datasets import load_iris
#dataset = load_iris()
#dataset
downloaded = drive.CreateFile({'id':'12BY34aCbYLoLjy3gDUMrZEBUf7l5FZsd'}) # replace the id with id of file you want to access
downloaded.GetContentFile('iris.csv')
dataset=pd.read_csv("iris.csv")
dataset
#https://drive.google.com/file/d/12BY34aCbYLoLjy3gDUMrZEBUf7l5FZsd/view?usp=share_link
#from sklearn.datasets import load_iris
#dataset = load_iris()
#dataset
downloaded = drive.CreateFile({'id':'12BY34aCbYLoLjy3gDUMrZEBUf7l5FZsd'}) # replace the id with id of file you want to access
downloaded.GetContentFile('iris.csv')
dataset=pd.read_csv("iris.csv")
dataset
#https://drive.google.com/file/d/12BY34aCbYLoLjy3gDUMrZEBUf7l5FZsd/view?usp=share_link

#Spliting the dataset in independent and dependent variables
X = dataset.iloc[:,:4].values
y = dataset['variety'].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 82)

# Feature Scaling to bring the variable in a single scale
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Naive Bayes Classification to the Training set with linear kernel
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#finding accuracy from the confusion matrix.
a = cm.shape
corrPred = 0
falsePred = 0

for row in range(a[0]):
    for c in range(a[1]):
        if row == c:
            corrPred +=cm[row,c]
        else:
            falsePred += cm[row,c]
print('Correct predictions: ', corrPred)
print('False predictions', falsePred)
print ('\n\nAccuracy of the Naive Bayes Clasification is: ', corrPred/(cm.sum()))

"""# **Assignment-5:SVM**
Predict if cancer is Benign or malignant. Using historical data about patients diagnosed with cancer enables doctors to differentiate malignant cases and benign ones are given independent attributes.
"""

# Load the important packages
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC

# Load the datasets
cancer = load_breast_cancer()
X = cancer.data[:, :2]
y = cancer.target

#Build the model
svm = SVC(kernel="linear")
# Trained the model
svm.fit(X, y)

# Plot Decision Boundary
DecisionBoundaryDisplay.from_estimator(
		svm,
		X,
		response_method="predict",
		cmap=plt.cm.Spectral,
		alpha=0.8,
		xlabel=cancer.feature_names[0],
		ylabel=cancer.feature_names[1],
	)

# Scatter plot
plt.scatter(X[:, 0], X[:, 1],
			c=y,
			s=20, edgecolors="k")
plt.show()

#Build the model
svm = SVC(kernel="rbf", gamma=0.5, C=1.0)
# Trained the model
svm.fit(X, y)

# Plot Decision Boundary
DecisionBoundaryDisplay.from_estimator(
		svm,
		X,
		response_method="predict",
		cmap=plt.cm.Spectral,
		alpha=0.8,
		xlabel=cancer.feature_names[0],
		ylabel=cancer.feature_names[1],
	)

# Scatter plot
plt.scatter(X[:, 0], X[:, 1],
			c=y,
			s=20, edgecolors="k")
plt.show()

"""# **ASSIGNMENT-6:KMeans-Assignment**"""

#import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#create dataset using DataFrame
df=pd.DataFrame({'X':[0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3],
                 'y':[0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]})
f1 = df['X'].values
f2 = df['y'].values
X = np.array(list(zip(f1, f2)))
print(X)

#centroid points
C_x=np.array([0.1,0.3])
C_y=np.array([0.6,0.2])
centroids=C_x,C_y

#plot the given points
colmap = {1: 'r', 2: 'b'}
plt.scatter(f1, f2, color='k')
plt.show()

#for i in centroids():
plt.scatter(C_x[0],C_y[0], color=colmap[1])
plt.scatter(C_x[1],C_y[1], color=colmap[2])
plt.show()

C = np.array(list((C_x, C_y)), dtype=np.float32)
print (C)

#plot given elements with centroid elements
plt.scatter(f1, f2, c='#050505')
print("point No.6[0.25,0.5] is belongs to blue cluster(cluster no:2)")
plt.scatter(C_x[0], C_y[0], marker='*', s=200, c='r')
plt.scatter(C_x[1], C_y[1], marker='*', s=200, c='b')
plt.show()


#import KMeans class and create object of it
from sklearn.cluster import KMeans
model=KMeans(n_clusters=2,random_state=0)
model.fit(X)
labels=model.labels_
print(labels)

#using labels find population around centroid
count=0
for i in range(len(labels)):
    if (labels[i]==1):
        count=count+1

print('No of population around cluster 2:',count-1)

#Find new centroids
new_centroids = model.cluster_centers_

print('Previous value of m1 and m2 is:')
print('M1==',centroids[0])
print('M1==',centroids[1])

print('Updated value of m1 and m2 is:')
print('M1==',new_centroids[0])
print('M1==',new_centroids[1])

#STEP-1: Import Libraries
# Code to read csv file into colaboratory:
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

#STEP-2: Autheticate E-Mail ID
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

#STEP-3: Get File from Drive using file-ID

downloaded = drive.CreateFile({'id':'1e10Ynfgrc35FtMl2V5qpzTGyuWF4KQsZ'}) # replace the id with id of file you want to access
downloaded.GetContentFile('hw.csv')

"""# **Assignment-7:Gradient Boost Classifier**

# **Implementation Using scikit-learn**
For implementation on a dataset, we will be using the Income Evaluation dataset, which has information about an individual’s personal life and an output of 50K or <=50. The dataset can be found here (https://www.kaggle.com/lodetomasi1995/income-classification)

The task here is to classify the income of an individual, when given the required inputs about his personal life.

First, let’s import all required libraries.
"""

# Import all relevant libraries

from sklearn.ensemble import GradientBoostingClassifier

import numpy as np

import pandas as pd

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn import preprocessing

import warnings

warnings.filterwarnings("ignore")

#STEP-1: Import Libraries
# Code to read csv file into colaboratory:
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

#STEP-2: Autheticate E-Mail ID
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Get File from Drive using file-ID
downloaded = drive.CreateFile({'id':'1zI-X3zdiuM9u74zQyKIShvAUtPJQ7jUK'}) # replace the id with id of file you want to access
downloaded.GetContentFile('income_evaluation.csv')
# https://drive.google.com/file/d/1zI-X3zdiuM9u74zQyKIShvAUtPJQ7jUK/view?usp=sharing  (Dataset Downloads Link)

#Now let’s read the dataset and look at the columns to understand the information better.
#https://drive.google.com/file/d/1zI-X3zdiuM9u74zQyKIShvAUtPJQ7jUK/view?usp=sharing
df = pd.read_csv('income_evaluation.csv')
df.head()

"""**Here my main aim is to tell you how to implement this on python. Now for training and testing our model, the data has to be divided into train and test data.**
We will also scale the data to lie between 0 and 1.
"""

df.shape

df.info()

df.isnull().sum()

df.columns

#df.drop(columns=' fnlwgt',inplace=True)
df.columns

X = df.drop(columns=' income')
y = df[' income']

from sklearn.preprocessing import LabelEncoder

def label_encoder(a):
    le = LabelEncoder()
    df[a] = le.fit_transform(df[a])

df.columns

label_list = [' workclass', ' education',' marital-status',
       ' occupation', ' relationship', ' race', ' sex',' native-country', ' income']

for i in label_list:
    label_encoder(i)

df.head()

from sklearn.model_selection import train_test_split

X = df.drop([' income'],axis=1).values   # independant features
y = df[' income'].values					# dependant variable

# Choose your test size to split between training and testing sets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

print("X_train shape:",X_train.shape)
print("y_test shape:",y_test.shape)
print("X_test shape:",X_test.shape)
print("y_train shape:",y_train.shape)

#Buildimg Gradient Boosting Model
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

gradient_booster = GradientBoostingClassifier(learning_rate=0.1)
accuracies = cross_val_score(gradient_booster, X_train, y_train, cv=5)
gradient_booster.fit(X_train,y_train)

print("Train Score:",np.mean(accuracies))
print("Test Score:",gradient_booster.score(X_test,y_test))

result_dict_train = {}
result_dict_test = {}
result_dict_train["Gradient-Boost Default Train Score"] = np.mean(accuracies)
result_dict_test["Gradient-Boost Default Test Score"] = gradient_booster.score(X_test,y_test)

grid = {
    'learning_rate':[0.01,0.05,0.1],
    'n_estimators':np.arange(100,500,100),
}

gb = GradientBoostingClassifier()
gb_cv = GridSearchCV(gb, grid, cv = 4)
gb_cv.fit(X_train,y_train)
print("Best Parameters:",gb_cv.best_params_)
print("Train Score:",gb_cv.best_score_)
print("Test Score:",gb_cv.score(X_test,y_test))

result_dict_train
result_dict_test

"""# **Extra Assignment:KNN**"""

downloaded = drive.CreateFile({'id':'1oikTU46hEkvGW_DeFyWos5_6q3cX6h7B'}) # replace the id with id of file you want to access
downloaded.GetContentFile('knndata.csv')

#Importing Libraries

import numpy as np
import pandas as pd

# To split dataset into its attributes and labels.

dataset=pd.read_csv("knndata.csv")
X=dataset.iloc[:,:-1].values
print(X)
Y=dataset.iloc[:,2].values
print(Y)

# Training of KNN Classification Model using trained data

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,Y)

# Testing  KNN Classification Model using unseen test data

X_test=np.array([6,6])
y_pred = classifier.predict([X_test])
print ('The predicition of classifier is :', y_pred)
classifier = KNeighborsClassifier(n_neighbors=3,weights='distance')
classifier.fit(X,Y)
# predict the class for points(6,6)
X_test=np.array([6,6])
y_pred = classifier.predict([X_test])
print ('The predicition of classifier is :', y_pred)
























### **1. Linear Regression**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv('linear_regression.csv')
X = data.iloc[:, 0].values  # Assuming first column is hours
y = data.iloc[:, 1].values  # Assuming second column is risk

# Linear Regression
coeff = np.polyfit(X, y, 1)
line_eq = f"y = {coeff[0]:.2f}x + {coeff[1]:.2f}"

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, np.polyval(coeff, X), color='red')
plt.title(f"Best Fit Line: {line_eq}")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()
```

---

### **2. PCA for Feature Reduction**
```python
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv('pca_data.csv')
X = data.iloc[:, :-1].values

# PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Plot
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=data.iloc[:, -1].values, cmap='viridis')
plt.title("PCA - Reduced to 2 Components")
plt.show()
```

---

### **3. Decision Tree Classifier**
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Load Data
data = pd.read_csv('decision_tree.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Train Model
clf = DecisionTreeClassifier().fit(X, y)

# Predict for test data
test = [[20, 30, 0, 1]]  # Example test input
decision = clf.predict(test)[0]

# Decision Tree
tree = export_text(clf, feature_names=data.columns[:-1])
print(tree, "\nDecision:", decision)
```

---

### **4. Naive Bayes Classification**
```python
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# Load Data
data = pd.read_csv('naive_bayes.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Model
nb = GaussianNB().fit(X, y)
accuracy = nb.score(X, y)

print(f"Accuracy: {accuracy:.2f}")


### **5. SVM Classification**
```python
import pandas as pd
from sklearn.svm import SVC

# Load Data
data = pd.read_csv('svm_data.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Model
svm = SVC(kernel='linear').fit(X, y)
accuracy = svm.score(X, y)

print(f"Accuracy: {accuracy:.2f}")
```

---

### **6. K-Means Clustering**
```python
import pandas as pd
from sklearn.cluster import KMeans

# Load Data
data = pd.read_csv('kmeans_data.csv').values

# K-Means
kmeans = KMeans(n_clusters=2, init=data[:2, :], n_init=1).fit(data)

# Outputs
print(f"Cluster of P6: {kmeans.labels_[5]}")
print(f"Population of Cluster 2: {sum(kmeans.labels_ == 1)}")
print(f"Updated Centroids: {kmeans.cluster_centers_}")
```

---

### **7. Gradient Boost Classifier**
```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# Load Data
data = pd.read_csv('gradient_boost.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
gb = GradientBoostingClassifier().fit(X_train, y_train)
accuracy = gb.score(X_test, y_test)

print(f"Accuracy: {accuracy:.2f}")