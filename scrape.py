import requests
import re
import character

from bs4 import BeautifulSoup
r = requests.get('https://www.imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html')
text = r.text

quote_dictionary = {}

soup = BeautifulSoup(text, 'html.parser')

names = character.randCharacter()

for name in names :
    if name :
        quote_dictionary[name.upper()] = ["hello","world"]

print(quote_dictionary)

quote = soup.find_all("b", text = re.compile(f'.*{name}.*'))[0].nextSibling

# print(f'{name}: {quote}')
