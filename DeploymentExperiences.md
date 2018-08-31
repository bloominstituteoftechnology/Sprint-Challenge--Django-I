## NOTE: This repo is the codebase for the deployed application.

LINK TO DEPLOYED APP:
https://hondabookinventory.herokuapp.com
## NOTE: Remember to add /api or /admin, or else the link will not work.

### Experience 

- Most of the deployment process was fairly straightforward; I started by following the Readme.md file through Step 6. Then, I joined the after hours to get a refresher on Heroku deployment, which got me through deployment, but I had an issue with the ALLOWED_HOSTS. 

- I reached out to some of the other students who were participating in the after hours review, and they gave me suggestions on formatting the ALLOWED_HOSTS data in the .env file. Ultimately, Amy discovered that I was trying to call the root of the application, which caused an issue because our project did not have a root. After trying /api and /admin, everything works as expected.

- At some point in the debugging process, a traceback recommended that I reconfigure my staticfiles directory _or_ run $ heroku config:set DISABLE_COLLECTSTATIC=1 in order to run properly.

- To test functionality, I created a superuser _lambdaSkewl_ and tried some queries, and everything works perfectly. 