# Experiences deploying a Django app to Heroku

I experienced a number of challenges here, from not having dependencies properly declared for heroku to install them, to not being able to access the site at all (getting 404 Bad Request errors) due to not having my ALLOWED_HOSTS variable set properly.

Another issue involved not understanding that SQLite does not work on Heroku, and exactly how to configure things to work with PostgreSQL. I have a much better conception of Heroku architecture after powering through those difficulties.

Overall things went well, and I did manage to get the remote deployment working as I expected, though I did not have time to setup a frontend/homepage.
