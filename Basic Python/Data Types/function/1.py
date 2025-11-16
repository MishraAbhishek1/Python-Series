def predict_disease(patient_data):
    
    result = model.predict(patient_data)
    return result