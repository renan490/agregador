#Este código acessa um artigo específico do site cidadeverde.com e captura e imprime o título, a fonte, a data e o link. 
#

# enconde: utf-8
import urllib.request
import os.path
from bs4 import BeautifulSoup
def integracao(url):
    # Captura a string após a última barra da url.
    arquivo = url.split("/")[-1]
    # Para agilizar a consulta de uma url, o documento html é salvo com o nome e a extensão após a última barra.
    # O urllib.request acessa a url e retorna o código html caso necessário, senão for necessário acessar a url somente é feita uma leitura no html na pasta local.
    if not (os.path.isfile(arquivo)):
        with urllib.request.urlopen('https://cidadeverde.com/noticias/293271/governador-confirma-a-bancada-que-cortara-2300-cargos-com-reforma') as f:
            b=f.read().decode('utf-8')
        f.close()
        a=open(arquivo,"w")
        a.writelines(str(b))
        a.close()
    else:
        with open(arquivo) as f:
            b=f.read()
        f.close()
    # A captura do título, autor, data e link abaixo.
    soup = BeautifulSoup(b, "html.parser")
    titulo = soup.title.string
    autor = soup.findAll("div", { "class" : "post-body" })
    autor = BeautifulSoup(str(autor), "html.parser")
    #autor = autor[0].text.strip()
    data = soup.find("p",{"class":"post-date"})
    #texto = soup.findAll("p", {"class":"content-text__container"})
    print("TÍTULO:",titulo)
    print(autor.find("p").text)
    print("Data:",data.text)
    print("Link:",url)
    #<div class="post-body">
    #<p class="post-date">11/02/19, 20:48</p>
