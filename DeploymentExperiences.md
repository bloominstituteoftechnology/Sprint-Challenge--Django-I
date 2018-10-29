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

One thing that can be scary about the deployement process is that many steps need to happen prior to the actual deployment.  This makes it feel like you're flying blind to a certain extent.  We can't pinpoint the errors until we have actually deployed.  Once deployment to Heroku has taken place, the first sign of a problem will be on the live site.  For example, when I clicked on my site, which takes the form, https://greenline-server.herokuapp.com/admin, all I got was an application error.  There was also the recommended command: $ heroku logs --tail.  When I ran this command in the terminal, I saw several versions of the same error H14.  After investigating this error on the web, I learned that the problem most likely lies with my Procfile.  It took me a while to notice that I had made a mistake in naming the Procfile with a lower case "p" instead of an upper case.  I renamed the Procfile and pushed to Heroku again.  This measure was not enough to solve the problem.  In order for the change to take effect, I had to delete the Procfile completely, push the changes to github without the Procfile, then create a new Procfile, push to github again, and then push to heroku.  This corrected the problem.  I struggled with this for a while and ended up getting help from a classmate.  I found it very helpful to discuss the problem with him and get some additional troubleshooting ideas.  I'm not good about asking for help, I tend to struggle alone for too lone.  I'm taking a mental note this time how important it is to do this!   



