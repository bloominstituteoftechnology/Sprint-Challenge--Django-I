# Deployedd sucessfuly:
* Had to include: ```# DJANGO RECOMMENDED FOR DEPLOYING TO HEROKU
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')``` inside the settings.py of djorg.
* Had to also inlude CORS: installled the package in the pipenv, and conffiguured it with the following lines inside the settings.py 
```
 'corsheaders', # CORS HEADERS inside Installed Apps Section
 'corsheaders.middleware.CorsMiddleware', # Inside the Middlewares section
 CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
```
* I couldd now acess my api from any endpoint locally, and even from my own reacct front end application.
# After deployment: Using Heroku CLI
* I sucessfuly ran migrations
* Sucessfuly created a superuser
* Sucessfuly set Config variables on the heroku app settings tab for SECRET_KEY, ALLOWED_HOSTS, DATABASE_URL, DEBUG.
* Sucessfuly was able to even runserver through the CLI, but the app address kept returning error, and unavailable acess at that endpoint.
* I might be missing an essential piece of the puuzzle which might be to have the Django server run on a speciffic port on the heroku dyno. Will have to research further. However my app works and functions locally on both front and back endd.
