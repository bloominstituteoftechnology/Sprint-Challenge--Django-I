# Sprint Challenge: INTRO TO DJANGO - DEPLOY TO HEROKU

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint explored the basics of Django. During this Sprint, you studied how to setup a Django project, build a REST API, and use token authorization. In your challenge this week, you will demonstrate proficiency by taking the application that you built over the course of this week and deploying it! Getting your application out there is a great way to learn, shake out bugs,
and get feedback as you can share it with others. 

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and Django and your command of the concepts and techniques covered during the Intro to Django Sprint.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

In this challenge, you will be documenting your experience in creating a Django project and using [Heroku](https://dashboard.heroku.com/) to deploy the application you built over the course of this sprint. 

In meeting the minimum viable product (MVP) specifications listed below, your application will be accessible remotely via Heroku's servers as demonstrated in the following screen-shot. 

(placeholder img)

![Todo Deploy MVP](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdSBBVXq6sA4ZRRXvoojXBdfJe8LmBO4muCiMxJnO-P9UbVjNgjQ)

You will also create a short written piece documenting your experience.
![Todo Writeup](/imgs/two_paragraphs.png)


## Self-Study/Essay Questions

This portion of the challenge is meant to allow you to practice your
*professional* writing skills. In the tech world, that means writing things clearly,
concisely, in a way to get the information across efficiently to an audience that may be pretty busy. 

It is suggested that you limit your response to the questions below to one or two paragraphs. Keep your answers short and to the point. Consider how much of an online resource people typically view.

![Stats](/imgs/reading_stats.png)

from [How People Read Content Online](https://www.go-gulf.ae/blog/how-people-read-content-online/)

Demonstrate your understanding of this week's concepts by answering the following free-form questions. With your final submission, complete the `DeploymentExperiences.md` file where you write about the experience of your Heroku deploy. 

- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

You are expected to be able to answer all these questions. Your responses contribute to your Sprint Challenge grade. Skipping this section *will* prevent you from passing this challenge.

## Project Set Up

Note: the instructions below assume you're on your `master` branch in git.

The steps to deploy (at a high level) are:
1. Sign up for [Heroku](https://www.heroku.com/)

2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. From your terminal, `heroku login`
4. Get to your project/repo directory
5. Install new dependencies. (If using `virtualenv`, use `pip install` as you have been, or migrate to `pipenv`.)
    1. `pipenv install gunicorn` - the webserver for Heroku to use (rather than the one built-in to Django)
    2. `pipenv install psycopg2-binary` - PostgreSQL client binaries
    3. `pipenv install dj-database-url` - enables parameterizing the database connection (so Heroku uses PostgreSQL but local is still SQLite)
    4. `pipenv install python-decouple` - set important/secret values as environment variables
    5. `pipenv install whitenoise` - optimizes deployment of static files (you may not have any, but it's good to add this now)
    6. If using `virtualenv`, you need to create a `requirements.txt` file in your project root directory with the command: `pip freeze > requirements.txt`
6. Prepare your project
    1. Copy the `dotenv` file in this repository to `.env` in your repository (this should *not* be checked in)
    2. `ALLOWED_HOSTS` and `DATABASE_URL` are probably already correct for your local environment, but read/understand them
    3. Use the example code (you can just run it in a `python` repl) to generate a new secret key and change `SECRET_KEY`
    4. `djorg/settings.py` will need new imports (`from decouple import config` and `import dj_database_url`)
    5. You can use `config` to load the environment variables you set above, e.g. `SECRET_KEY = config('SECRET_KEY')` (`ALLOWED_HOSTS` will be a little trickier, but that's why this is a sprint challenge!)
    6. For the database, you want to both load the `DATABASE_URL` and pass it to `dj_database_url.config` (see [documentation](https://github.com/kennethreitz/dj-database-url))
    7. Make a `Procfile` ([example](https://github.com/heroku/python-getting-started/blob/master/Procfile)) to tell Heroku what to run to start your app. (Hint: the name of your Django project is probably "djorg", not "gettingstarted".)
    8. Configure `whitenoise` (add a few configuration lines to your `settings.py` file per the [documentation](http://whitenoise.evans.io/en/stable/))
    9. Add static settings to your `settings.py`:
       ```
       STATIC_URL = '/static/'
       STATIC_ROOT = os.path.join(BASE_DIR, 'static')
       ```
7. `heroku create your-app` - makes the project and adds Heroku as a remote to your git repository so you can push to it to deploy
8. `heroku addons:create heroku-postgresql:hobby-dev` - makes a PostgreSQL database associated with the project (and sets the `DATABASE_URL` Heroku config var, equivalent to a local environment variable)
9. Set the other Heroku config vars, e.g. `ALLOWED_HOSTS=.herokuapp.com`, `DEBUG=False`, and `SECRET_KEY=somenewsecret` - see the [documentation](https://devcenter.heroku.com/articles/config-vars), you can set either via the Heroku CLI or by logging in to the Heroku Dashboard in your browser
10. Deploy! _First, make sure you're all committed_. Then `git push heroku master`

Once you've got it deployed, you'll probably need to run migrations on Heroku
(since it's using a different database then local). You can do this with
`heroku run python manage.py migrate`, and in general
`heroku run python manage.py` is the way to do all the helpful Django things,
just "in production." For example, `heroku run python manage.py createsuperuser`
is a good thing to do, and you can even administer/explore the app/data with
`heroku run python manage.py shell` and `heroku run python manage.py dbshell`.

### Troubleshooting

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) - official tutorial, has a full working example app if you want to step through with that before you try with Djorg
- [Lambda School Python/Django resources](https://github.com/LambdaSchool/Getting-Started/blob/master/PythonDjango.md)

You may also find the `heroku logs` command useful to diagnose errors, as Heroku
error messages are usually not that descriptive. 

#### Bash prompt doesn't echo and RETURN doesn't go to the next line

Note for bash users: if you ever get in a place where your terminal isn't
printing out newlines properly and is not echoing your keypresses, hit `CTRL-C`
then blindly type in the following command and hit `RETURN`:

```
stty sane
```

#### Whitenoise incompatible with Version 4.0

If you get errors along these lines, make sure your `STATICFILES_STORAGE` is set to `Compressed` and not to `Gzip`.

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Example working `MIDDLEWARE` config:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

#### Modules installed locally, but not on Heroku

Make sure the module is in your `Pipfile`. If it's not, you probably installed
it with `pip` instead of `pipenv`.

If the module appears in `pip list`:

1. `pip uninstall modulename`
2. `pipenv install modulename`

Then try to redeploy.


#### Improperly configured databases

Error:

```
raise ImproperlyConfigured("settings.DATABASES is improperly configured. "
django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.
```

Try this in your `settings.py`:

```python
DATABASES = {}

DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'), conn_max_age=600)
```

Another option:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```


## Minimum Viable Product

Your finished project must include all of the following requirements:

- A link to your Djorg project repo
- A link to your live site, if you were able to deploy
- Completed summary of your deployment process in `DeploymentExperiences.md`

In your solution, it is essential that you follow best practices and produce clean and professional results. Schedule time to review, refine, and assess your work and perform basic professional polishing including spell-checking and grammar-checking on your work. It is better to submit a challenge that meets MVP than one that attempts too much and does not.

## Stretch Problems

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module but they build on the material you just studied. Time allowing, stretch your limits and see if you can deliver on the following optional goals:

- Teach others what you have learned about Django development. Write a blog post or short article. Consider easy-to-read formats like a how-to guide or top 5 list. Do NOT just publish your answers to the Self-Study/Essay Questions section. You may use this content as a starting point, but it must be expanded upon in a significant, transformative way. Or focus on one or two specific pieces of Django you explored this week and describe how to use them or why they are useful with a high level of technical detail. 

  Publish your writing on your own personal blog or website or submit it to a larger publication like [Medium](https://help.medium.com/hc/en-us/articles/213904978-Add-draft-or-post-to-publication) or [Hackernoon](https://hackernoon.com/about). Show that you completed this stretch goal by submitting the following in a seperate folder in your repo name `stretch_write`:
  - `DjangoExperiences.md` file with the final text.
  -  A link to the published piece ***OR*** screenshot showing your submitted it to be published on another site.
- Explore how [Heroku logging](https://devcenter.heroku.com/articles/logging) works. Try generating, retrieving, and filtering log messages from your app. Show that you completed this stretch goal by submitting the following in a seperate folder in your repo named `stretch_log`:
  -  A short paragraph describing the steps you took to implement logs, saved in `LoggingExperiences.md`. Include some of the statements you wrote to generate logs from within your application.
  - A screenshot that show logs being viewed from the terminal.
  - A second screenshot that shows logs being fetched with filtering arguments. Try fetching with filters at least two times, using different filters each time.
