import urllib.request
from bs4 import BeautifulSoup

#Listas onde ficarão armazenadas os dados do arquivo de input.

links="https://www.uol.com.br/"
#Criação do arquivo output.txt (se não existir) e escrita no arquivo

fonte = urllib.request.urlopen(links)
sopa = BeautifulSoup(fonte, "lxml")
materiasDestaque = sopa.findAll("a")
#Ignora os 32 primeiros links e lista 10 links
for i in range(32,42,1):
    print(materiasDestaque[i].get("href"))
