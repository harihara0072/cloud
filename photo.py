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
    bucket_name = os.environ.get('BUCKET_NAME',
                                 app_identity.get_default_gcs_bucket_name())
    bucket = '/' + bucket_name

    response.write('Listbucket result:<br>')
    response.write('<ol>')

    page_size = 1
    stats = client.listbucket(bucket, max_keys=page_size)
    while True:
        count = 0
        for stat in stats:
            count += 1
            file_name = repr(stat.filename)
            response.write('<li><a href=' + str('\'/download?file=' + str(os.path.basename(file_name)) + '\'>'))
            response.write('%s</a>' % file_name)
            response.write('&nbsp;&nbsp;&nbsp;&nbsp;')
            response.write('<a href=' + str('\'/view?file=' + str(os.path.basename(file_name)) + '\'>'))
            response.write('View Me</a>')
            response.write(
                '&nbsp;&nbsp;&nbsp;&nbsp;<a href=' + str(
                    '\'/download?file=' + str(os.path.basename(file_name)) + '\'>'))
            response.write('Download Me</a>')
            # self.response.write('<button type="button" onclick="location.href=;" value="Download">'%file_name)
            response.write('</li>')

        if count != page_size or count == 0:
            break
        stats = client.listbucket(bucket, max_keys=page_size,
                               marker=stat.filename)
    response.write('</ol>')
    return "Hello hari"


if __name__ == '__main__':
    app.run()
