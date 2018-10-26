

Deployment experience:

Deployment has been sticky.  I have been introduced to a lot of new modules, for various uses in deployment and production.  Getting my mind wrapped around their purposes added to the time it took to deploy.  (Mind you, "deploy" is used loosely, as my app is responding with a 404.)

THere were a few big blockers.  The biggest was the settings.py DATABASES reconfiguration with dj_database_url.  I had to read through quite a bit of 3rd-party literature and discussion before coming to a solution that worked.  

As I mentioned, my app has been deployed to Heroku.  However, when navigating to the URL, I receive a 404 response.  

NodeJS, historically, has been much simpler to deploy to Heroku for me.  Which I've done enough that I had to delete an app from Heroku in order to deploy this Django app.


URL: https://epilepsy.herokuapp.com
