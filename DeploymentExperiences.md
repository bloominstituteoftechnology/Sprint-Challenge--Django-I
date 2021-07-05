- Summarize the key steps in the deployment process. 
  - What went well?
  Project Set Up went well, which involed the following:

  Sign Up for Heroku and Install the Heroku CLI

  I already had a Heroku account and Heroku CLI installed in my computer prior to the Sprint.

  The installing of new dependencies went quick and seemless.
  I cd into the project folder and ran pipenv shell to launch the virtual environment and proceed to install the following:

    1) pipenv install gunicorn - which is the webserver for Heroku to use, in place of the one built-in in Django

    2) pipenv install psycopg2-binary - which is the PostgreSQL client binaries

    3) pipenv install dj-database-url - which enables parameterizing the database connection so Heroku uses PostgreSQL but local is still SQLite
    
    4) pipenv install python-decouple - which sets the important secret values as environment variables in the .env file
    
    5) pipenv install whitenoise - which optimizes deployment of static files and is useful if you have views etc.
    
    6) We also needed to create a requirements.txt file in the project root directory by running this in terminal: 
    
      pip freeze > requirements.txt

  I prepared my project by doing the following:

    I typed ALLOWED_HOSTS=localhost,127.0.0.1
            DATABASE_URL="sqlite:///db.sqlite3"
            SECRET_KEY= -placed my secret key here-
            DEBUG=True
       into my .env which I placed in my .gitignore to hide.

    In djorg/settings.py, I added import dj_database_url as required and added 'smurf-app.herokuapp.com' into the empty ALLOWED_HOSTS list to allow heroku to host my smurf-app.

    Orginally, I placed:

            DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

            db_from_env = dj_database_url.config(conn_max_age=500)
            DATABASES['default'].update(db_from_env)

    in djorg/settings.py and changed it later to:

            DATABASES = {}

            DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'), conn_max_age=600)

    because I thought I had hit an error. I found out later that either works.

  I made a Procfile to tell Heroku what to run to start my smurf-app. I typed web: gunicorn djorg.wsgi --log-file - in the body of the Procfile.

  Even if I did not use any static files, I configured whitenoise by adding static settings to djorg/settings.py:
  
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

  I then made the project and added Heroku as a remote to my git repository so I could push to it to deploy by running this in terminal: 
  
    heroku create smurf-app

  Next, I made a PostgreSQL database associated with the project and set the DATABASE_URL Heroku config var, equivalent to a local environment variable by running this in terminal:

    heroku addons:create heroku-postgresql:hobby-dev

  After, I set the other Heroku config vars by logging in to the Heroku Dashboard in my browser.

  Lastly, I commited and pushed to github then deployed to Heroku by running this in terminal:

    git push heroku master

  - What challenges did you face? 

  To test if my smurf-app had deployed successfully on Heroku, I entered this in the browser and tried to log the admin user in:

    https://smurf-app.herokuapp.com/admin/

  I got this error:
  
   ProgrammingError at /admin/login/ 
   
   "auth_user" does not exist django Heroku

  I did a quick google and found out the hard way that I needed to run this in terminal:

    heroku run python manage.py migrate

  I also ran this to check that all migration ran successfully:

    heroku run python manage.py showmigrations

  After doing this, I was able to access my paths through: 

    https://smurf-app.herokuapp.com/api/

  and found out that the database was empty. I could not login because there was no superuser access in the database yet. A serious amount of googling happened after that. Until I found out that I could not import my existing sqlite3 database into heroku.

  I then decided to create a new superuser for the heroku database so I could access my app by running this in terminal:

    heroku run python manage.py createsuperuser

  I was able to create a superuser and use the access to login, add a second user, add smurfs under each user, DELETE a smurf with the admin user, and GET the respective information while logged into the respective user accounts.

  NOTE: I would have been able to avoid the headache of the extensive googling had I just read the sprint instructions all the way through.

  - How far did you get?

  I was able to deploy my app on Heroku.

- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
  I only really used training kit except when I needed to install sqlite which I had to google how to do. I used this
  resource for that http://johnatten.com/2014/12/07/installing-and-using-sqlite-on-windows/

  I also used the articles in the heroku docs.

  https://devcenter.heroku.com/articles

  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

  They are an easy read and very clear.

