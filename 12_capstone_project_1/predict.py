import pickle
import pandas as pd

from flask import Flask, request, jsonify

model_file = 'dt_model_01.bin'

with open(model_file, 'rb') as f_in:
    dt, le, scaler, oe = pickle.load(f_in)
    
app = Flask('drug')

@app.route('/predict', methods=['POST'])

def predict():
    patient_data = request.get_json()
    
    if isinstance(patient_data, dict):
        df = pd.DataFrame([patient_data])
    elif isinstance(patient_data, list):
        df = pd.DataFrame(patient_data)
    else:
        return jsonify({"error": "Input format not recognized"}), 400
    
    bp_order = ['low', 'normal', 'high']
    cholesterol_order = ['normal', 'high']
    
    X_oe = oe.transform(df[['bp', 'cholesterol']])
    X_oe_df = pd.DataFrame(X_oe, columns=['bp', 'cholesterol'])
    
    X_numeric = df[['age', 'na_to_k']]   
    X_num_standardized = scaler.transform(X_numeric)
    X_num_standardized = pd.DataFrame(X_num_standardized, columns=X_numeric.columns)
    
    X_encoded = pd.concat([X_num_standardized, X_oe_df], axis=1)
    
    y_pred_proba = dt.predict_proba(X_encoded)
    
    y_pred_class = dt.predict(X_encoded)
    
    y_pred_drug = le.inverse_transform(y_pred_class)
    
    
    results = []
    
    for i in range(len(df)):
        results.append({
            "predicted_drug": y_pred_drug[i],
            "class_probabilities": y_pred_proba[i].tolist()
        })
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
