from flask import Flask, request, jsonify
from predictor import predict
from models import PredictionInput

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def prediction():
    # Get input data from request
    input_data = PredictionInput(**request.json)

    # Perform prediction
    predictions = predict(input_data)

    # Return prediction results
    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    app.run(debug=True)
