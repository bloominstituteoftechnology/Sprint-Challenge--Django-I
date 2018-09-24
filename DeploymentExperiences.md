Project repo: https://github.com/LambdaSchool/Intro-Django/pull/64
Heroku site(not working): https://erin-meredith-django.herokuapp.com/

Deployment experience: I got through the steps without many problems, but when I got to deployment I recieved errors. I think the problem is how I configured DATABASE_URL. I followed the instructions in the documentation, but there's not much information I can find outside of that to figure out where I went wrong.
9/23/18 - Continued to work on the project over the weekend. I fixed the error I had on Friday (heroku error H14) by deleting the procfile and creating a new one, and changed DATABASES in settings. But now I receive error H10. My local server works fine, just can't get heroku to cooperate.