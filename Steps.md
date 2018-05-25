
1. create a folder fr the project

2. run ``` virtualenv env-name ```

Note: the following steps are appliccabe for Heroku

3.``` pipenv install gunicorn``` - the webserver for Heroku to use (rather than the one built-in to Django)

4. ```pipenv shell```

5. ```pipenv install psycopg2-binary``` PostgreSQL client binaries

6.``` pipenv install python-decouple``` - set important/secret values as environment variables

7.``` pipenv install whitenoise ``` - optimizes deployment of static files (you may not have any, but it's good to add this now)

8. If using ```virtualenv```, you need to create a requirements.txt file in your project root directory with the command: pip freeze > requirements.txt```

Till here the environmnet should be prepared and ready.

9. Prepaaring the Project

	a. Create ```.gitignore``` file if is ont yet created
	b. Create .env file and make sure you don't push it (add it to gigignore file)
	c. 




















