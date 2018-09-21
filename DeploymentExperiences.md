-  pipenv freeze > requirements.txt couldnt install because pip command couldnt found. I ran 'sudo easy_install pip' command that I found on stackoverflow.

- pip install dj-database-url also couldnt install so I ran sudo.

- raise ImproperlyConfigured("You're using the staticfiles app "
remote:        django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.

Found solution to add 'STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")' to the settings.py

- I was able to deploy but getting not found 400 error. So I changed ALLOWED_HOSTS to  ['*'].