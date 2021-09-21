from urllib.request import urlopen
from bs4 import BeautifulSoup
from storage.bucket import Storage

import requests
import zipfile 
import shutil

cloud = Storage()

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
        file_nm = 'file.csv'
        zip_nm = 'zip.zip'

        with urlopen(link) as response, open(zip_nm, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            with zipfile.ZipFile(file_nm) as z:
                z.extractall(file_nm)
        return file_nm,zip_nm

    def start_download(self):
        list_link = self.get_url()

        i = 0
        for link in list_link:
            i = i + 1
            print(f"Downloading File {i}...")
            file_nm,zip_nm = self.download_files(link)
            print(f'Download File {i}')

            print(f'Sending File {i}...')
            cloud.send_csv(file_nm)
            print(f'Sent File {i}')

            print(f'Removing File {i}...')
            cloud.remove_file(file_nm)
            cloud.remove_file(zip_nm)
            print(f'Remove File {i}...')

        print("All Downloads Finished")

if __name__ == "__main__":
    teste = DownloadFiles()
    list_all_links =teste.get_url()
    links_teste = list_all_links[0:2]

    i = 0
    for link in links_teste:
        i = i + 1
        print(f"Downloading File {i}...")
        file_nm,zip_nm = teste.download_files(link)
        print(f'Download File {i}')

        print(f'Sending File {i}...')
        cloud.send_csv(file_nm)
        print(f'Sent File {i}')

        print(f'Removing File {i}...')
        cloud.remove_file(file_nm)
        cloud.remove_file(zip_nm)
        print(f'Remove File {i}...')
