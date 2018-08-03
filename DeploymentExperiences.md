- A link to your Djorg project repo: https://github.com/LambdaSchool/Hello-Django/pull/84

- A link to your live site, if you were able to deploy: (still working on bug fixes to show notes, but it does deploy!)
https://hello-django-kfly.herokuapp.com/

- A `DeploymentExperiences.md` file where you write summarizing how the process went for you, what went well and what was tricky, and how far you got

Kaitlyn's Summary:
Started off with installing my heroku CLI and installing all the dependencies. I hit a small bump with generating a new SECRET_KEY, but was able to work through that and got that setup. Then I setup my Procfile and implemented the needed code to configure `whitenoise` within my project.

Hit some stumbling blocks along the way and was having issues deploying to Heroku, but this was because I had my Heroku config vars setup incorrectly. Once I made those fixes, my app now successfully deploys on heroku (YAY!) but my issue I've been trying to debug now is getting my notes to display. Right now when I got to my webpage, I see `Application Error`. My notes project was working locally as of this morning, but now that also seems to be broken. Going to keep hacking to see if I can get it fixed! Overall, it has been a great learning process to overcome some challenges. 
