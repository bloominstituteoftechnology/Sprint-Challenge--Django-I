Djorg Repo:
https://github.com/jamiemd/djorg

Deployed Site: (errored)
https://mydjorg.herokuapp.com/


The deployment experience has been challenging since I didn't quite understand some of the instructions. I got through installing the dependencies but the "Prepare your project" step was tricky. I was able to get it deployed but the page doesn't load because of an error. For the times I was stuck, I googled many of the error messages to see if other people had the same issue. There were answers and it was a matter of trying different things. However, I eventually got stuck on the " heroku run python manage.py migrate" step which kept erroring.

Here is the error: 
DATABASES = {'default': dj_database_url.parse('DATABASE_URL', conn_max_age=600) }
  File "/Users/jamiedomingo/.local/share/virtualenvs/djorg-L8Qy3KBe/lib/python3.6/site-packages/dj_database_url.py", line 103, in parse
    engine = SCHEMES[url.scheme] if engine is None else engine
KeyError: ''