from bs4 import BeautifulSoup
from io import BytesIO
from s3 import s3
import requests, zipfile, shutil
import urllib
import wget
import io

class DownloadFiles():

    def __init__(self):
        self.url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
        r = requests.get(self.url, stream =True)
        self.soup = BeautifulSoup(r.content, "lxml")
        self.check = zipfile.is_zipfile(io.BytesIO(r.content))
        

    def get_url(self):
        link_list = []
        for a in self.soup.find_all("a", class_ = "external-link", href = True):
            link_list.append(a["href"])

        return link_list


    def download_zip(self,link):
        file_name = "teste"
        output = BytesIO() 
        
        with urllib.request.urlopen(link) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            with zipfile.ZipFile(file_name) as zf:
                zf.extractall(output)
                filebyte = output.getvalue()

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
            filebytes = self.download(link)
            #self.send_file_to_s3(filebytes)

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
        filebytes = teste.download_zip(link)
        print(filebytes)
