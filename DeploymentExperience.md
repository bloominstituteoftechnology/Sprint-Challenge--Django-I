A Link to deployed site: 

https://lambnotecs10.herokuapp.com/

* add `admin` to the link to go directly to the admin page

* add `api` to the link to go directly to the api page

--------
Deployment Experience:

Today I started this sprint challenge with a Django project rep. 

I created a pipenv virtual environment for my django project to live, created that project and created an app to be associated with it called notes. Because the main purpose of today's exercise was to deploy, I opted not to bother with Personal Notes and decided a class of Notes would be enough for demo purposes. 

The important part of this deployment process was correctly instantiating .env variables that 
would be used for deployment and double checking to be sure correct dependencies were installed. Because we are using Heroku, a Procfile needed to be created in the root directory of the project as well. 

The part of the deployment process that was super buggy for me was actual deployment. Because my environment used Python 3.7 and Heroku only supports up to 3.6.6, I had to investigate how to essentially 'downgrade' my Python version to the version needed for deployment. This is where the runtime.txt file comes in. Heroku will see this file and change the python runtime to the version that is listed in the file so it will deploy properly. 

I also created the procfile to automatically perform migrations upon successful deploy. This is what the release statement does in the procfile. 

Upon going to the site, we see a 404 not found, but that's okay! navigate to `/admin` and you will see that the admin site works. I needed to create a new superuser through `heroku run` CLI. Once I did that I was able to log in and perform admin functions. 

Navigating to `/api` also allows us to add notes. Right now, because I don't have permissions restricted, anyone who visits the site can add a note. I know this is a NEED TO FIX area of my app, but I wanted to go through a complete start to deploy on a Django project in the given time. Because my project from earlier in the week is so louse with files and possibilities for error, I wanted a clean slate to make this sprint less frustrating for myself. 

