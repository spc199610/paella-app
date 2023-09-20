from flask import Flask, request, jsonify
import math
import json

app = Flask(__name__)

def transform_data(input_data):
    transformed = []

    # Check if the input object is a dictionary and has the 'use cases' key
    if 'use cases' not in input_data:
        raise ValueError("The input_data should be a dictionary with a 'use cases' key")

    # Iterate over the 'use cases' key from the input data
    for case in input_data['use cases']:
        # Check if individual cases have "onion people" and "nonion people" keys
        if 'onion people' not in case or 'nonion people' not in case:
            raise ValueError("Each case should have 'onion people' and 'nonion people' keys")

        # Try to perform mathematical operations
        try:
            onion = math.ceil(case["onion people"]/2)
            nonion = math.ceil(case["nonion people"]/2)
        except TypeError:
            raise TypeError("The values of 'onion people' and 'nonion people' should be numbers")
        
        new_case = {}
        new_case["tortilla"] = onion + nonion
        new_case["onion tortilla"] = onion
        new_case["nonion tortilla"] = nonion
        transformed.append(new_case)
    
    return transformed

@app.route('/paella', methods=['POST'])
def paella():
    # Extract JSON data from the request
    input_data = request.get_json()

    # Check if the input_data is valid
    if not input_data:
        return jsonify({"error": "No input data provided"}), 400

    # Process the input_data
    output_data = transform_data(input_data)

    # Create the output JSON structure
    output_json = {"output": output_data}

    # return the transformed data as a formatted JSON string
    return(json.dumps(output_json, indent=4))

if __name__ == '__main__':
    app.run(debug=True)

