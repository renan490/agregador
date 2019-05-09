#Este código acessa um artigo específico do site g1.globo.com e captura e imprime o título, o subtítulo, o autor, a data e o texto. 
#

# enconde: utf-8
import urllib.request
import os.path
from bs4 import BeautifulSoup
url = "https://g1.globo.com/pi/piaui/noticia/2019/02/06/policia-encontra-fabrica-de-falsificacao-de-dinheiro-e-prende-suspeito-no-litoral-do-piaui.ghtml"
# Captura a string após a última barra da url.
arquivo = url.split("/")[-1]
# Para agilizar a consulta de uma url, o documento html é salvo com o nome e a extensão após a última barra.
# O urllib.request acessa a url e retorna o código html caso necessário, senão for necessário acessar a url somente é feita uma leitura no html na pasta local.
if not (os.path.isfile(arquivo)):
    with urllib.request.urlopen('https://g1.globo.com/pi/piaui/noticia/2019/02/06/policia-encontra-fabrica-de-falsificacao-de-dinheiro-e-prende-suspeito-no-litoral-do-piaui.ghtml') as f:
        b=f.read().decode('utf-8')
    f.close()
    a=open(arquivo,"w")
    a.writelines(str(b))
    a.close()
else:
    with open(arquivo) as f:
        b=f.read()
    f.close()
# A captura do título, subtítulo, autor, data e texto abaixo.
soup = BeautifulSoup(b, "lxml")
titulo = soup.title.string
subtitulo = soup.h2.string
autor = soup.findAll("p", { "class" : "content-publication-data__from" })
autor = autor[0].text.strip()
data = soup.time.string
texto = soup.findAll("p", {"class":"content-text__container"})
print("TÍTULO:",titulo)
print("Subtítulo:",subtitulo)
print("Autor:",autor)
print("Data:",data)
print("Link:",url)
