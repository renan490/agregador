#O seguinte código acessa o site do cidadeverde.com coletando o código fonte da página html do site através da biblioteca urllib.request. O BeautifulSoup pega o código fonte e permite que este código fonte seja trabalhado de uma maneira mais fácil. Observe a tag "ul" e o atributo "class".

#O objetivo deste código é listar todos os links da tag ul cuja classe é "materias-destaque", que são as notícias principais.

import urllib.request
import integracaocidadeverdeb
from bs4 import BeautifulSoup

# O urllib.request.urlopen() acessa a url e retorna o código html.
url = "https://cidadeverde.com/"
fonte = urllib.request.urlopen(url)
sopa = BeautifulSoup(fonte, "lxml")
materiasDestaque = sopa.findAll("ul",{"class":"materias-destaque"})
materiasDestaque = BeautifulSoup(str(materiasDestaque), "lxml")
linksdestaque = materiasDestaque.findAll("a")
for i in linksdestaque:
    integracaocidadeverdeb.integracao(i.get('href'))
    print()

