# -*- coding: utf-8 -*-
"""big_mart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-IHitTpPmnrn6CB21aTHDfG0jlF-1KRK
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print(train.head())
print(test.head())

train.isnull().sum()

def data_prep(train):
  train['Item_Weight'] = np.where(train['Item_Weight'].isna(),train['Item_Weight'].median(skipna = True),train['Item_Weight'])
  train['Outlet_Size'] = np.where(train['Outlet_Size'].isna(),train['Outlet_Size'].mode()[0], train['Outlet_Size'])
  train['Item_Fat_Content'] = train['Item_Fat_Content'].replace('low fat', 'Low Fat')
  train['Item_Fat_Content'] = train['Item_Fat_Content'].replace('LF', 'Low Fat')
  train['Item_Fat_Content'] = train['Item_Fat_Content'].replace('reg', 'Regular')
  train['YOB'] = 2023 - train['Outlet_Establishment_Year']
  return train

train_new = data_prep(train)

train_new.isnull().sum()

train_new.drop(['Item_Identifier', 'Item_Fat_Content', 'Item_Type', 'Outlet_Identifier', 'Outlet_Establishment_Year', 'Outlet_Type', 'Outlet_Location_Type', 'Outlet_Size'], inplace=True, axis=1)
train_new

y = train_new['Item_Outlet_Sales']
x = train_new.drop(['Item_Outlet_Sales'], axis = 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 15)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

lr = LinearRegression()
lr.fit(x_train, y_train)
lr_train = lr.predict(x_train)
lr_test = lr.predict(x_test)

#Lets define a function for Model Evaluation
def model_eval(actual, predicted):
  rmse = np.sqrt(mean_squared_error(actual, predicted))
  r2 = r2_score(actual, predicted)
  print('The RMSE value for the model is: ', round(rmse,2))
  print('The R2 Score for the model is: ', round(r2, 2))

model_eval(y_train, lr_train)

model_eval(y_train, lr_train)

# random forest
rf = RandomForestRegressor()
rf.fit(x_train, y_train)

rf_preds_train = rf.predict(x_train)
rf_preds_test = rf.predict(x_test)

model_eval(y_train, rf_preds_train)

model_eval(y_test, rf_preds_test)

