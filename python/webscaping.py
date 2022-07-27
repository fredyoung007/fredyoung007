import requests
from bs4 import BeautifulSoup

url = "https://yntbros.com"
page = requests.get(url).content
soup = BeautifulSoup(page, "html.parser")

print(soup.p)