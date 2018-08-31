### Intro-Django repo

https://github.com/LambdaSchool/Intro-Django/pull/18

### Heruku
https://note-with-django.herokuapp.com/


What's a Sprint Challenge and how I tackle it! 

This Sprint is like an adventure. I did a lot of researches, ran into a huge error, more research, ran several commands to debug them and Voila! 

First, I read though the whole instruction and try to summarize what the goal of this Sprint. I then simply follow the steps in Readme and also Edward's repo that he posted in CS10 channel yesterday which I found that's really helpful. 

I didn't have difficulties to implement these steps until I deployed the app to Heroku. I got an error `ModuleNotFoundError: No module named 'corsheaders'`. I installed it but error still exist. Then I found the comment in StackOverflown to run `python manage.py collectstatic` to find out that really happened locally and I got the error `ModuleNotFoundError: No module named 'django'`. That raised the flag that I might not be in virture env. 

I decided to delete the heroku app and started over. Then I had an issue with PostgreSQL because my new app had different name from the one I linked to the database. After changing the name back, linked the database again then migrated it. My heroku app is deployed. YAY! 
 