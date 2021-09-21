from google.cloud import storage

import pandas as pd
import os

class Storage():
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket('bucket-id-here')
    
    def send_csv(self,remote_file,local_file):
        blob = self.bucket.blob(remote_file)
        blob.upload_from_filename(local_file)

    def get_csv(self,remote_file):
        df = pd.read_csv('gs://'+remote_file)
        return df

    def remove_file(self,file):
        os.remove('gs://' + file)

    