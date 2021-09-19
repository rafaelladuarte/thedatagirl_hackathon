import requests
from bs4 import BeautifulSoup
import wget

url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
link_list = []
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

for a in soup.find_all("a", class_ = "external-link", href = True):
    link_list.append(a["href"])

i = 0
for link in link_list:
    i = i + 1
    print(f"Downloading File {i}...")
    wget.download(link)
    
print("All Downloads Finished")