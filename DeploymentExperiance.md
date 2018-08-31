

``` https://djorgnote.herokuapp.com/ ```

My Deployment experience was straight forward. I followed the instruction given and it worked well. 
The first part was installing new dependencies, the next step was to copy the .env file from the sprint to 
the one already setup and generating a new SECRET-KEY using django radom string generator once done with that
.
ALLOWED_HOSTS and DATABASE_URL. 
Allowed hosts was a bit tricky since allowed_hosts in the .env was separated by comma, I ended up using .split(',') that solved that. 
For the Database, the documentation was useful and configured the setting file with ```DATABASES['default'] = dj_database_url.config(default=...) ```
For the Procfile, I created a new file in the root and with it and the logo changed to the heroku logo and that gave me the confidence that what I did was right
For the whitenoise, the documentation was helpful and copies the requied files in the setting file. 

