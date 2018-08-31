# Deployment Experience

* [Intro Django Repo](https://github.com/d-vail/Intro-Django)
* [Live Admin Panel](https://intense-plateau-87266.herokuapp.com/admin/)
  - username: ls-sprint-review
  - password: LS08312018&
* [Live API](https://intense-plateau-87266.herokuapp.com/api/)

I prepped for the depolyment process by reviewing the issues I had deploying my backend project to ensure this deployment was not at risk for the similar issues. The most time consuming problem that I ran into deploying my backend project arose from the decision to use Heroku, instead of Netlify, to house my frontend and properly linking it to the backend. In its current form, the Djorg project is strictly backend, removing the possibility of running into the previous issues I had.

This deployment was fairly quick and smooth. Most of the time was spent waiting for dependencies to install. `python-decouple` was already installed on my project. I did need to add `gunicorn`, `psycopg2-binary` and `dj-database-url`. `whitenoise` is a good thing to install if your project uses static files. This project did not but I included it to get practice deploying static files.

My first build failed. The build log showed that the staticfiles app was improperly configured:

      django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.

`STATIC_ROOT` is the absolute path to the static files directory. When using the static files app, this is where that app will place all static files. The fix was to either remove the static files app (a valid option since this project does not use static files) or define the static root. I choose to define the static root and added the following to the `settings.py` file:

      STATIC_ROOT = os.path.join(BASE_DIR, 'static')

The second build was successful but the application crashed. The log showed a ModuleNotFoundError for gettingstarted. The lesson learned here was do not copy and paste from guides without understanding why that step is needed. I previously copied the Profile from Heroku's Getting Started guide which tried to start up my app with gettingstarted.wsgi. The fix was to use my project name and call djorg.wsgi.