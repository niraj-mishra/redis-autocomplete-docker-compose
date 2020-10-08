# Autocomplete-Redis
Implementing autocomplete functionality using redis and Python.

Tech Stack-

Flask

Third party libraries-

1. Redis

2. flask

3. python-dotenv

-----

**Setup docs-** 

Navigate to Autocomplete-Redis folder and run command below if you are using linux machine
and run command below


$ pip install -r requirements.txt

$ `export FLASK_APP=autocomplete.py`

$ `flask run`

make sure to change redis url in .env file if deploying

----

API Endpoints =>

    To add words

**http://127.0.0.1:5000/add?name=niraj**

    To get words

 **http://localhost:5000/suggestions?prefix=ni**
