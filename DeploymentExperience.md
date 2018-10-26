Things that went well during the deployment process:
The process of installing the heroku dependencies for the application were very straight forward. Along with creating the application in the termianl and have that push to the heroku terminal. THe syntax implementation for the most part was pretty seamless, couple of errors regarding the env file but was able to work through them. 


Things that were tricky during the deployment process:

After the application was deployed the biggest problem that I was having was getting the migrations to work on the heroku server. I had to delete all the previous migrations, upload them to the server, and fix the camelcasing on Procfile in order for it to assign the web: variable. I then had dyno issues and had to look up kill operations to terminate a operation that never executed and then was able to create a super user. 
