from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the saved Logistic Regression Pipeline
with open('student_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Define feature lists from your screenshot to ensure type conversion
num_features = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        # Capture all form inputs
        form_data = request.form.to_dict()
        
        # Convert to DataFrame
        df_input = pd.DataFrame([form_data])
        
        
        for col in num_features:
            df_input[col] = pd.to_numeric(df_input[col])

        # Prediction using the Pipeline (Preprocess + Logistic Regression)
        prediction = model.predict(df_input)[0]
        prob = model.predict_proba(df_input)[0][1]
        result = "PASS" if prediction == 1 else "FAIL"
        
        # Determine color for the UI
        color = "green" if result == "PASS" else "red"
        
        return render_template('index.html', 
                            prediction_text=f'Result: {result}',
                            confidence=f'Confidence: {prob*100:.2f}%',
                            result_color=color)
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    app.run(debug=True)