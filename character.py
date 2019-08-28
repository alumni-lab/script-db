import requests
import re
import random

from bs4 import BeautifulSoup



def allCharacters() :
    imdb = requests.get('https://www.imdb.com/title/tt0120737/fullcredits?ref_=tt_cl_sm#cast')

    text = imdb.text

    soup = BeautifulSoup(text, 'html.parser')

    characters = soup.find_all("td", {"class": "character"})
    character_names = set()

    for i in characters:
        name = i.findChildren("a")
        # print(name) 
        if name :
            character_names.add(name[0].text)
            # print(name[0].text)

    return character_names