# Hello-Django
Repo for playing with basic Django usage
--------------------------------------------------

This repository is for validating and demonstrating a basic Django installation.
Your goal is to create a basic initial Django project - if you have Python
and `pip` installed, this should be pretty straightforward.

```
python --version  # Should be >3
pip --version     # Should be >9
```

The `requirements.txt` file describes project dependencies, and `pip` can use it
with:

```
pip install -r requirements.txt
```

Note that before doing this you may want to set up an environment with
`virtualenv` (more details soon).

This will give you Django 2.0.2, which you can verify by running:

```
python -m django --version  # Should be 2.0.2
```

Now you can add your project! Django includes a command line tool `django-admin`
that can be used to do this:

```
django-admin startproject hello
```

This will make a directory with various files in it, notably `manage.py` (which
you will use to start the app and generally interact with it) and
`hello/settings.py` (which controls the settings of the app). `cd` into `hello`
and try running:

```
python manage.py runserver
```

If it works, you'll be able to load the page locally and should see something
like this:

![Screenshot of fresh Django project](https://raw.githubusercontent.com/LambdaSchool/Hello-Django/master/success.png "Success!")

If it doesn't, read the error, read the documentation, and ask for help. Common
issues include needing to apply migrations (`python manage.py migrate`) and (if
you're using Docker) needing to edit `ALLOWED_HOSTS` or set up the ports (you
can specify port at runtime by e.g. `python manage.py runserver 8000`).

Once you have it working, add and commit your new project so we can check it out
and give help/feedback. We'll be working on a much more substantial project
soon, but if you can't wait you can follow the
[tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/) to keep
adding features to this one.
