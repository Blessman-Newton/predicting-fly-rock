from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('best_pipeline.pkl', 'rb') as model_file:
    best_pipeline = pickle.load(model_file)

# Define the expected columns
columns = [
    'burden', 'spacing', 'ucs', 'bench_height', 'hole_diameter', 
    'initial_stemming_height_', 'final_stemming_height', 'charge_length', 
    'charge_hole_', 'powder_factor'
]

@app.route('/')
def home():
    return "Welcome to the ML Model API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print("Received data:", data)
    
    # Convert the input data to a DataFrame
    df = pd.DataFrame(data)
    print("DataFrame columns:", df.columns.tolist())
    
    # Check if the input data contains the expected columns
    if not all(column in df.columns for column in columns):
        return jsonify({"error": "Invalid input data. Expected columns: " + ", ".join(columns)}), 400
    
    # Ensure the DataFrame has the correct order of columns
    df = df[columns]
    
    # Make predictions
    predictions = best_pipeline.predict(df)
    predictions1 = best_pipeline.predict_proba(df)
    print("Predictions:", predictions)
    print("Predictions:", predictions1)
    
    return jsonify(predictions1.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)