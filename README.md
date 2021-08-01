# Survival-Hydration API: A first attempt at using FastAPI

I've wanted to learn and practice some basics of FastAPI and have a bunch of water stored up. This was a perfect opportunity.
# Project Structure:

-/api: This folder holds the SQLite database, and the main FastAPI code. `main.py` runs the API.py file in this directory. The API returns only JSON/Python Dicts.

-/Utils: This folder contains `NumberTools.py`, a file I used for initial testing, and `AsyncNumberTools.py`, a file the project imports in order to query or update the DB and perform calculations.

-/Various Uses (To be renamed, yuck): This folder holds future implementations. I plan to make a basic web frontend, React frontend, Android app, email notifier, and basic text-to-speech program, all of which will be able to present the amount of water stored to the user. A Dockerfile will also be made at some point, but will be in the root folder.

-/: The project's root directory holds `main.py`, which calls Uvicorn to run the API, `setup_db.py`, which is used to make a template for the SQLite database, and `requirements.txt`, which holds the modules one would need to run their own instance, and can be installed using `python3 -m pip install -r requirements.txt`.

# Setup

If you ever want to set this up (which you probably shouldn't), there are three steps after cloning:
1. `python3 -m pip install -r requirements.txt`
2. `python3 setup_db.py`
3. `main.py`

By default, the program will run on localhost (127.0.0.1) at port 8000

# Usage

To use the API, simply send a GET request to `/supply` or `/calculate/{weight as integer}/`, or send a POST request to `/edit/{operation}/{liters}`. For example,`curl -X GET 127.0.0.1:8000/supply`.