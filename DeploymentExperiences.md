**summarize how the process went for you, what went well and what was tricky, and how far you got**


I ended up starting from scratch with a fresh repo to get some more practice with django.
Once the copy app was ready to deploy, I created a new heroku app and configured my local environment as well as the heroku app environment.
About one headache and 90 minutes later, I realized that there was a mix up in my heroku config variables.
For some reason heroku was storing the postgresql database url in a seperate variable from DATABASE_URL.
After moving a few variable names/values around, the app was successfully deployed.
I have yet to experience any enjoyment from the process of heroku web deployment. Might dabble with some AWS later.