Live site: https://charles-djorg.herokuapp.com/admin
username: admin
password: password
Project url: https://github.com/sherlock270/Intro-Django

I didn't run into many issues during deployment, but there were a couple speed bumps:

- I had to reinstall django cors
- Had to set STATIC_ROOT in settings.py. Documentation wasn't clear on this until I hit an error

Some other points of note:

- Heroku performed migrations when I pushed which was nice
- Steps in the readme to deploy were a little fuzzy in places, but I had no issues
  figuring out what I needed to do from various documentations
- I also hit a small bump when I set Heroku's 'ALLOWED_HOSTS' to what I had in my
  .env file. When I went back to the readme I realized Heroku's 'ALLOWED_HOSTS'
  was different from my local development environment 'ALLOWED_HOSTS'
