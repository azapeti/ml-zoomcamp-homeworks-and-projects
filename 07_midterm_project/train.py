#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import xgboost as xgb
import pickle
from sklearn.metrics import roc_auc_score


output_file = f'model_1.bin'


#data preparation

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')




df = pd.concat([train, test])




df.columns = df.columns.str.lower().str.replace(' ', '_')




categorical_cols = list(df.dtypes[df.dtypes == 'object'].index)
categorical_cols.remove('attrition')




for c in categorical_cols:
    df[c] = df[c].str.lower().str.replace(' ', '_')



df.attrition = (df.attrition == 'Left').astype(int)




numerical_cols = list(df.dtypes[df.dtypes != 'object'].index)
numerical_cols.remove('employee_id')
numerical_cols.remove('attrition')
numerical_cols


from sklearn.model_selection import train_test_split


df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)



y_train = df_train.attrition.values
y_test = df_test.attrition.values



from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)


#training

train_dicts = df_train[categorical_cols + numerical_cols].to_dict(orient='records')
test_dicts = df_test[categorical_cols + numerical_cols].to_dict(orient='records')

X_train = dv.fit_transform(train_dicts)
X_test = dv.transform(test_dicts)


features = list(dv.get_feature_names_out())


dtrain = xgb.DMatrix(X_train, label = y_train, feature_names = features)
dtest = xgb.DMatrix(X_test, label = y_test, feature_names = features)



xgb_params = {
    'eta': 0.3,
    'max_depth': 6,
    'min_child_weight': 1,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    
    'seed': 1,
    'verbosity': 2
}

model = xgb.train(xgb_params, dtrain, num_boost_round=30)

y_pred = model.predict(dtest)




auc = roc_auc_score(y_test, y_pred)
print(f'auc = {auc}')


output_file = f'model_1.bin'


with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')

