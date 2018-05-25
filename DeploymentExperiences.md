# Deployment Experience

Today's assignment of deploying our Django application to Heroku went fairly well. I had a much easier time with this than when I attempted to deploy my MERN application. I did run into a few hiccups, but nothing that I could not figure out eventually.

After installing all of the dependencies, I edited my `.env` file to include the correct settings for my local environment. Then, I made the appropriate changes to the `settings.py` file. This includes importing some of the new dependencies that we installed, setting the correct Database URL, and setting up the application to properly handle static files with WhiteNoise.

The static files is actually what gave me the most trouble. However, by doing some research on my error messages, following a few tutorials and reading some documentation, I was able to locate the issue. The problem was that `python manage.py collectstatic` was not running correctly. After making a few changes and creating a `STATIC_ROOT` folder, I was able to get it working locally, but it still kept failing when trying to push to Heroku. Finally, I realized that I had not commited the new folder yet. This solved the problem and I was able to push to Heroku immediately after.

The final steps simply involved running the migrations on Heroku and setting the Heroku config variables. Now the application is up and running!

For the most part, I was able to get everything done simply by following the instructions and reading the documentation. The only difficulties came while trying to debug some of the errors I was faced with. Overall though, it went quite well.