- Summarize the key steps in the deployment process.
  - What went well?
  - What challenges did you face?
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past.

In this deployment sprint challenge I had the most problems at the very beginning. After installing heroku I had trouble being able to login, which ended up taking about 3 hours to solve but ended up being about 20 seconds worth of time writing the correct path and command in the terminal. After being able to successfully log into heroku the next step was installing all the dependencies I would need, which included whitenoise, python-decouple, dj-database-url, psycopg2-binary and gunicorn. Now it was time to prepare the project. I had to get a new secret key by running code in a python repl and printing it, then using config to load the environment variables, SECRET_KEY = config('SECRET_KEY'). After that came time to load DATABASE_URL and pass it to dj_database_url.config, then make a procfile to tell heroku to start the app. Lastly I configured the whitenoise install and added static settings to settings.py.

Now it was time to run heroku create my-app in the terminal to make the project and adds heroku as a remote to my git repo so I could push to it to deploy. After that I had to make a PostgreSQL database associated with the project and set the DATABASE_URL heroku config variable with this command in the terminal, "heroku addons:create heroku-postgresql:hobby-dev". Once I then set the other heroku config variables like ALLOWED_HOSTS, DEBUG, and SECRET_KEY in my heroku dashboard I was ready to deploy after committing and pushing with git push heroku master.

I felt like some of the docs were more straightforward than others, such as the whitenoise doc. However the doc for loading and passing the DATABASE_URL to dj_database_url.config took me a little more time to decipher exactly what to do.




https://agreb17-djangosprint.herokuapp.com/admin/
https://github.com/agreb17/Intro-Django