# -*- coding: utf-8 -*-
"""pca_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sxo8LEuTz0C3tX5-WMi3kjYKtC4eJ4gY
"""

import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
feature_names = iris.feature_names
y = iris.target
df = pd.DataFrame(data,columns=feature_names)
df["sinif"] = y
x = data
from sklearn.decomposition import PCA
pca = PCA(n_components=2, whiten=True)
pca.fit(x)
x_pca = pca.transform(x)
print("variance ratio",pca.explained_variance_ratio_)
print("sum",sum(pca.explained_variance_ratio_))

print(df)

df["p1"] = x_pca[:,0]
df["p2"] = x_pca[:,1]

color = ["red","blue","green"]

import matplotlib.pyplot as plt
for each in range(3):
  plt.scatter(df.p1[df.sinif==each],df.p2[df.sinif==each],color=color[each],label=iris.target_names[each])

plt.legend()
plt.xlabel("p1")
plt.ylabel("p2")
plt.show()