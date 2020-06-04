- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 


Deploying to Heroku with Python Django

paragraph 1 – steps to deployment
paragraph 2 – overall experience with the deployment process

The steps I took to deploy to Heroku are as follows. I was using a virtual environment for deployment. I started that up with pipenv shell. Then I installed gunicorn, psycopg2-binary, dj-database-url, python-decouple, and whitenoise. Since I was in a virtual environment I added a requirements.txt file at the root of my directory and did the command pip freeze > requirements.txt so that all the required add-ons for my project where imported. I then filled out my .env file with all the relevant variables. I then set up my database to run locally with sqlite3 and with PostgreSQL on Heroku in my settings.py file. I made a Procfile in the root of my directory letting Heroku know what to run when my app is loaded up. I then created my Heroku app, set up its config vars, pushed to Heroku master, migrated the database, and added a superuser through the Heroku console.

I did get stuck a few times making sure everything was filled out in my Procfile. I overlooked that the Procfile, requirements.txt, and the project itself needs to be in the root of the git repository for it all to work which lead to problems. In the end I was able to complete the deployment. I personally found all the docs helpful in completing this assignment.  I think the code examples in the debug section really helped me make sure I was on the right track and also with finding any possible errors. I also really liked how the docs talked about running Heroku logs command to figure what if anything was wrong. This helped me because I was able to see that Heroku could not find my project when it was trying to run. I then made sure my project was at the root directory so the Procfile could pick it up.

