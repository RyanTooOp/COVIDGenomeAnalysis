#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:11:26 2020

@author: guanhuali
"""

import pandas as pd
import numpy as np
import seaborn as sns
import sklearn.model_selection as ms
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
features = pd.read_csv('../../Downloads/data1.csv')

features= features.drop('Participant', axis = 1)
features = features.drop('ID',axis = 1)
features = features.drop('Date', axis = 1)
labels = np.array(features['label'])
y = []
for x in range(len(labels)):
    if labels[x] == 'Yes':
        y.append(1)
    else:
        y.append(0)
y = np.array(y)

#labels = pd.get_dummies(labels)
#features = pd.get_dummies(features)
features= features.drop('label', axis = 1)
features = np.array(features)

modified = []

for col in features:
    temp = []
    for x in range(len(col)):
        if col[x] == 'Yes':
            temp.append(1)
        elif col[x] == 'No':
            temp.append(0)
        else:
            temp.append(0)
    modified.append(temp)

x = np.array(modified)
#print(x.shape,y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=62)

NN_model = MLPClassifier(solver='adam', activation='relu', hidden_layer_sizes=(42, 2), random_state=1000)

NN_model.fit(x_train, y_train)
pred_y = NN_model.predict(x)

ac = (y == pred_y).sum() / y.size
print('accuracy ac=', ac)


m = sm.confusion_matrix(y, pred_y)
print('confusion matrix：', m, sep='\n')


r = sm.classification_report(y, pred_y)
print('Overall Report：', r, sep='\n')


C2= sm.confusion_matrix(y, pred_y, labels=[0, 1])
sns.heatmap(C2,annot=True)
plt.show()
