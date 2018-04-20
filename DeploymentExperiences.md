1.  Summarize how the process went for you, what went well and what was tricky, and how far you got.  
    _answer_  
    I found the process to be extremely frustrating. At first all went well. I signed in to my Heroku accoun.t I had already installed the CLI in a previous deployment. I logged in from the terminal, and then moved into my djorg folder. I encountered no problems when installing dependencies, creating the .env file, creating a new secret key, and creating required new imports. I used a resource from the web to create my "ALLOWED_HOSTS" but ultimately ended up changing it to

    ```ENVIRONMENT = 'production'
       DEBUG = False
       ALLOWED_HOSTS = ['django-sprint-challenge.herokuapp.com'
    ```

    toward the end of the deployment.  
     I had trouble with the databases portion, specifically with determining the URL for my database, but ended up going with `'sqlite:////Users/metten/Desktop/Lambda/djorg/db.sqlite3'` based on the documentation. I have no idea if this is correct. I created the Procfile and originally gave it the contents of `web: gunicorn djorg.wsgi`. I configured whitenoise, created the heroku app, took care of add-ons, and config var without any obvious incident, although any of these steps could contain my problem. After completing all steps, I went to deploy and got the following error:  
     `[remote rejected] master -> master (pre-receive hook declined)`
    In an attempt to fix, I tried the following: reinitializing the app, changing the Procfile contents, changing the DATABASES content in `settings.py`, changing SECRET_KEY language in `settings.py`, switching to a temp branch and attempting to push from there, and even logging out and back in to Heroku from the CLI. None of these efforts were successful.
