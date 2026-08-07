# %%
import requests

url ="https://www.google.com"

resp = requests.get(url)
# %%
resp.status_code