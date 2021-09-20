from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import BytesIO
from s3 import s3

import pandas as pd
import requests
import zipfile 
import shutil
import os


class DownloadFiles():

    def __init__(self):
        self.url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
        r = requests.get(self.url, stream =True)
        self.soup = BeautifulSoup(r.content, "lxml")
        self.check = zipfile.is_zipfile(BytesIO(r.content))
        

    def get_url(self):
        link_list = []
        for a in self.soup.find_all("a", class_ = "external-link", href = True):
            link_list.append(a["href"])

        return link_list


    def download_file_byte_zip(self,link):
        zip_name = "zip_teste.zip"
        file_name = 'file_teste.csv'
        output = BytesIO() 

        with urlopen(link) as response, open(zip_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            with zipfile.ZipFile(file_name) as z:
                with z.open(file_name) as f:
                    file_pd = pd.read_csv(f.read(),sep=";",encoding='utf-8')
                    file = f.read()
                    filebyte = output.getvalue(file)

        os.remove(file_name)
        os.remove(zip_name)
        return filebyte


    def send_file_to_s3(self, filebyte):
        filename = ""
        s3.save_csv(filename, filebyte)
        

    def start_download(self):
        list_link = self.get_url()

        i = 0
        for link in list_link:
            i = i + 1
            print(f"Downloading File {i}...")
            filebytes = self.download_file_byte_zip(link)
            self.send_file_to_s3(filebytes)

        print("All Downloads Finished")

        return None

if __name__ == "__main__":
    teste = DownloadFiles()
    list_all_links =teste.get_url()
    links_teste = list_all_links[0:2]

    i = 0
    for link in links_teste:
        i = i + 1
        print(f"Downloading File {i}...")
        filebytes = teste.download_file_byte_zip(link)
        print(filebytes)
