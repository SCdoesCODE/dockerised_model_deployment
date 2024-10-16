from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved XGBoost model
with open('model.pkl', 'rb') as file:  # Open the file in read-binary mode
    model = pickle.load(file)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = [
        float(request.form['gender']),
        float(request.form['age']),
        float(request.form['height']),
        float(request.form['weight']),
        int(request.form['family_history_with_overweight']),
        int(request.form['FAVC']),
        int(request.form['FCVC']),
        float(request.form['NCP']),
        int(request.form['CAEC']),
        int(request.form['SMOKE']),
        float(request.form['CH2O']),
        int(request.form['SCC']),
        float(request.form['FAF']),
        int(request.form['TUE']),
        int(request.form['CALC']),
        int(request.form['MTRANS'])
    ]
    
    # Convert to numpy array for prediction
    features = np.array(data).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)[0]

    # Map prediction to corresponding label
    health_status_mapping = {
        0: 'Insufficient Weight',
        1: 'Normal Weight',
        2: 'Obesity Type I',
        3: 'Obesity Type II',
        4: 'Obesity Type III',
        5: 'Overweight Level I',
        6: 'Overweight Level II'
    }
    prediction_label = health_status_mapping[prediction]

    return render_template('index.html', prediction=prediction_label)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)