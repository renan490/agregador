#O seguinte código acessa o site do g1.globo.com/pi/piaui coletando o código fonte da página html do site através da biblioteca requests. O BeautifulSoup pega o código fonte e permite que este código fonte seja trabalhado de uma maneira mais fácil. Observe a tag "a" e o atributo "class".

#O objetivo deste código é listar todos os links cuja classe é "feed-post-link", que são as notícias principais. 

import requests
import integracaog1b
from bs4 import BeautifulSoup
pagina = requests.get("https://g1.globo.com/pi/piaui/").text
soup = BeautifulSoup(pagina, 'html.parser')
# Capturar links com a classe "feed-post-link"
principais = soup.findAll('a', {"class":"feed-post-link"})
# listar links com a classe "feed-post link"
for i in range(len(principais)):
    integracaog1b.integracao(principais[i].get("href"))
    print()
