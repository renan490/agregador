#O seguinte código acessa o site do g1.globo.com coletando o código fonte da página html do site através da biblioteca requests. O BeautifulSoup pega o código fonte e permite que este código fonte seja trabalhado de uma maneira mais fácil. Observe a tag "a" e o atributo "class".

#O objetivo deste código é listar todos os links cuja classe é "feed-post-link", que são as notícias principais. 

import requests
import urllib.request
import re
from bs4 import BeautifulSoup

url = "https://www.cidademodelo.com/"
fonte = urllib.request.urlopen(url)
sopa = BeautifulSoup(fonte, "lxml")
materiasDestaque = sopa.findAll("div",{"class":"page-content"})
materiasDestaque = BeautifulSoup(str(materiasDestaque), "lxml")
linksdestaque = materiasDestaque.findAll("h3")
for i in range(5):
    print("Título:",linksdestaque[i].text.strip())
    link=linksdestaque[i].findAll("a")
    for j in link:
        print("Link:",j.get("href"))
    print()
#<div class="page-content">

