I ran into some confusion with the Heroku CLI early on with
-logging into Heroku
-using Heroku CLI at all/confirming installation
The solution came when I
-searched forums online
-added the step I missed which was using 'yarn global add Heroku' after the browser installation UI was complete
From there I installed all the dependencies pretty smoothly, altered the dotenv file as asked, read up on ALLOWED_HOSTS and DATABASE_URLS, and generated the new secret key after some trouble with repl.it upon which I used a python interpreter to complete the task
After addng imports, I attempted to add the other configurations to the project while dealing with some mild confusion on where they should be placed/if I were to create a new settings.py file or collaborate with the previous settings.py file from day 1-4 project
I'm currently in the process of clarifying if I am doing my configuratons correctly and attempting to deploy my project and find out 
-I have completed the Heroku create your app step and am trying to continue the following steps