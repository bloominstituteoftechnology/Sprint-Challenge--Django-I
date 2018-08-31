### What went well?
Steps 1-6.5 went smoothly with no problems. I was able to 
- successfully prepare my project for deployment
- create a new heroku app
- create a postgres database
- deploy my project to heroku
- create a superuser account

### What was tricky?
I had trouble when loading the `DATABASE_URL` and passing it to `dj_database_url.config`. I followed the instructions in the documentation and used this line in settings.py: 

```python
DATABASES['default'] = dj_database_url.config('DATABASE_URL')
```

I got this error message when trying to run the server:

    "ImproperlyConfigured at /admin/

    settings.DATABASES is improperly configured. Please supply the ENGINE value."

After some exploring, I found that setting a default database fixed the issue.

```python
DATABASE_URL = config('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config('DATABASE_URL', default=DATABASE_URL)
}
```

Next, I ran into a problem with setting up static files. I needed to add a directory for static files and save that path in a variable `STATIC_ROOT`

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### How far did you get?
I deployed my application and created a superuser account. For some reason, though, I'm not able to load the live site. It crashes and I'm not sure why.