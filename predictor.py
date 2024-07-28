from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
from database import insert_into_cassandra, connect_to_cassandra


# Load pre-trained model
def load_model():
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=4)
    model.load_state_dict(torch.load('distilbert_model.pth', map_location=torch.device('cpu')))
    model.eval()
    return model


# Preprocess input data
def preprocess_data(text, tokenizer):
    inputs = tokenizer(text, truncation=True, padding=True, max_length=512, return_tensors="pt")
    return inputs


# Perform prediction
def predict(input_data):
    # Load pre-trained model
    model = load_model()

    # Tokenize and preprocess input data
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
    inputs = preprocess_data(input_data.data, tokenizer)

    # Perform prediction
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=1).tolist()

    # Map encoded predictions to actual labels
    label_mapping = {
        0: 'benign',
        1: 'defacement',
        2: 'malware',
        3: 'phishing'
    }
    mapped_predictions = [label_mapping[pred] for pred in predictions]

    # Insert data into Cassandra
    session = connect_to_cassandra()
    for label in mapped_predictions:
        insert_into_cassandra(session, input_data.data, label)

    return mapped_predictions
