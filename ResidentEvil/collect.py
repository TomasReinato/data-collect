# %%
import requests
from bs4 import BeautifulSoup

url ="https://www.residentevildatabase.com/personagens/ada-wong/"

resp = requests.get(url)
# %%
resp.status_code
# %%
resp.text
# %%
soup = BeautifulSoup(resp.text)
soup
# %%
div_page = soup.find("div", class_ = "td-page-content")
div_page
# %%
div_page.find_all("p")[1]
# %%
