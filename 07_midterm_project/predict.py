import pickle

import xgboost as xgb

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model_1.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])

def predict():
    employee = request.get_json()
    
    employee_transformed = dv.transform([employee])
    feature_names = list(dv.get_feature_names_out())
    X_employee = xgb.DMatrix(employee_transformed, feature_names=feature_names)
    y_pred = model.predict(X_employee)
    
    attrition = y_pred >= 0.5
    
    result = {
        'attrition_probability': float(y_pred[0]),
        'attrition': bool(attrition[0])
    }
    
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)