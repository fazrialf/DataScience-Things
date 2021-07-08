#Created by Fazrial Feizal
#For Educational Purposes Only

#Importing Libraries
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

#Loading Data
irisDataset = pd.read_csv('assets\iris.csv')

#Ploting The Dispersion
sns.scatterplot(x='sepals-length', y='sepals-width', hue='label', data=irisDataset).set_title('Sebaran Data Iris')
plt.figure(1)
plt.show()