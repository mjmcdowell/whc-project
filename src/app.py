import pandas as pd
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Load data from a CSV file
csv_path = os.environ['CSV_PATH']
data = pd.read_csv(csv_path)

@app.route('/query', methods=['GET'])
def query_data():
    # Get the 'unique_number' parameter from the query string
    unique_number = request.args.get('unique_number')
    if not unique_number:
        return jsonify({"error": "Please provide a unique_number parameter"}), 400
    
    # Filter based on 'unique_number'

    result = data[data['unique_number'] == int(unique_number)]

    if not result.empty:
        return jsonify(result.to_dict(orient='records')), 200
    else:
        return jsonify({"error": "No data found for the provided unique_number"}), 404

@app.route('/health', methods=['GET'])
def health_check():
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)