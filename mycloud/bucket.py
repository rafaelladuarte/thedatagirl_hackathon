from google.cloud import storage
from io import BytesIO
import dask.dataframe as dd

from unicodedata import category

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

    def get_csv(self,file_name):
        blob  = self.bucket.blob(file_name)
        df = dd.read_csv(f'gs://{bucket_name}/{file_name}', encoding = 'iso-8859-1', header = None, sep=';')
    
        return df

    def list_files(self):
        file_list = []
        for blob in self.client.list_blobs(bucket_name):
            file_list.append(blob.name)
        return file_list


if __name__ == "__main__":
    cloud = MyStorage()
    df = cloud.get_csv("UALS_2021-09-22_22-55-31.106577.csv")
    print(df.head())