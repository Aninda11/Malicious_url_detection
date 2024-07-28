from flask import Flask, request, jsonify
from predictor import predict
from models import PredictionInput
from notifyer import send_notification


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def prediction():
    # Get input data from request
    input_data = PredictionInput(**request.json)
    # Perform prediction
    predictions = predict(input_data)
    threat_labels = ["defacement", "malware", "phishing"]
    if any(label in predictions for label in threat_labels):
        # If any malicious URL detected, send notification
        send_notification(input_data.data)

    # Return prediction results
    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    app.run(debug=True)

