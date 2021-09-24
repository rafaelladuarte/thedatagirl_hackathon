from dask.core import get
import dask.dataframe as dd
import re

bucket_name = 'thedatagirls-hackathon-a3'
file_name = 'ESTABELECIMENTO*'

def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i)<128)

def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]',' ', text)

def get_csv(self,file_name):
    df = dd.read_csv(
        f'gs://{bucket_name}/{file_name}', 
        encoding = 'iso-8859-1', 
        header = None, 
        sep=';'
    )

    return df


df = get_csv(file_name)