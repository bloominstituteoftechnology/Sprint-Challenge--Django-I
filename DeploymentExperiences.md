# Issues during deployment

  #### Environment variables were not set in Heroku
  > Given that Heroku set up the DATABASE_URL for me I had assumed that it would automagically set up the rest. This was not the case so proceeded to set them up manually via the Heroku web app.

  #### ALLOWED_HOSTS not forming an array
  > The environment variable was translating to a string with each subsection divided by a comma. I used pythons split method to divide the string into an array.

  #### Placement of DATABASE['default] declaration
  > When setting up the DATABASE['default'] declaration I did not notice that the dictionary had not been defined above it. I had to move the line of code below the initial declaration.

  #### Static url not defined
  > Upon trying to push to Heroku it was giving me an error stating that I was using the staticfiles app without a STATIC_ROOT setting. I added a STATIC_ROOT filepath variable and I was able to deploy my Heroku server successfully

  <br>
  Server up on Heroku <a href='https://django-notes-api.herokuapp.com/'>here</a>