# %%
###IMPORTS

import requests
from bs4 import BeautifulSoup

# %%
###FUNCTIONS
data = {}

def get_content(url):
    resp = requests.get(url)
    return resp

def get_basic_infos(soup):
    div_page = soup.find("div", class_ = "td-page-content")
    paragrafo = div_page.find_all("p")[1]
    ems = paragrafo.find_all("em")
    for i in ems:
        chave,  valor = i.text.split(":")
        chave = chave.strip(" ")
        data[chave] = valor

    return data

def get_apperances(soup):
    lis = (soup.find("div", class_ = "td-page-content")
       .find('h4')
       .find_next()
       .find_all('li')
    )
    appearances = [i.text for i in lis]
    return appearances

def get_name(soup):
    nome = (soup.find("div", class_ = "td-page-header")
       .find('h1')
       .find('span')
       .text.split(" | ")
    )
    return nome[1]

url_geral = 'https://www.residentevildatabase.com/personagens/'
get_url = 'https://www.residentevildatabase.com/personagens/ivan-ataman-judanovich/'
# %%
url = get_url
resp = get_content(url)

if resp.status_code != 200:
    print('Nãop foi possível obter os dados')
else:
    soup = BeautifulSoup(resp.text)
    data['Nome'] = get_name(soup)
    data = get_basic_infos(soup)
    data['Appearances'] = get_apperances(soup)
    

data
# %%

# def get_url_personagens(url_geral):
personagens = get_content(url_geral)
if personagens.status_code != 200:
    print('Nãop foi possível obter os dados')
else:
    print(personagens.status_code)
soup_personagens = BeautifulSoup(personagens.text)
# get_url = (
sessoes = (soup_personagens.find("div", class_ = "td-page-content").find_all('h3'))
personagens_sessao = [i.find_next() for i in sessoes]
        # .find_next('a')
        # .get('href')
    # )
    # return get_url
# get_url
