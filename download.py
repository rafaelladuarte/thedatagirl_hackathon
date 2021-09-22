from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from io import BytesIO
from google.cloud import storage
import requests
import zipfile 
import os

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to the bucket.
    Source: https://cloud.google.com/storage/docs/uploading-objects
    """
            
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")


class DownloadFiles():

    def __init__(self):
        self.url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
        r = requests.get(self.url, stream = True)
        self.soup = BeautifulSoup(r.content, "lxml")
        

    def get_url(self):
        link_list = []
        for a in self.soup.find_all("a", class_ = "external-link", href = True):
            link_list.append(a["href"])

        return link_list[-2:]


    def download_files(self, link):
        file_nm = 'file'

        with BytesIO(requests.get(link).content) as filebytes:
            with zipfile.ZipFile(filebytes) as z:
                z.extractall(file_nm)
            
    
    def get_file_csv_name(self):
        lista = os.listdir('file')
        today = str(datetime.now())
        today = today.replace(' ', '_')

        for l in lista:
            if 'EMPRECSV' in l:
                csv_nm = 'EMPRESAS_' + str(today) + '.csv'
                os.rename('file/' + l, csv_nm)
            elif 'ESTABELE' in l:
                csv_nm = 'ESTABELECIMENTO_' + str(today) +'.csv'
                os.rename('file/' + l, csv_nm)
            elif 'SOCIOCSV' in l:
                csv_nm = 'SOCIO_' + str(today)+ '.csv'
                os.rename('file/' + l, csv_nm)
            else:
                csv_nm = f'{l[-7:-3]}_{str(today)}.csv'
                os.rename('file/' + l, csv_nm)
        
        print('Removing Directory...')
        os.rmdir('file')

        return csv_nm


    def start_download(self):
        list_link = self.get_url()

        i = 0
        for link in list_link:
            i = i + 1
            print(f'Downloading File {i}...')
            self.download_files(link)
            print(f'Downloaded File {i}')

            local = self.get_file_csv_name()
            
            print(f'Uploading File {i}...')
            upload_blob("thedatagirls-hackathon-a3", local, local)

            print(f'Removing File {i}...')
            os.remove(local)
            print(f'Removed File {i}...')

        print("All Operations Finished")


if __name__ == "__main__":
    DownloadFiles().start_download()
    #para fazer a operação com todos os arquivos,
    #remover o [-2:] do return do get_url