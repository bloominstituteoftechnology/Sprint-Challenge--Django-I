Deployed project: https://django-super-notes.herokuapp.com/api/

djorg repo: https://github.com/LambdaSchool/Intro-Django/pull/78

The installation of dependencies went well with the installation of the Heroku CLI. For the ALLOWED_HOSTS environment variable, when setting it in the .env file, I had to parse each host in order to let the project know what hosts are allowed. The DATABASE_URL lets the project know where the sql db file is. I forgot to set the STATIC_ROOT file which is supposed to say, where are the files that need to be served up at?
