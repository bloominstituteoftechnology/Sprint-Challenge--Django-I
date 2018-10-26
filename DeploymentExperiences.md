Deployment is always tricky -- it either works, or you're stuck debugging for a few hours. Luckily, this time around, I was able to deploy with no issues. After deploying multiple applications via Netlify, Heroku, and Surge (although Netlify and Surge make it super easy), I am getting used to the whole process and learning from my previous mistakes. Deploying a Django application was not too different, and here were the steps I took to get a smooth deployment:

- Using python-decouple, allowing me to use a .env file.
- Using gunicorn, which connected my application with heroku
- Using dj-database-url, which allowed for a sqlite3 connection locally, and a PostgreSQL connection in production
- Using psycopg2-binary, which allowed for PostgreSQL client binaries
- Using whitenoise, which optimizes deployment of any static files
- Creating a Procfile, which tells Heroku what to do to start the app
- Configuration for the aforementioned libraries
- Creating a PostgreSQL database within Heroku
- Setting up environment variables in Heroku
