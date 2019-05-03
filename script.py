'''
coletor input.txt output.txt

# input.txt
# <link portal de notícia> <data inicial timestamp> <data final timestamp> <qtd noticias>
https://www.uol.com.br 1554390900 1554477300 10
https://www.globo.com 1554390900 1554477300 *

# output.txt
# <link da notícia> <categoria> <facebook tweeter> <ranking no portal origem>
https://g1.globo.com/politica/noticia/2019/04/05/nao-existe-olavetes-contra-militares-diz-bolsonaro-sobre-disputa-entre-alas-do-governo.ghtml política 76 tweet
'''
import sys

#Listas onde ficarão armazenadas os dados do arquivo de input.

links=[]
datasIniciais=[]
datasFinais=[]
qtdsNoticias=[]
nomeDoArquivo = str(sys.argv[1])

#Leitura do arquivo input.txt

with open(nomeDoArquivo, "r") as arquivo:
    for line in arquivo.readlines():
        link, dataInicial, dataFinal, qtdNoticias = line.split(' ')
        links.append(link)
        datasIniciais.append(dataInicial)
        datasFinais.append(dataFinal)
        qtdsNoticias.append(qtdNoticias)
    print(links, datasFinais, datasIniciais, qtdsNoticias)




#Criação do arquivo output.txt (se não existir) e escrita no arquivo
