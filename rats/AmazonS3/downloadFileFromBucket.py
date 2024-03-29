import boto3
import botocore

BUCKET_NAME = 'shumi-bucket' # replace with your bucket name
KEY = 'test.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'downloads/test_downloaded.txt')
    print("Download complete")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print(e)
        print("The object does not exist.")
    else:
        raise

