import requests
from bs4 import BeautifulSoup
from os import remove, rename

# exe = 'dist/risi.exe'
exe = 'risi.exe'
tmp = exe + '.tmp' 

def get_latest_version_num() -> str:
  r = requests.get('https://github.com/GGetsov/risi/releases/latest')
  html = r.text
  soup = BeautifulSoup(html, 'html.parser')
  try: 
    latest_version = soup.find_all("h1")[3].string
    return latest_version
  except Exception:
    return "0.0.0"

def download_release(version: str):
  r = requests.get(f'https://github.com/GGetsov/risi/releases/download/v{version}/risi.exe')
  with open(tmp, 'wb') as file:
    file.write(r.content)

def replace_exe():
  remove(exe)
  rename(tmp, exe)
