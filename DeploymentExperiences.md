Installation of all the dependencies went smoothly. Documentation for each of the dependencies was very thorough and kept me from making mistakes.

**Loading the environment variables**
- The dj_database_url.config default threw me off a bit. I am still not sure if my solution is correct. It works, but I think I just have two defaults. I plan on going back and playing with it a bit to see what works. 

- The ALLOWED_HOSTS settings threw me off the most because they weren't allowing me to access any part of the website. I didn't realize what the problem was until I dug through the heroku logs a little bit. Ended up being a simple fix, just took some time to figure out.

- The Procfile was a great lesson for me because I was unsure of what the point of it was. I realized, after loading the procfile with the wrong .wsgi, that it was supposed to point to the wsgi file that was responsible for loading the entire application. After changing the name to the appropriate directory, the site began giving me more thorough debugging clues.

**Heroku Issues**

- Because heroku seems to be running a seperate instance of my project, I had to remember that whatever I pushed into my own repository, I had to push to the heroku master as well. My corsheader was throwing an error because I had installed it incorrectly, and after fixing the issue on my local machine, it wasn't working on the heroku server. So I did another push to the heroku master and everything worked fine after that. This also applies to the migrations that I had to make to the heroku server. Was a good way of getting an understanding of how heroku is being deployed.


https://intense-beach-95351.herokuapp.com/

https://github.com/LambdaSchool/Intro-Django/pull/69
