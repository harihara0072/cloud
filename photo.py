from flask import Flask
from google.cloud import storage
import os


app = Flask(__name__)


@app.route('/')
def hello_world():

    # Imports the Google Cloud client library
    #from google.cloud import storage
    # Instantiates a client
    client = storage.Client()
    for bucket in client.list_buckets():
        print(bucket)
    bucket_name = "haricloudbucket"
	storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)
    return "Hello hari"


if __name__ == '__main__':
    app.run()
