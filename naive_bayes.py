# -*- coding: utf-8 -*-
"""naive_bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AqM675_UTW-9m_KLJxTdoKsCGHzsN7nw
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv("/content/drive/MyDrive/data.csv")

data.head()
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)

data.tail()

M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]

plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha=0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="ıyı",alpha=0.3)
plt.xlabel("radius_mean(tümör yarıçapı)")
plt.ylabel("texture_mean(tümör dokusu)")
plt.legend()
plt.show()

data.diagnosis = [1 if each =="M" else 0 for each in data.diagnosis]

x_data= data.drop(["diagnosis"],axis=1)
y= data.diagnosis.values

x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data))

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train,y_train)

print("accuracy of svm algorithm: ",nb.score(x_test,y_test))