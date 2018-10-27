Everything went relatively straightforward, per the readme.

The following setting required additional research, in order to  correctly identify correct syntax.



ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
DATABASES = {
   'default': dj_database_url.config('DATABASE_URL', default='sqlite:///db.sqlite3'),
}

THe whitespace documentation required time in order obtain the required parameters needed, which reduced the amount of time for debug within the allotted timeframe.

The initial deploy had 2 related problems, the "git push heroku master" for the deploy was aborting with the following:

remote:        Your Pipfile.lock (e64405) is out of date. Expected: (40bf6b).
remote:        Aborting deploy.

possible solution:

delete pipfile.lock --- successful
run pipenv install to generate a new lock file yielded this error:

C:\Users\rverd\Intro-Django>pipenv install
Pipfile.lock (e64405) out of date, updating to (40bf6b)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
er.py", line 76, in main
    system=system,
  File "C:\\Users\\rverd\\AppData\\Roaming\\Python\\Python37\\site-packages\\pipenv\\resolver.py", line 63, in resolve
    allow_global=system,
TypeError: resolve_deps() got an unexpected keyword argument 'verbose'.

the solution...move the"env" file out of the way(rename)

pipenv install then worked

tried to deploy again...which failed

StackOverFlow, hinted at a possible corrupt requirements file
which was regenerated with a pip freeze>requirements.txt.

seemed to resolve my deploy issues finally.

Now the deployed app did not startup.

running "heroku logs --tails" yielded the following:

File "/app/.heroku/python/lib/python3.7/importlib/__init__.py", line 127, in import_module
2018-10-26T23:16:53.282218+00:00 app[web.1]: return _bootstrap._gcd_import(name[level:], package, level)
2018-10-26T23:16:53.282255+00:00 app[web.1]: ModuleNotFoundError: No module named 'OddJobBoard.settings' "oddJobBoard" was chnged to "apps" in the "wsgi.py" and the application worked. The aforementioned error message was mis-interpreted originally and thought the problem was in the "settings.py" file....this actually lasted for several hours as we moved files around and made changes to the files structure, all of which were unnecessary.

