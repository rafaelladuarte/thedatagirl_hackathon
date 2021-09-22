from google.cloud import storage
import dask.dataframe as dd

bucket_name = 'thedatagirls-hackathon-a3'

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

    def get_csv(self, remote_file):
        df = dd.read_csv(f'gs://{bucket_name}/{remote_file}', encoding = 'iso-8859-1', header = None)
        return df

    def list_files(self):
        file_list = []
        for blob in self.client.list_blobs(bucket_name):
            file_list.append(blob.name)
        return file_list

if __name__ == "__main__":
    cloud = MyStorage()
    df = cloud.get_csv("UALS_2021-09-22_01-07-48.557902.csv")
    print(df.head())