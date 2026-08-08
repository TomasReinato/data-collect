# %%
import requests
from bs4 import BeautifulSoup

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

url = 'https://www.residentevildatabase.com/personagens/ada-wong/'
resp = get_content(url)

if resp.status_code != 200:
    print('Nãop foi possível obter os dados')

soup = BeautifulSoup(resp.text)
soup

get_basic_infos(soup)
data

# %%
