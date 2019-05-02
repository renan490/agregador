# enconde: utf-8
import urllib.request
from bs4 import BeautifulSoup 
f = urllib.request.urlopen('https://g1.globo.com/economia/noticia/2019/04/16/bolsonaro-afirma-que-nao-quer-e-nao-pode-intervir-em-politica-de-precos-da-petrobras-diz-porta-voz.ghtml')
soup = BeautifulSoup(f, "lxml")
date = str(soup.time).split('"')[1]
print(date)
from datetime import datetime
date2 = datetime.strptime(date[:-1].strip('"'), '%Y-%m-%dT%H:%M:%S.%f')
print(date2)
timestamp = datetime.timestamp(date2)
print(timestamp)
