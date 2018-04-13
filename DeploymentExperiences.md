I followed Sprint-Challenge steps, deployed my app by the 2nd try, did the migration, but there are errors in the log file, failed to deploy the app.
Summarisation of the Deployment:
# 1. Spent lots of time of step 6: Prepare your project.
## 1. Don't know how to setup the dotenv file: read some old study materials, then created .env file under root directory, and put .env into .gitignore file
## 2. Don't know how to setup config for SECRET_KEY, ALLOWED_HOSTS, DATABASES['default']: google searched , found some example, and modified djorg/djorg/settings.py and .env files, didn't see error about these configs.
## 3. First deployment failed because "collectstatic--noinput", then close collectstatci by config:set collectstatic=1; second deployment succeeded, but could not open the app. Checked the log, because Procfile didn't set up correctly. Modified a little bit, still could not open the app. 


Link to my repo: https://github.com/leelali/djorg
