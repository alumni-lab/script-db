Project setup
=============

Create database.ini file based on database.ini.example

On Mac:

```
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

On Windows:

```
python3 -m pip install --user virtualenv
python3 -m venv env
source env/Scripts/activate
pip install -r requirements.txt
```

Heads up! Always run one of the following

```terminal
source env/bin/activate
source env/Scripts/activate # For Windows
source env/bin/activate.fish # For Nima
```

when you start development.

To start scraping, create a "quote_chat" database on PSQL and run

```
python3 create-tables.py
python3 scrape.py
```