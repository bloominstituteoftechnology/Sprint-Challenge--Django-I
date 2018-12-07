- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
  - We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 


My project is deployed to:
https://django-blue.herokuapp.com/admin/

My project on Github:
https://github.com/Csillag61/Intro-Django
https://github.com/LambdaSchool/Intro-Django/pull/175 


Deployment is a tricky thing -- it either works, or you're stuck debugging for ever.   After deploying 1 react application via Netlify (notes_app), and 2 backend projects viaHeroku I am getting used to the whole process and learning from my previous mistakes. 

Here were the steps I took to get a smooth deployment:
•Using python-decouple, allowing me to use a .env file.
•Using gunicorn, which connected my application with heroku
•Using dj-database-url, which allowed for a sqlite3 connection locally, and a   PostgreSQL connection in production
•Using psycopg2-binary, which allowed for PostgreSQL client binaries
•Using whitenoise, which optimizes deployment of any static files
•Creating a Procfile, which tells Heroku what to do to start the app
•Configuration for the aforementioned libraries
•Creating a PostgreSQL database within Heroku
•Setting up environment variables in Heroku

All of the provided documentations were extremely helpful, I have learned again to follow the instructions very carefully, or else... meaning unwanted bugs.
The Intro to Django guides and the step by step instructions to deploy gave me a very good base to start from. 
Everything considered, it was a great learning experience pushing me further than I've been before.
