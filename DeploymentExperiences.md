the deployment process is very easy but there is some steps to do

- we init git in the root folder of the app
- install and login to heroku and we add it a a second remote origin in git
- we install "gunicorn" , "psycopg2-binary","dj-database-url", "python-decouple"," whitenoise"
- we state the allowed hosts in the the projects settings.py file
- we make DEBUG = Fale
- we add "whitenoise.middleware.WhiteNoiseMiddleware" to middleware in the settings.py
- a add more code to setting.py:
  db_form_env = dj_database_url.config(default=DATABASE_URL)
  DATABASES['default'].update(db_form_env)

- we add this line of code to .env file : DATABASE_URL="sqlite:///db.sqlite3"
- we start hereku app "heroku create your-app"
- we set herohu secret key
- we make sure that all migrations are sent to the database
- we add add and commit changes to git
- we push changes to heroku master and origin master

in general is it not that difficult to deploy on heroku but there is lot of commands to follow and many dependencies to install, google will give a good help in the steps
