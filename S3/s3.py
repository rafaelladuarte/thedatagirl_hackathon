import boto3
import base64
import hashlib

class S3:
    def __init__(self, bucket):
        self.bucket = bucket

    def file_md5(self, filebytes):

        digest = hashlib.md5(filebytes).digest()
        encode = base64.b64encode(digest)

        return encode.decode('utf-8')

    def save_csv(self, filename, filebytes):

        client = boto3.Session().client('s3')
        md5 = self.file_md5(filebytes)

        response = client.put_object(
            Body=filebytes,
            Bucket=self.bucket,
            Key=filename,
            ContentMD5=md5,
            ContentType='text/csv',
            ACL='public-read'
        )

        status_code = response['ResponseMetadata']['HTTPStatusCode']

        if status_code != 200:
            raise ValueError(f"status code returned {status_code}")
