import requests
from bs4 import BeautifulSoup
from os import remove, rename

exe = 'dist/risi.exe'
tmp = exe + '.tmp' 
r = requests.get('https://github.com/GGetsov/risi/releases/latest')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
latest_version = soup.find_all("h1")[3].string
r = requests.get(f'https://github.com/GGetsov/risi/releases/download/v{latest_version}/risi.exe')
with open(tmp, 'wb') as file:
  file.write(r.content)
remove(exe)
rename(tmp, exe)


