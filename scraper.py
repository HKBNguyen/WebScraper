import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
print soup.prettify()