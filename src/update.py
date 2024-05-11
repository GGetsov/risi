import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/GGetsov/risi/releases/latest')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
latest_version = soup.find_all("h1")[3].string
r = requests.get(f'https://github.com/GGetsov/risi/releases/download/v{latest_version}/risi.exe')
with open('dist/test.exe', 'wb') as file:
  file.write(r.content)
