- A link to your Djorg project repo: https://github.com/LambdaSchool/Hello-Django/pull/84

- A link to your live site, if you were able to deploy: 
https://hello-django-kfly.herokuapp.com/

https://hello-django-kfly.herokuapp.com/admin/login/?next=/admin/
USERNAME: kfly
PW: LambdaCS9

(added one note successfully to test)

- A `DeploymentExperiences.md` file where you write summarizing how the process went for you, what went well and what was tricky, and how far you got

Kaitlyn's Summary:
Started off with installing my heroku CLI and installing all the dependencies. I hit a small bump with generating a new SECRET_KEY, but was able to work through that and got that setup. Then I setup my Procfile and implemented the needed code to configure `whitenoise` within my project.

Hit some stumbling blocks along the way and was having issues deploying to Heroku, but this was because I had my Heroku config vars setup incorrectly. Once I made those fixes, my app now successfully deploys on heroku (YAY!) but my issue I've been trying to debug now is getting my notes to display. Right now when I got to my webpage, I see `Application Error`. My notes project was working locally as of this morning, but now that also seems to be broken. Going to keep hacking to see if I can get it fixed! Overall, it has been a great learning process to overcome some challenges. 

UPDATE: Turns out after doing some major digging that the issue preventing me from seeing my login page on Heroku was a procfile issue. Earlier when going through the process, I labeled my procfile with a lowercase p. I later decided to change this to be capitalized and have committed changes and didn't think anything of it. Doing some debugging, I ran `heroku ps:scale web=1 to discover "Scaling dynos...! Couldn't find that process type". My commits still showed my procfile with a lowercase P, so I deleted my procfile, commited/pushed, recreated Procfile with capital P this time, committed/pushed and when I ran the `heroku ps:scale web=1` command again it gave me a result I wanted to see of `Scaling dynos... Done!" When I pushed to heroku master I can now view the login page. I created a superuser and can now succesfully log in and create notes! 
