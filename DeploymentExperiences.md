## Deployment

Deployment went smoothly, but app crashes on start up both on deployment and locally. App was working as intended prior to attempting deployment, and is giving me an error listed below involving code that I did not touch. Googling for an answer is not yielding much result.

* Installed new dependencies
* Generated new secret
* Updated .env file
* Added new imports to setting.py
* Updated settings
* Created Procfile
* Configured whitenoise
* Ran heroku create mwaus-django
* Created heroku postgres add on
* Set heroku env variables
* Deployed to heroku
* Deployment appears to have been successful per the logs:
  ```
  remote: Compressing source files... done.
  remote: Building source:
  remote:
  remote: -----> Python app detected
  remote:  !     The latest version of Python 3.6 is python-3.6.6 (you are using python-3.7.0, which is unsupported).
  remote:  !     We recommend upgrading by specifying the latest version (python-3.6.6).
  remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
  remote: -----> Installing python-3.7.0
  remote: -----> Installing pip
  remote: -----> Installing dependencies with Pipenv 2018.5.18…
  remote:        Installing dependencies from Pipfile.lock (341136)…
  remote: -----> Installing SQLite3
  remote: -----> $ python manage.py collectstatic --noinput
  remote:        152 static files copied to '/tmp/build_2de55b59c620471213fb21d97b8c1b84/staticfiles'.
  remote:
  remote: -----> Discovering process types
  remote:        Procfile declares types -> web
  remote:
  remote: -----> Compressing...
  remote:        Done: 68.3M
  remote: -----> Launching...
  remote:        Released v7
  remote:        https://mwaus-django.herokuapp.com/ deployed to Heroku
  remote:
  remote: Verifying deploy... done.
  To https://git.heroku.com/mwaus-django.git
  * [new branch]      master -> master
  ```

  * Ran migrations on heroku with no errors
  * Created superuser on heroku with no errors

  * Entire app now crashes on startup even locally, giving me this error:
    `django.core.exceptions.ImproperlyConfigured: WSGI application 'djorg.wsgi.application' could not be loaded; Error importing module.`
    