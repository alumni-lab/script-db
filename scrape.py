import requests
import re
import character

from bs4 import BeautifulSoup
r = requests.get('https://www.imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html')
text = r.text

quote_dictionary = {}

soup = BeautifulSoup(text, 'html.parser')

# get random character to pull quotes from
names = character.randCharacter()


# print(quote_dictionary)




# print(f'{name}: {quote}')



for name in names :
        if name :
                quote_dictionary[name.upper()] = []
                quotes = soup.find_all("b", text = re.compile(f'.*{name.upper()}.*'))
                
                for quote in quotes:
                        quote_text = quote.nextSibling

                        if quote_text.name == None :
                                
                                quote_text_split = quote_text.split('\n')
                                # print(quote_text)
                                quote_text_stripped = []

                                for quote_text in quote_text_split :
                                        quote_text_stripped.append(quote_text.strip())
                                
                                quote_text_joined = " ".join(quote_text_stripped)
                                
                                if quote_text_joined != " " :
                                        quote_dictionary[name.upper()].append(quote_text_joined)
                        

print(quote_dictionary)