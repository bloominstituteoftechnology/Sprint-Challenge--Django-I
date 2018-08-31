# Deployment Experiences
## Deploying Django Backend to Heroku

My Django deployment was successful, and generally went smoothly. Some issues 
that I experienced:

* <u>Improper setup of `whitenoise`.</u><br/>
A missing configuration line in `settings.py` led to a `STATIC CONTENT` error 
during deployment. That was resolved after some light digging in `whitenoise` 
doku.

* <u>`dj_database_url` problems with Sqlite3</u><br/>
I cannot properly access the local Sqlite3 database with `dj_database_url`. 
**Heroku and Postgre work fine**, so _no action taken_ yet to resolve this.

That is the extent of it. The deployment guide in this repo's `README.md` 
walked me through the process and prevented the introduction of a lot of issues.
The documentation for the invididual dependencies also aided in deployment. 
Finally, Heroku itself has a comprehensive guide for deploying Django 
applications to the service.

---

Github repository: https://www.github.com/mister-corn/Intro-Django<br/>
Heroku App: https://guarded-headland-70198.herokuapp.com/api/cards/