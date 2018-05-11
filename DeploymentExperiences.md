## Deployment Experiences
The first time I deployed to Heroku was during the backend project week with a notes app. I had put together a fairly simple app that attempted to utilize Google OAuth, which was quite a challenge. I had it *mostly* functioning, though it is still not fully connected. It otherwise had no issues deploying to Heroku.

This project has been fun. While setting things up in general kept me back for a time, it didn't take much time at all to catch up and get where I needed to be. Issues I had are Windows Related, and at this point deploying to Heroku is a little confusing for me. I read the docs and try to follow and implement what is stated but I'm sure I'm far from correct on what to do.

I was able to of course install the necessary dependencies with no issue. Confusion for me came in the database. I'm not exactly sure how to load the DATABASE_URL properly or how to pass it to dj_database_url.config. Then there's the Procfile. It's pretty botched, though I want to believe it's going in the right direction. I added a Procfile.Windows under the assumption it may be necessary for Windows. I could possibly get away without that I assume, so I may go delete it and see what happens.

Configuring whitenoise seemed to be pretty straightforward and I believe I have it set up properly. Creating the heroku app was exactly the same as before so that was not an issue. Setting the Heroku config vars seemed pretty simple, both from Heroku CLI and from the web dashboard. But there's a good chance I didn't do something properly there. Deploying to Heroku lead to issues.

At the top of the error log is
##### python manage.py collectstatic --noinput

This probably has to do with the Procfile not being set properly.

Following the list the next real noteable error I see is

##### DATABASES[`default`] = django.db.backends.sqlite3(conn_max_age=600)
#####    NameError: name 'django' is not defined

So, back to where the DATABASES are set, I know I did not set something up properly, so I will rework it and see what I can figure out. It gives an option to disable collectstatic, which I believe I could try out just to see what happens. It ends with

##### Push rejected

So obviously, there are a few bugs I need to go back to correct. I will continue to work on this project and try to correct the issues.