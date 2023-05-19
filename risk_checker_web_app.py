# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model.pkl', 'rb'))

# Create application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('webb-app.html')

@app.route('/predict', methods=['POST'])
def predict():
# Retrieve form data
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    cp = float(request.form['cp'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    fbs = float(request.form['fbs'])
    restecg = float(request.form['restecg'])
    thalach = float(request.form['thalach'])
    exang = float(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = float(request.form['slope'])
    ca = float(request.form['ca'])
    thal = float(request.form['thal'])

    features = np.array([[age, sex, cp, 
                          trestbps, chol, fbs, 
                          restecg, thalach, exang, 
                          oldpeak, slope, ca, thal]])
    prediction = model.predict(features)
    if prediction == 1:
        result = 'You have a lower risk of having heart disease'
    else:
        result = 'You are at a higher risk of having heart disease'

    return render_template('webb-app.html', result=result)

if __name__ == 'main':
# Run the application
    app.debug = True
    app.run()
    
    