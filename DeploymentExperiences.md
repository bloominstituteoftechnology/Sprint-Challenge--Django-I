# Wladimir Fraga CS10

## Project djorg PR

https://github.com/LambdaSchool/Intro-Django/pull/20

## Heroku backend deployment

# API
https://djangodashboard.herokuapp.com/api/

# admin
https://djangodashboard.herokuapp.com/admin/

# Sprint-Challenge--Django-I

For this project I'm going to address only the main steps in order to deploy a Django app in Heroku.

* [X] ```Note: the instructions below assume you're on your `master` branch in git.```

* [x] 5. Install new dependencies. (If using `virtualenv`, use `pip install` as you have been, or migrate to `pipenv`.)

    This steps are important for deploy in Heroku, similar when you use webpack, so when you miss one of these you will see a H10 error like this:

    ```2018-08-31T16:27:50.131415+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=djorgnotes.herokuapp.com request_id=-xxxx?????ssssxxxx fwd="50.29.204.9" dyno= connect= service= status=503 bytes= protocol=https
2018-08-31T16:27:50.267594+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=djorgnotes.herokuapp.com ```

    * [x] 1. `pipenv install gunicorn` - the webserver for Heroku to use (rather than the one built-in to Django)
    * [x] 2. `pipenv install psycopg2-binary` - PostgreSQL client binaries
    * [x] 3. `pipenv install dj-database-url` - enables parameterizing the database connection (so Heroku uses PostgreSQL but local is still SQLite)
    * [x] 4. `pipenv install python-decouple` - set important/secret values as environment variables
    * [x] 5. `pipenv install whitenoise` - optimizes deployment of static files (you may not have any, but it's good to add this now)
    * [x] 6. If using `virtualenv`, you need to create a `requirements.txt` file in your project root directory with the command: `pip freeze > requirements.txt`

6. Prepare your project

    * [x] 5. You can use `config` to load the environment variables you set above, e.g. `SECRET_KEY = config('SECRET_KEY')` (`ALLOWED_HOSTS` will be a little trickier, but that's why this is a sprint challenge!)

      ``` In order to acheive this inside your .env file you should add the enviroment variable ALLOWED_HOSTS and assign some values like: ```

          ALLOWED_HOSTS=localhost,127.0.0.1
 
      ``` Your settings.py file has the same variable name which is an array with the all the hosts allowed but is necesary to convert to an array: ```
      
          #Replace
          # ALLOWED_HOSTS = [
          #   '127.0.0.1',
          #   'localhost',
          # ]
          
          # With
          ALLOWED_HOSTS = list(config('ALLOWED_HOSTS').split(','))

    * [x] 8. Configure `whitenoise` (add a few configuration lines to your `settings.py` file per the [documentation](http://whitenoise.evans.io/en/stable/))

      ```You need this in order to be able to use CSS inside your app, here is the reason: ```
      
      The main problem with this approach is that Amazon S3 cannot currently selectively serve compressed content to your users. Compression (using either the venerable gzip or the more modern brotli algorithms) can make dramatic reductions in the bandwidth required for your CSS and JavaScript. But in order to do this correctly the server needs to examine the Accept-Encoding header of the request to determine which compression formats are supported, and return an appropriate Vary header so that intermediate caches know to do the same. This is exactly what WhiteNoise does, but Amazon S3 currently provides no means of doing this.
