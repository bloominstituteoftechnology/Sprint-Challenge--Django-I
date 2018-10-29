* My experience with deployment was fairly straightforward and successful. 
* I utilized the django-heroku python library to make settings configuration easy.
* After installing django-heroku, I simply imported the library in settings.py and added `django_heroku.settings(locals())` to the bottom of the file.
* I then only needed to add a Procfile and requirements.txt file, as well as setting my config vars via the heroku dashboard, to be able to successfully deploy with the expected results.


