import uuid
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
from cassandra.cluster import Cluster
from datetime import datetime


# Establish connection to Cassandra
def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])  # Connect to local Cassandra instance
    session = cluster.connect()
    session.set_keyspace('my_keyspace')  # Use your keyspace name here
    return session


# Insert data into Cassandra
def insert_into_cassandra(session, url, label):
    id = uuid.uuid1()  # Generate a UUID for the id column
    detection_time = datetime.now()  # Get current timestamp for detection_time column
    session.execute(
        """
        INSERT INTO malicious_urls (id, url, label, detection_time)
        VALUES (%s, %s, %s, %s)
        """,
        (id, url, label, detection_time)
    )
