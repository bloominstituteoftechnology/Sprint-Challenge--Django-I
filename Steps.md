
1. create a folder for the project

These steps will install Django and basic app

2. ```pipenv install django``` will add Django to the project  

3. type ```pipenv shell```

4. ```django-admin startproject djorg .```

5. Now try to run ```python manage.py runserver``` you should be able to run the app on ```http://127.0.0.1:8000/```

6. once we create a project then we have to create our app 
    ```python manage.py startapp bookmarks```
    PLease check this to know more about each file and its purpose
    ```https://djangoforbeginners.com/hello-world/ ```

Note: the following steps are appliccabe for Heroku


4. ``` pipenv install gunicorn``` - the webserver for Heroku to use (rather than the one built-in to Django)

5. ```pipenv install psycopg2-binary``` PostgreSQL client binaries

6. ``` pipenv install python-decouple``` - set important/secret values as environment variables

7. ``` pipenv install whitenoise ``` - optimizes deployment of static files (you may not have any, but it's good to add this now)

8. you always can create ```pip freeze > requirements.txt``` and add dependencies there this is like creating your own package.json

Till here the environmnet should be prepared and ready.

9. Prepaaring the Project

	a. Create ```.gitignore``` file if is ont yet created
	b. Create .env file and make sure you don't push it (add it to gigignore file)

Note: Pipenv & Virtualenv are differents but they do the same 
   Pipenv is a dependency manager for Python projects &&
   virtualenv is a tool to create isolated Python environments. 
   virtualenv creates a folder which contains all the necessary executables to use the packages 
   that a Python project would need.
   It can be used standalone, in place of Pipenv.

Important before to get to the point of migrating you have to call index in the app views
in this case bookmarks/views.py

10. create the models into the app in this case bookmarks and then run:
    ```python3 manage.py makemigrations```

Once you have your new migration files, you should apply them to your database to make sure they work as expected:
    ```python3 manage.py migrate``` 
    do not forget import ```import dj_database_url```

for databse ```pip install dj-database-url``` this will set avalability for ```dj_database_url```
set the ```.env``` file : Do not forget ```from decouple import config``` adding config in settings.py on djogr app

   



















