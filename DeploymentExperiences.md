- Summarize the key steps in the deployment process. 
1. Sign up for Heroku (if you haven't yet before) || Install the Heroku CLI
2. Sign into Heroku via your terminal --> `heroku login` || Move into the repo directory already if you haven't yet
3. Install the dependencies (pipenv install.... gunicorn, psycopg2-binary, dj-database-url, python-decouple, whitenoise)
4. `pip freeze > requirements.txt` || if you haven't yet, create a `requirements.txt` file at the root directory and then run the code on the left
5. Fill out `.env`!
6. Add your config vars in the `settings.py` (check your djorg repo for reference)
7. Create a `Procfile` and paste the code for the log-file
8. `heroku create your-app-name`
9. `heroku addons:create heroku-postgresql:hobby-dev`
10. Add the config vars onto your heroku project via the broswer (on your Heroku dashboard for your via the `settings` tab!)
11. `git push heroku master` || NOTE: you may have to run `heroku run python manage.py migrate` after deployment and create a new superuser via `heroku run python manage.py createsuperuser` once deployed so you can create new login credentials for the heroku-deployment version.
  - What went well?
    - Deployment to Heroku felt so smooth and easy to follow. The only issues I had faced during the deployment process were small typos in the command line!

  - What challenges did you face? 
    - I would say the only challenged I faced was myself. I got so excited to deploy successfully that I would create many typos when setting up the code for deployment! Deploying to heroku, after following the directions, felt so simple and easy!

  - How far did you get?
    - I got to deploy my django app successfully and created a new superuser for the heroku-app as well to check if the website would be functional (and it is!).

- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
    - The `Heroku Dev Center` docs were so extensive and answered all my questions I had at the beginning! They're super fleshed out and navigating through the docs were super simple and quick. Another document that I found useful was the `README`. It really guides you through what you should be doing each step of the way, and more importantly doesn't give us every direct answer and instead links us to other official documentation!

  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 
    - `Heroku Dev Center`. With its simple and fleshed out navigation system, to fleshed out documentation for each tab, the `Heroku Dev Center` really made bug-fiing easy!

