**GitHub:** **[https://github.com/harrisonbrock/Sprint-Challenge--Django-I]()**

**Heroku:** **[https://py-notes-app.herokuapp.com/admin/]()**

**API Login:** **[https://py-notes-app.herokuapp.com/api-token-auth/]()**

**API Notes:** **[https://py-notes-app.herokuapp.com/api/note]()**

__Deployment Experiences__


This deployment was not all that hard because I have deployed to the Heroku cloud platform in the past. 
The only difference this time was I needed to set up a few configuration variables for the database URL,  DEBUG, Secret-Key.  The tricky one was DISABLE_COLLECTSTATIC. I got an error when trying to deploy, and the error message was to set DISABLE_COLLECTSTATIC to 1. With all these variables set I was able to deploy 