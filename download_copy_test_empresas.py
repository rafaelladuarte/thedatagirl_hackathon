from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from io import BytesIO
from cloud.bucket import MyStorage
import requests
import zipfile
import os

cloud = MyStorage()

class DownloadFiles():

    def __init__(self):
        self.url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
        r = requests.get(self.url, stream = True)
        self.soup = BeautifulSoup(r.content, "lxml")
        

    def get_url(self):
        link_list = []
        for a in self.soup.find_all("a", class_ = "external-link", href = True):
            link_list.append(a["href"])

        return link_list


    def download_files(self, link):
        file_nm = 'file'

        with BytesIO(requests.get(link).content) as filebytes:
            with zipfile.ZipFile(filebytes) as z:
                z.extractall(file_nm)
            
    
    def get_file_csv_name(self):
        lista = os.listdir('file')
        today = str(datetime.now())
        today = today.replace(' ', '_')
        today = today.replace(':', '-')

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
            cloud.send_csv(local, local)
            print(f'Uploading File {i}...')

            print(f'Removing File {i}...')
            os.remove(local)
            print(f'Removed File {i}...')

        print("All Operations Finished")

if __name__ == "__main__":
    teste = DownloadFiles()
    list_all_links = teste.get_url()
    links_teste = list_all_links[4:10]

    i = 0
    for link in links_teste:
        i = i + 1
        print(f"Downloading File {i}...")
        teste.download_files(link)
        print(f'Downloaded File {i}')

        local = teste.get_file_csv_name()

        print(f'Uploading File {i}...')
        cloud.send_csv(local, local)
        print(f'Uploaded File {i}')

        print(f'Removing File {i}...')
        os.remove(local)
        print(f'Removed File {i}...')