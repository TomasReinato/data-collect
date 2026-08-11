# %%
###IMPORTS

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import polars as pl 

# %%
###FUNCTIONS
url = 'https://www.residentevildatabase.com/personagens/'

def get_content(url):
    resp = requests.get(url)
    return resp

def get_url_personagens(url):
    resp = get_content(url)
    if resp.status_code != 200:
        print('Nãop foi possível obter os dados')
    else:
        soup_personagens = BeautifulSoup(resp.text)
        sessoes = (soup_personagens.find("div", class_ = "td-page-content").find_all('a'))
        get_url = [i.get('href') for i in sessoes]
    return get_url

def get_basic_infos(soup):
    div_page = soup.find("div", class_ = "td-page-content")
    paragrafo = div_page.find_all("p")[1]
    ems = paragrafo.find_all("em")
    data = {}
    for i in ems:
        chave,  valor, *_ = i.text.split(":")
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

def get_personagens_info(url):
    resp = get_content(url)
    if resp.status_code != 200:
        print("Não foi possível obter os dados")
        return {}
    else:
        soup = BeautifulSoup(resp.text)
        data = get_basic_infos(soup)
        data['Appearances'] = get_apperances(soup)
        return data

# %%
urls = get_url_personagens(url)
data = []
for i in tqdm(urls):
    print(i)
    d = get_personagens_info(i)
    d['link'] = i
    nome = i.strip("/").split("/")[-1].replace("-", " ").title()
    d["Nome"] = nome
    data.append(d)
# %%[
lf = pl.DataFrame(data)
# %%
lf.write_parquet("output.parquet")