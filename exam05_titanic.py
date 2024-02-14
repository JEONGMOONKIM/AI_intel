# -*- coding: utf-8 -*-
"""exam05_titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17AVz3mmREYb_2lYfkOtwT3TmJ6MOQVkQ
"""

import seaborn as sns
import pandas as pd
import numpy as np

raw_data=sns.load_dataset('titanic')
raw_data

raw_data.info()

raw_data.isnull().sum()

clean_data=raw_data.dropna(axis=1, thresh=500)

clean_data

clean_data.columns

test=raw_data[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive',
       'alone']]
test

mean_age=clean_data['age'].mean()
print(mean_age)

clean_data['age'].fillna(mean_age, inplace=True)
clean_data.head(10)

clean_data.drop(['embark_town', 'alive'], axis=1, inplace=True)

clean_data.info()

clean_data['embarked'].fillna(method='ffill', inplace=True)
clean_data['embarked'][825:830]

clean_data.isnull().sum()

clean_data.info()

clean_data['sex'].replace({'male':0, 'female':1}, inplace=True)
clean_data.info()

print(clean_data['sex'].unique())

print(clean_data['embarked'].unique())

from sklearn import preprocessing

label_encoder=preprocessing.LabelEncoder()
onehot_encoder=preprocessing.OneHotEncoder()

print(clean_data['embarked'].value_counts())

clean_data['embarked']=label_encoder.fit_transform(
    clean_data['embarked'])
print(clean_data['embarked'].unique())

print(clean_data['embarked'].value_counts())

clean_data.info()

clean_data['adult_male']=clean_data['adult_male'].astype('int64')
clean_data.info()

clean.data.head()

clean_data.head()

target=clean_data[['survived']]
target

training_data=clean_data.drop('survived', axis=1, inplace=False)
training_data.head()

value_data=training_data[['age', 'fare']]
training_data.head()

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaled_data=scaler.fit_transform(value_data)
value_data=pd.DataFrame(scaled_data, columns=value_data.columns)
value_data.head()

training_data.drop(['age', 'fare'], axis=1, inplace=True)
training_data.head()

onehot_data=pd.get_dummies(training_data['pclass'])
onehot_data.head()

onehot_data=pd.get_dummies(training_data, columns=training_data.columns)
onehot_data.head()

onehot_data.info()

training_data=pd.concat([value_data, onehot_data], axis=1)
training_data.info()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(
    training_data.astype('float64'), target, test_size=0.20)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model=Sequential()
model.add(Dense(128, input_dim=34, activation='relu'))
model.add(Dropout(0.02))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])

fit_hist=model.fit(
    x_train, y_train, batch_size=50, epochs=5, validation_split=0.2, verbose=1)

import matplotlib.pyplot as plt
plt.plot(fit_hist.history['binary_accuracy'])
plt.plot(fit_hist.history['val_binary_accuracy'])
plt.show()

score=model.evaluate(x_test, y_test, verbose=0)
print('loss', score[0])
print('accuracy', score[1])

