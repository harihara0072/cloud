from flask import Flask
from google.cloud import storage

app = Flask(__name__)


@app.route('/')
def hello_world():

    # Imports the Google Cloud client library
    #from google.cloud import storage
    # Instantiates a client
    client = storage.Client()
    for bucket in client.list_buckets():
        print(bucket)


if __name__ == '__main__':
    app.run()
