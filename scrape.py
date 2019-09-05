import requests
import re
import character

from bs4 import BeautifulSoup
r = requests.get('https://www.imsdb.com/scripts/Lord-of-the-Rings-Fellowship-of-the-Ring,-The.html')
text = r.text

# setup tables herer
import psycopg2         #psycopg2 is a Postgres database adapter for Python
from config import config

print("Database opened successfully")

def insert_movie(title):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO movies(title)
             VALUES(%s) RETURNING id;"""
    conn = None
    movie_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (title,))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return id

def insert_character(name):
    sql = """INSERT INTO characters(name)
             VALUES(%s) RETURNING id;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name,))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return id

def insert_quote(quote, characterID):
    sql = """INSERT INTO quotes(quote, character_id)
             VALUES(%s, %s) RETURNING id;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (quote, characterID))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return id

# insert_movie("The Lord of the Rings: The Fellowship of the Ring (2001)")
# insert_character("Golem")
# insert_quote("My Precious...")

####################

quote_dictionary = {}

soup = BeautifulSoup(text, 'html.parser')

# get random character to pull quotes from
names = character.allCharacters()

for name in names :
        if name :

                characterID = insert_character(name)

                quote_dictionary[name.upper()] = []
                quotes = soup.find_all("b", text = re.compile(f'.*{name.upper()}.*'))
                
                for quote in quotes:
                        quote_text = quote.nextSibling

                        if quote_text.name == None :
                                
                                quote_text_split = quote_text.split('\n')
                                
                                quote_text_stripped = []

                                for quote_text in quote_text_split :
                                        quote_text_stripped.append(quote_text.strip())
                                
                                quote_text_joined = " ".join(quote_text_stripped)

                                if quote_text_joined != " " :

                                        insert_quote(quote_text_joined, characterID)

                                        quote_dictionary[name.upper()].append(quote_text_joined)
                        

# print(quote_dictionary)