#!/usr/bin/env python
# coding: utf-8

import pickle

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE


output_file = 'model_1.bin'

df = pd.read_csv('drug200.csv')


    #### Preprocessing ####
df.columns = df.columns.str.lower() #.str.replace(' ', '_')
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)
df['drug'] = df['drug'].apply(lambda x: x[:-1] + '_' + x[-1])
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
numerical_columns = list(df.dtypes[df.dtypes != 'object'].index)

    #### Encoding ####
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, StandardScaler

X = df.drop(columns=['drug', 'sex'])
y = df['drug']


bp_order = ['low', 'normal', 'high']
cholesterol_order = ['normal', 'high']

oe = OrdinalEncoder(categories=[bp_order, cholesterol_order])

X_oe = oe.fit_transform(X[['bp', 'cholesterol']])
X_oe_df = pd.DataFrame(X_oe, columns=['bp', 'cholesterol'])

X_numeric = X[['age', 'na_to_k']]


scaler = StandardScaler()
X_num_standardized = scaler.fit_transform(X_numeric)
X_num_standardized = pd.DataFrame(X_num_standardized, columns=X_numeric.columns)



X_encoded = pd.concat([X_num_standardized, X_oe_df], axis=1)

le = LabelEncoder()

y_encoded = le.fit_transform(y)

    #### Upsampling with SMOTE ####


from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=1)

X_train_resamp, y_train_resamp = smote.fit_resample(X_encoded, y_encoded)


    #### Model ####
dt = DecisionTreeClassifier(
    random_state=1,
    max_depth=4
    )

dt.fit(X_train_resamp, y_train_resamp)


output_file = 'dt_model_01.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dt, le, scaler, oe), f_out)