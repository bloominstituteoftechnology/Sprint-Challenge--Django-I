
Intro-Django Repository: https://github.com/katiagilligan888/Intro-Django

Heroku Deployed Site: https://instgram-data.herokuapp.com

This part of the project was definitely the most challenging part of my week. Instead of setting up the static files and white-noise on my own, I used a library called django-heroku to do the settings configurations. This library did not have a lot of documentation which was definitely a challenge to the process of setting up the heroku server. I initially did not knkow what the library boilerplate code did to my files which made it a challenge to follow the rest of the instructions in the READ.ME. However, with a little research I realized that I needed to add a requirements file and a Procfile and pass the heroku to the ALLOWED_HOSTS in the settings. 

The hardest part of the project was understanding what project name to add to the Procfile. I wasn't sure if it was the name of the heroku project or the name of my folder and so I had to experiment and change some things around until I got to the solution. 