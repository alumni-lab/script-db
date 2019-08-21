import requests
import re
from bs4 import BeautifulSoup
r = requests.get('https://www.imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html')
text = r.text

soup = BeautifulSoup(text, 'html.parser')

quote = soup.find_all("b", text = re.compile('.*GOLLUM.*'))[0].nextSibling

print(quote)
