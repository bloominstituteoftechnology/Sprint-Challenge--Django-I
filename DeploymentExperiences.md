Heroku is pretty easy to work with and I've used it a few times before this
so I didn't have much of an issue with heroku itself. I didn't realize it was so
easy to spin up a postgres database on heroku and it immediately just worked.  
  
The only real issue I ran into with heroku was that it didn't like some of the 
hardcoded static file URLs which was easy to fix.
  
The biggest issue I ran into in general was that I wasn't aware I needed to reload 
pipenv locally to refresh changes to my .env file which took me a good half hour
to realize.