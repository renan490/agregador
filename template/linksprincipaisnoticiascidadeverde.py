#O seguinte código acessa o site do g1.globo.com coletando o código fonte da página html do site através da biblioteca requests. O BeautifulSoup pega o código fonte e permite que este código fonte seja trabalhado de uma maneira mais fácil. Observe a tag "a" e o atributo "class".

#O objetivo deste código é listar todos os links cuja classe é "feed-post-link", que são as notícias principais. 

import requests
import urllib.request
import re
from bs4 import BeautifulSoup
pagina = requests.get("https://cidadeverde.com/").text
soup = BeautifulSoup(pagina, 'html.parser')
links = soup.find_all("a")
novoslinks = []
principal = []
print("Artigos!")
# Capturar links com a classe "feed-post-link" adicionando a lista "novoslinks"
principais = soup.findAll('a', {"class":"materias-destaque"})
#subtitulos = soup.findAll('div', {"class":"feed-post-body-resumo"})
for i in soup.findAll('a', {"class":"materias-destaque"}):
    novoslinks.append(i.get('href'))
# listar links com a classe "feed-post link"
print("Principais!!!")
for i in range(len(principais)):
    print("Título: ",principais[i].text)
    #print("Sub título: ",subtitulos[i].text)
    print("Link: ",principais[i].get('href'))
    print()
#materiasDestaque = soup.findAll("div",{"class":"col-sm-5 clearfix"})
#linksMateriasDestaque = materiasDestaque.findAll("a")
#for i in linksMateriasDestaque:
#    print(i)
# Captura a string após a última barra da url.

# Para agilizar a consulta de uma url, o documento html é salvo com o nome e a extensão após a última barra.
# O urllib.request acessa a url e retorna o código html caso necessário, senão for necessário acessar a url somente é feita uma leitura no html na pasta local.
url = "https://cidadeverde.com/"
fonte = urllib.request.urlopen("https://cidadeverde.com/")
sopa = BeautifulSoup(fonte, "lxml")
materiasDestaque = sopa.findAll("ul",{"class":"materias-destaque"})
materiasDestaque = BeautifulSoup(str(materiasDestaque), "lxml")
linksdestaque = materiasDestaque.findAll("a")
for i in linksdestaque:
    print("Título: ",i.text)
    print("Link: ",i.get('href'))
#<div class="col-sm-5 clearfix">
#<ul class="materias-destaque">
#<ul class="materias-destaque">
