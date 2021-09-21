from google.cloud import storage

import pandas as pd
import os

class MyStorage():
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket('bucket-id-here')
    
    def send_csv(self,remote_file,local_file):
        blob = self.bucket.blob(remote_file)
        blob.upload_from_filename(local_file)

    def get_csv(self,remote_file):
        df = pd.read_csv(remote_file)
        return df

    