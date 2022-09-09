import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler 
from sklearn import metrics
data = pd.read_csv('D:\graduation_project\csv_files\Default_Fin.csv')
print(data.head())
data.info()
y= data['Defaulted?']
data = data.drop('Defaulted?',axis=1)
st= StandardScaler()
x= st.fit_transform(data)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state=50,stratify=y)
model=LogisticRegression()
model.fit(x_train, y_train)  
test_pred = model.predict(x_test)
train_pred = model.predict(x_train)
print("test score =",metrics.accuracy_score(test_pred,y_test))
print("train score =",metrics.accuracy_score(train_pred,y_train))