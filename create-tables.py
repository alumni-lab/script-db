import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS movies, characters, quotes
        """,
        """
        CREATE TABLE movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL
        )
        """,
        """ 
        CREATE TABLE characters (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE quotes (
            id SERIAL PRIMARY KEY,
            quote VARCHAR NOT NULL,
            character_id INTEGER REFERENCES characters(id)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()