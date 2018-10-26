Deploy Application on Heroku

Error code H14
https://devcenter.heroku.com/articles/error-codes#h14-no-web-dynos-running


If your Heroku deployment works the first time without any errors, you should check your pulse.  Fortunately, this warning was heavily reiterated to me by my instructors.  I was anxious jumping into the process because I knew I would have to correct mistakes, no matter how meticulously/methodically I followed the prescribed process. The key componenets for setting up a Heroku App with a Django backend can be summarized as follows:

- Get up and running with Heroku.  That is get make an account and install the CLI https://www.heroku.com/

- Install the dependencies you need in order to deploy:
    - gunicorn (a webserver for Heroku to use)
    - psycopg2-binary (PostgreSQL client binaries)
    - dj-database-url (enables parameterizing the database connection)
    - python-decouple (to set secret variables, etc.)
    - whitenoise (optimizes deployment of static files)

- Prepare the project.  This is the part for which you would want to reserve the greatest mental focus as the steps are deailed and need to be followed precisely.

- Create the App with Heroku and configure your variables in settings (these config vars resemple your .env file)

Obviously, this is not a full tutorial, merely a breakdown of the process.  

One thing that can be scary about the deployement process is that many steps need to happen prior to the actual deployment.  This makes it feel like you're flying blind to a certain extent.  We can't pinpoint the errors until we have actually deployed.  Once deployment to Heroku has taken place, the first sign of a problem will be on the live site. When I clicked on my site, which takes the form, https://greenline-server.herokuapp.com/admin, all I got was an application error.  There was also the recommended command: $ heroku logs --tail.  When I ran this command in the terminal, I saw several versions of the same error H14.  After investigating this error on the web, I learned that the problem most likely lies with my Procfile.  It took me a while to notice that I had made a mistake in naming the Procfile with a lower case "p" instead of an upper case.  I renamed the Procfile and pushed to Heroku again.  This still did not resolve there error and this is where I am now ...



