from flask import Flask
from flask import request
from flask import render_template
import boto3
from fileinput import filename

app = Flask(__name__)
s3 = boto3.resource('s3')
BUCKET_NAME = 'ejemplounibe'


def getFilesInBucket():
    my_bucket = s3.Bucket(BUCKET_NAME)
    return my_bucket.objects.all()


@app.route('/')
def home():
    fileList = getFilesInBucket()
    return render_template('index.html', bucketName=BUCKET_NAME, fileList=fileList)


@app.route('/upload2s3', methods=['POST'])
def upload2s3():
    if request.method == 'POST':
        file = request.files['file']
        s3.Bucket(BUCKET_NAME).put_object(Key=file.filename, Body=file)

    fileList = getFilesInBucket()

    return render_template('index.html', bucketName=BUCKET_NAME, fileList=fileList)


if __name__ == '__main__':
    app.run()
