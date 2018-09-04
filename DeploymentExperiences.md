Project Repo: 
https://github.com/holly-g/Intro-Django

Live Site:
https://intro-django-app.herokuapp.com/api/

Deployment Experience

The Good: After a considerable amount of sweat and tears, I was finally able to get the app to deploy. It's extremely bare bones, but it works.

The Bad: I lost a whole day's worth of productivity due to a sudden update for Chrome OS. It caused my Linux apps to become transparent and after trying out some different approaches, I had no choice but to powerwash and work out of the beta channel. It took me a while to get my environment set up.
Ultimately, I had to comment out rest_framework after testing the limits of my Google Fu. I had reinstalled it to make sure it was in the appropriate virtual environment; I also had it listed in installed apps and requirements.txt.
Moreover, it took me longer than it should have to realize that the python3-pip package was not installed correctly. I also had to deal with pipenv getting the wrong Python version. 

Overall, it was a good learning experience for me. I do feel that,after spending an excessive amount of time trying to debug, I have learned from these careless mistakes and will have a smoother time deploying my next Django app!