#O seguinte código acessa o site do g1.globo.com coletando o código fonte da página html do site através da biblioteca requests. O BeautifulSoup pega o código fonte e permite que este código fonte seja trabalhado de uma maneira mais fácil. Observe a tag "a" e o atributo "class".

#O objetivo deste código é listar todos os links cuja classe é "feed-post-link", que são as notícias principais. 

import requests
import re
from bs4 import BeautifulSoup
pagina = requests.get("https://g1.globo.com/pi/piaui/").text
soup = BeautifulSoup(pagina, 'html.parser')
links = soup.find_all("a")
novoslinks = []
principal = []
print("Artigos!")
# Capturar links com a classe "feed-post-link" adicionando a lista "novoslinks"
principais = soup.findAll('a', {"class":"feed-post-link"})
#subtitulos = soup.findAll('div', {"class":"feed-post-body-resumo"})
for i in soup.findAll('a', {"class":"feed-post-link"}):
    novoslinks.append(i.get('href'))
# listar links com a classe "feed-post link"
print("Principais!!!")
for i in range(len(principais)):
    print("Título: ",principais[i].text)
    #print("Sub título: ",subtitulos[i].text)
    print("Link: ",principais[i].get('href'))
    print()
#class="feed-post-body-resumo">
