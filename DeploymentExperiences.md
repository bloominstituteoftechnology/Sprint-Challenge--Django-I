https://github.com/LambdaSchool/Intro-Django/pull/130

https://adb-roster-app.herokuapp.com/api/roster/

My deployment process went surprisingly smoothly.  Granted, I mostly owe this to being able to watch Ronald's fantastic walk through of how to deploy.  
The only real hiccup i encountered was getting the heroku CLI installed.  Because i'm using a WSL environment, the sudo snap install did not work for me.  I ended up using curl https://cli-assets.heroku.com/install-ubuntu.sh | sh and it seemed to work as intended.  Between the README and Ronald's video I was able to navigate the rest of the deployment very smoothly.