from urllib.request import urlopen
from bs4 import BeautifulSoup
#from cloud.bucket import MyStorage
from datetime import datetime
from io import BytesIO
import requests
import zipfile 
import csv
import os

#cloud = MyStorage()

class DownloadFiles():

    def __init__(self):
        self.url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
        r = requests.get(self.url, stream =True)
        self.soup = BeautifulSoup(r.content, "lxml")
        

    def get_url(self):
        link_list = []
        for a in self.soup.find_all("a", class_ = "external-link", href = True):
            link_list.append(a["href"])

        return link_list


    def download_files(self,link):
        file_nm = 'file'

        with BytesIO(requests.get(link).content) as filebytes:
            with zipfile.ZipFile(filebytes) as z:
                z.extractall(file_nm)
            
    
    def get_file_csv_name(self):
        lista = os.listdir('file')
        em, es,so, o = 0,0,0,0
        today = str(datetime.now())
        today = today.replace(' ', '_')

        for l in lista:
            if 'EMPRECSV' in l:
                em += 1
                csv_nm = 'EMPRESAS' + str(em) + '.csv'
                os.rename('file/' +l, csv_nm)
            elif 'ESTABELE' in l:
                es += 1
                csv_nm = 'ESTABELECIMENTO' + str(es) +'.csv'
                os.rename('file/' +l, csv_nm)
            elif 'SOCIOCSV' in l:
                so += 1
                csv_nm = 'SOCIO' + str(so)+ '.csv'
                os.rename('file/' +l, csv_nm)
            else:
                o += 1
                csv_nm = 'OUTROS' + str(o) + '.csv'
                os.rename('file/' +l, csv_nm)
        
        print('Remove Dir...')
        os.rmdir('file')

        return csv_nm

    def start_download(self):
        list_link = self.get_url()

        i = 0
        for link in list_link:
            i = i + 1
            print(f"Downloading File {i}...")
            self.download_files(link)
            print(f'Download File {i}')

            local = self.get_file_csv_name()
            
            print(f'Sending File {i}...')
            # cloud.send_csv(file_nm)
            print(f'Sent File {i}')

            print(f'Removing File {i}...')
            os.remove(local)
            print(f'Remove File {i}...')

        print("All Downloads Finished")

if __name__ == "__main__":
    teste = DownloadFiles()
    list_all_links =teste.get_url()
    links_teste = list_all_links[-2:]

    i = 0
    for link in links_teste:
        i = i + 1
        print(f"Downloading File {i}...")
        teste.download_files(link)
        print(f'Download File {i}')

        local = teste.get_file_csv_name()
        
        print(f'Sending File {i}...')
        # cloud.send_csv(file_nm)
        print(f'Sent File {i}')

        print(f'Removing File {i}...')
        os.remove(local)
        print(f'Remove File {i}...')
