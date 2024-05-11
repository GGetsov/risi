import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/GGetsov/risi/releases/latest')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.find("span", string="Assets").parent.parent.prettify())
print(soup.find_all("h1")[3].string)
# for link in soup.find_all('a'):
#   # print(link.get('href'))
#   link = link.get('href')
#   if "/GGetsov/risi" in link: print(link)
