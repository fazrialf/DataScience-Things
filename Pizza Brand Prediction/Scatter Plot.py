#Created by Fazrial Feizal
#For Educational Purposes Only

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loading Data
data = pd.read_csv('Pizza.csv')

#Plotting
plt.figure(figsize=(8,8))
sns.scatterplot(x='mois', y='carb', hue='Brand', data=data).set_title('Mois vs Cab')
plt.legend(loc='best')

plt.figure(figsize=(8,8))
sns.scatterplot(x='fat', y='ash', hue='Brand', data=data).set_title('Fat vs Ash')
plt.legend(loc='best')
