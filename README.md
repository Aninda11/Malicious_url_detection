# malicious_url_detection
My malicious url detector project for Data Scientist Internship at iNeuron.ai.

Here's a README file for this project:

---

# Malicious URL Detector

This project aims to develop a predictive model for detecting malicious URLs using the DistilBERT transformer model. The project involves data preprocessing, model training, validation, testing, and deploying an API for predictions. Additionally, a notification system alerts the cybersecurity team if a malicious URL is detected. The project utilizes a Cassandra database and is implemented as a Flask application.

## Project Structure

- `malicious_url_detector.ipynb`: Jupyter notebook for training the model and generating the `distilbert_model.pth` file.
- `main.py`: Main script to run the Flask application.
- `app_vars.py`: variables connecting to app.
- 'env': variables setting env file.
- `database.py`: Script to manage database operations using Cassandra.
- `models.py`: Script defining the model architecture.
- `predictor.py`: Script for making predictions using the trained model.

## Setup Instructions

### Prerequisites

- Python 3.8 or later
- Cassandra database
- Flask
- PyTorch
- Transformers
- smtplib

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aninda11/Malicious_url_detection.git
   cd ml
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. **Start Cassandra:**
   Follow the instructions to start your Cassandra server.

2. **Create Keyspace and Table:**
   Open `cqlsh` and create the keyspace and table:
   ```cql
   CREATE KEYSPACE my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
   USE my_keyspace;
   CREATE TABLE malicious_urls (
       id UUID PRIMARY KEY,
       detection_time TIMESTAMP,
       label TEXT,
       url TEXT
   );
   ```

### Model Training

1. **Run the Jupyter notebook to train the model:**
   ```bash
   jupyter notebook malicious_url_detector.ipynb
   ```
   This will generate the `distilbert_model.pth` file in the same directory.

### Running the Application

1. **Ensure the `distilbert_model.pth` file is in the same directory as `main.py`.**

2. **Run the Flask application:**
   ```bash
   python main.py
   ```

3. **Access the application:**
   Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. **Making Predictions:**
   Use the `/predict` endpoint to make predictions by sending a POST request with the URL to be classified.

2. **Notifications:**
   The application sends email notifications if a malicious URL is detected.

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.


---

Replace `https://github.com/Aninda11/Malicious_url_detection.git` with the actual URL of your GitHub repository.
