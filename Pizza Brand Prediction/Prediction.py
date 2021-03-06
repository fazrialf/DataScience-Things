#Created by Fazrial Feizal
#For Educational Purposes Only

#Importing Libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#Loading Data
dataset = pd.read_csv('Pizza.csv', header=0)
x = dataset.iloc[:,1:8].values
y = dataset['Brand'].values

#Modelling
model = KNeighborsClassifier(n_neighbors = 7, )
model.fit(x, y)

#Inputing the variable value
mois = input("Input kadar Moisture? ")
prot = input("Input kadar Protein? ")
fat = input("Input kadar Lemak? ")
ash = input("Input kadar Ash? ")
sodium = input("Input kadar Sodium? ")
carb = input("Input kadar Karbohidrat? ")
cal = input("Input kadar Kalsium? ")

moisData = float(mois)
protData = float(prot)
fatData = float(fat)
ashData = float(ash)
sodiumData = float(sodium)
carbData = float(carb)
calData = float(cal)

#Predicting
prediction = model.predict([[moisData, protData, fatData, ashData, sodiumData, carbData, calData]])
print('Prediction : ' + prediction)
