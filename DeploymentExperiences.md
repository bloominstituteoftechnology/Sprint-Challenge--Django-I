Links to Heroku

Admin login
https://books-collection-app.herokuapp.com/admin/

Login Credentials:
Username:test
Password:testu46299

Heroku Api access after login
https://books-collection-app.herokuapp.com/api/booksapp/


Link to Project Repo:

https://github.com/sukhadagholba/Intro-Django



Experiecne Deploying Booksapp to Heroku:
My deployment went fairly well expect for the two major blockers mentioned below:

1. The deployment failed the first time since the project name was incorrent in the Procfile. After chnaging the name to the right directory the deployment was successful.

2. The second problem I encountered while deployment was - my static files were missing and as a result there was no CSS on my django admin tempelate. I was missing the STATIC_ROOT settings in my setting.py. On adding the settings I was able to view the template with CSS styling.

Other than the two major blockers mentioned everything went pretty smooth. 

