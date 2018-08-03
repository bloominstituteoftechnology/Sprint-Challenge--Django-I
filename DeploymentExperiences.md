# Django I Sprint Deployment Experience

Overall smooth deployment with a few things that required extra attention to launch with no errors.
Link to heroku app: https://django-notes-app.herokuapp.com

* Chose to build off [Hello-Django project](https://github.com/cgoez/Hello-Django) rather than copy files to Django I Sprint repo.
------------------------------
* Setup Heroku and installed dependencies using `pipenv`.
* Replaced contents of `.env` with contents of `dotenv`.
  * Generated new SECRET_KEY.
* Config new environment variables.
* Load database.
* Create Heroku Procfile.
* Config `STATIC_ROOT` in `settings.py`.
------------------------------
* Create Heroku project and add Heroku remote to git repo.
  * `heroku create django-notes-app`
* Add PostgreSQL DB
* Set Heroku config vars via CLI
  * Double check and edit in Heroku Dashboard
* Debug, commit, deploy!
  * `git push heroku master`
------------------------------
* Django commands through heroku app:
  * `heroku run python manage.py`
* Check/make migrations
  * `heroku run python manage.py showmigrations`
  * `heroku run python manage.py migrate`
* Create new super user and check functionality
  * `heroku run python manage.py createsuperuser`

# Errors and Fixes:
`error: failed to push some refs to 'https://git.heroku.com/django-notes-app.git'`
* Add `STATIC_ROOT` in `settings.py`.
  * `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`

Heroku bad request (400)
* Add `".herokuapp.com"` to `ALLOWED_HOSTS` in `settings.py`
