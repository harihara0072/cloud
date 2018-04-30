from google.cloud import storage
import os
import MySQLdb
from flask import Flask

app = Flask(__name__)

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')

#cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

db = MySQLdb.connect(
            host='35.192.165.227',
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)
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