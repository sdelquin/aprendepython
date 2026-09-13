import requests
from bs4 import BeautifulSoup

URL = 'https://pypi.org'

response = requests.get(URL)
soup = BeautifulSoup(response.text, features='html.parser')

links = soup.find(attrs={'aria-labelledby': 'pypi-trending-packages'})('a')
for link in links:
    name, version = link.h3('span')
    description = link.p
    url = URL + link['href']
    data = [name.string, version.string, description.string, url]
    print(','.join(data))
