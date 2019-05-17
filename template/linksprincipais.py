import requests
import re
from bs4 import BeautifulSoup
import urllib
class Noticias:
    def __init__(self):
        self.id=0
    def g1(self):
        pagina = requests.get("https://g1.globo.com/pi/piaui/").text
        soup = BeautifulSoup(pagina, 'html.parser')
        links = soup.find_all("a")
        novoslinks = []
        artigos = []
        titulos=[]
        links=[]
        # Capturar links com a classe "feed-post-link" adicionando a lista "novoslinks"
        principais = soup.findAll('a', {"class":"feed-post-link"})
        #subtitulos = soup.findAll('div', {"class":"feed-post-body-resumo"})
        for i in soup.findAll('a', {"class":"feed-post-link"}):
            novoslinks.append(i.get('href'))
        # listar links com a classe "feed-post link"
        for i in range(len(principais)):
            titulos.append(principais[i].text)
            #print("Sub título: ",subtitulos[i].text)
            links.append(principais[i].get('href'))
        for index, titulo in enumerate(titulos):
            artigos.append({"id":self.id, "title":titulo, "link":links[index]})
            self.id+=1
        return artigos

    def cidadeverde(self):
        artigos = []
        titulos=[]
        links=[]
        url = "https://cidadeverde.com/"
        fonte = urllib.request.urlopen(url)
        sopa = BeautifulSoup(fonte, "lxml")
        materiasDestaque = sopa.findAll("ul",{"class":"materias-destaque"})
        materiasDestaque = BeautifulSoup(str(materiasDestaque), "lxml")
        linksdestaque = materiasDestaque.findAll("a")
        for i in linksdestaque:
            titulos.append(i.text)
            links.append(i.get('href'))
        for index, titulo in enumerate(titulos):
            artigos.append({"id":self.id, "title":titulo, "link":links[index]})
            self.id+=1
        return artigos

    def cidademodelo(self):
        links=[]
        titulos=[]
        artigos=[]
        url = "https://www.cidademodelo.com/"
        fonte = urllib.request.urlopen(url)
        sopa = BeautifulSoup(fonte, "lxml")
        materiasDestaque = sopa.findAll("div",{"class":"page-content"})
        materiasDestaque = BeautifulSoup(str(materiasDestaque), "lxml")
        linksdestaque = materiasDestaque.findAll("h3")
        for i in range(5):
            titulo=linksdestaque[i].text.strip()
            titulos.append(titulo)
            link=linksdestaque[i].findAll("a")
            for j in link:
                link=j.get("href")
                links.append(link)
        #<div class="page-content">
        for index, titulo in enumerate(titulos):
            artigos.append({"id":self.id, "title":titulo, "link":links[index]})
            self.id+=1
        return artigos

    def articles(self):
        structure = [
                {
                    'id': 1,
                    'title':'Article One',
                    'body':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.',
                    'author':'Brad Traversy',
                    'create_date':'04-25-2017'
                },
                {
                    'id': 2,
                    'title':'Article Two',
                    'body':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.',
                    'author':'John Doe',
                    'create_date':'04-25-2017'
                },
                {
                    'id': 3,
                    'title':'Article Three',
                    'body':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.',
                    'author':'Brad Traversy',
                    'create_date':'04-25-2017'
                }
        ]
        articles = self.g1()+self.cidademodelo()+self.cidadeverde()
        self.id=0
        print(articles)
        return articles
        
noticias = Noticias()
noticias.articles()