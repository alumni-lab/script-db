import requests
import re
import character

from bs4 import BeautifulSoup
r = requests.get('https://www.imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html')
text = r.text

soup = BeautifulSoup(text, 'html.parser')

name = character.randCharacter().upper()

quote = soup.find_all("b", text = re.compile(f'.*{name}.*'))[0].nextSibling

print(f'{name}: {quote}')
