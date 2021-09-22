from google.cloud import storage
import dask.dataframe as dd
import os

class MyStorage():
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket('thedatagirls-hackathon-a3')
    
    def send_csv(self, remote_file, local_file):
        """
        Uploads a file to the bucket.
        Source: https://cloud.google.com/storage/docs/uploading-objects
        """
        blob = self.bucket.blob(remote_file)
        blob.upload_from_filename(local_file)

    def get_csv(self, remote_file):
        df = dd.read_csv(remote_file)
        return df    