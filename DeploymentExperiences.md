## DeploymentExperiences

Heroku account and loggin information was gether and used to download and run the local Heroku CLI app. 

For the Django app set up: 
-Commands run: 
 'pipenv shell' was launched
  then 'pipenv install django' was run
  then 'pipenv install' was run for: gunicorn, psycopg2-binary, dj-database-url, python-decouple, and whitnoise
  
-Then a requirements.txt file was made in the root folder. 
-Then to set up the database, 'pipenv install dj_database_url' was run and imprted into settings with DATABASES configured. 
-A Procfile was added to the root directory with 'web: gunicorn djorg wsgi'. 
-Whitenoise was configured in Settings with a few lines above MIDDLEWARES to allow for service of static files. 
-Then connection to heroku happenened with 'heroku create my firstdjangoapp'. 
-More configuring was done with addons and the heroku link was added to ALLOWED_HOSTS in settings. 
-Heroku was then deppplayed with 'git push heroku master'. 
Then connection to heroku happenened with 'heroku create my firstdjangoproject1'. 
-More configuring was done with addons and the heroku link was added to ALLOWED_HOSTS in settings. 
-Heroku was then deppplayed with 'git push heroku master'. 

Links: 

https://myfirstdjangoproject1.herokuapp.com/ | https://git.heroku.com/myfirstdjangoproject1.git