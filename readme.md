# Intro

This demo shows how an input file is attached to a model, as well as programmatically create a processed file to the model.

# How to run

```bash
# Make a virtualenvironment
python -m venv .venv

# activate it
source .venv/bin/activate # for Linux/MacOS
.venv\Scripts\activate.bat # for Windows CMD
.venv\Scripts\Activate.ps1 # for Windows PowerShell

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# start server
python manage.py runserver
```

Now you can use your browser, go to http://127.0.0.1:8000,
choose a PNG image, hit submit,
You should then see the original file (in `media/input`), as well as a thumbnail (in `media/output`).
