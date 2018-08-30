1. I followed the deployment steps provided in the repo. The only step that took some extra digging was the ALLOWED_HOSTS variable since Django’s ALLOWED_HOSTS expects a list of host names and not a single string. For that I referenced https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html. I believe the function used parses the ALLOWED_HOSTS values in the .env and once it encounters a comma it inputs the preceding characters into the list as a list item. It also strips whitespace around the values if applicable.   

2. For the last step I ran the command -> git push heroku master <- and it resulted in the following error: 

django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.
 !     Error while running '$ python manage.py collectstatic --noinput'.
       See traceback above for details.
       You may need to update application code to resolve this error.
       Or, you can disable collectstatic for this application:
          $ heroku config:set DISABLE_COLLECTSTATIC=1 


To resolve this error I created the DISABLE_COLLECTSTATIC config variable on the heroku dashboard and set it's value equal to 1. 

3. Afterwards, the project deployed successfully. I created 2 superusers using the command -> heroku run python manage.py createsuperuser <- and tested the endpoints using curl in the terminal. The requests returned expected data. 