# my-private-journal
A private journaling, Django web application

# Installation
1. Install [Python 3.8.2](https://www.python.org/downloads/).
2. Create a Python virtual environment via `python3 -m venv <virtual-environment-path>`.
3. Activate the virtual environment via `source <virtual-environment-path>/bin/activate`.
4. Download this repository via `git clone git@github.com:LesterKim/my-private-journal.git`.

# Viewing
1. Go into the repository via `cd my-private-journal`.
2. Install package dependencies via `pip install -r requirements.txt`.
3. Migrate the database via `python manage.py migrate`.
4. Run the server via `python manage.py runserver`.
5. Go to http://127.0.0.1:8000 to see the list of journal entries.
5. Go to http://127.0.0.1:8000/add to add a new entry.

Superuser/Admin
1. Create a superuser via `python manage.py createsuperuser`.
2. Go to http://127.0.0.1:8000/admin and put in your username and password to access the admin UI; make sure you are running the server.

# Biggest Issue
I ran out of time to add delete and update. I could have just forked a Github repository with the skeleton for a private journal web application and made style changes, but I would have a shallower understanding of the code.

# Learning Takeaways
This was my first time creating an web application in Django, so I learned how one of the most popular Python framework functions. Fortunately, the official [Django documentation](https://docs.djangoproject.com/en/3.0/) is well-written. As I was working on this, I was surprised by how I can get away with creating only one data model.

# What Could Be Done Differently
Aside from allowing delete and update, I would like to replace the default SQLite database with PostgreSQL because the latter can handle larger data. Of course, we could have used Flask, Express.js, or some lighter, less opinionated framework since the core functionality of this application is simple. Finally, I would like to be able to authenticate a user.
