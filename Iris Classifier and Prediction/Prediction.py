#Created by Fazrial Feizal
#For Educational Purposes Only

#Importing Libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#Loading Data
irisDataset = pd.read_csv('assets\iris.csv', header = 0)
x = irisDataset.iloc[:, :2]
y = irisDataset.iloc[:, -1]

#Modelling and Fitting
n_neighbors = 6
model = KNeighborsClassifier(n_neighbors, weights='distance')
model.fit(x, y)

#Predicting
length = float(input('Masukkan Panjang Sepal (cm) : '))
width = float(input('Masukkan Lebar Sepal (cm) : '))
prediction = model.predict([[length, width]])
print('Prediction : ' + prediction)
