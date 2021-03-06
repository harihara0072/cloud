from google.cloud import storage
import os
import pymysql
from flask import Flask

app = Flask(__name__)

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='cloud_db')

print "Database connected..."

@app.route('/')
def hello_world():
    # Imports the Google Cloud client library
    # from google.cloud import storage
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