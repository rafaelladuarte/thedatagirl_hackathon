from mycloud.bucket import MyStorage
from bs4 import BeautifulSoup
from datetime import datetime
from io import BytesIO

import requests
import zipfile
import os

cloud = MyStorage() # Construct a Storage object.

class DownloadFiles():

    def __init__(self):
        """
        Download an IRS webpage returning a response object
        to collect all existing information
        """
        self.url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
        r = requests.get(self.url, stream = True)
        self.soup = BeautifulSoup(r.content, "lxml")
        

    def get_url(self):
        """
        Scrap the response object to collect the links from the zip files
        """
        link_list = []
        for a in self.soup.find_all("a", class_ = "external-link", href = True):
            link_list.append(a["href"])

        return link_list


    def download_files(self, link):
        """
        Download the zip file link into memory and then unzip 
        and extract in the file directory
        """
        file_nm = 'file'

        with BytesIO(requests.get(link).content) as filebytes:
            with zipfile.ZipFile(filebytes) as z:
                z.extractall(file_nm)
            
    
    def get_file_csv_name(self):
        """
        Lists extracted files into the file directory
        and renamed according to spreadsheet type to facilitate
        the identification. Then we remove the directory from memory
        not to fill the machine's memory
        """
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
        """
        Starts download of spreadsheets and sends to bucket
        """
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
    links_teste = list_all_links[-2:]

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