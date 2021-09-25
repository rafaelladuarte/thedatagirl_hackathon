from google.cloud import storage

bucket_name = 'thedatagirls-hackathon-a3'
project_name = 'hackathon-a3-data'

class MyStorage():
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket_name)
    
    def send_csv(self, remote_file, local_file):
        """
        Uploads a file to the bucket.
        Source: https://cloud.google.com/storage/docs/uploading-objects
        """
        blob = self.bucket.blob(remote_file)
        blob.upload_from_filename(local_file)


