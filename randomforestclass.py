# -*- coding: utf-8 -*-
"""RandomForestClass.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1maSavBTuLtoo89FyG4ZIICJtModcDIeD
"""

import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv("/content/drive/MyDrive/data.csv")
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)

data.dignosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)

x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.15, random_state=42)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
dt.fit(x_train, y_train)
print("decisiontree score: ",dt.score(x_test,y_test))

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(x_train,y_train)
print("random forest algo result", rf.score(x_test,y_test))