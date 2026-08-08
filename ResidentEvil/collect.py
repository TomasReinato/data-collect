# %%
###IMPORTS

import requests
from bs4 import BeautifulSoup

# %%
###FUNCTIONS
def get_content(url):
    resp = requests.get(url)
    return resp

def get_basic_infos(soup):
    div_page = soup.find("div", class_ = "td-page-content")
    paragrafo = div_page.find_all("p")[1]
    ems = paragrafo.find_all("em")
    data = {}
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


# %%
url = get_url
resp = get_content(url)

if resp.status_code != 200:
    print('Nãop foi possível obter os dados')
else:
    soup = BeautifulSoup(resp.text)
    data = get_basic_infos(soup)
    data['Appearances'] = get_apperances(soup)

data
# %%
url_personagens = 'https://www.residentevildatabase.com/personagens/'
personagens = get_content(url_personagens)
if personagens.status_code != 200:
    print('Nãop foi possível obter os dados')
else:
    print(personagens.status_code)
soup_personagens = BeautifulSoup(personagens.text)
get_url = (
    soup_personagens
    .find("div", class_ = "td-page-content")
    .find('h3')
    .find_next('a')
    .get('href')
)
get_url


# %%
