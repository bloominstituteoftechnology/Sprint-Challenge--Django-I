# Sprint-Challenge--Django-I

Deployment Experiences:

Note: I used pipenv and worked inside the shell.

The steps to deploy were lacking to for Windows10 to say the least:

1. I had to manually reinstall all dependencies as follows:  `pipenv install -r path/to/requirements.txt` to import a requirements file.
2. the app crashed on deployement several times until I added :`# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())` at the very bottom of settings.py
