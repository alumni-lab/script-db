Project setup
=============

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