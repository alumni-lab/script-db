import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html')
text = r.text

soup = BeautifulSoup(text, 'html.parser')

print(soup.pre.text)
