# Axhon Ruiz

The deployment went pretty smoothly, thanks mostly to how well the heroku CLI runs. I was able to run most of the commands without fail on the first try.
One problem I am having, however, is with the ALLOWED_HOSTS and DEBUG env vars on my deployed instance.
Currently it shows that DEBUG=True so django is showing the rocketship. I ran `heroku run manage.py shell` so that I could run `from decouple import config` and then print the value of `config('DEBUG')`. From that shell it says the variable=False, so I am lost on what to do next.

Another issue I'm having is with the stretch goal of setting up ALLOWED_HOSTS. I tried appending to an empty list conditionally, but that failed. I also tried having a list that looks like `[config('ALLOWED_HOSTS')]`, but that failed.

Overall, I am happy that I was able to deploy to heroku, and that it was not a hard time doing so. I need to do a deeper dive into dj-database-url and the static file helper so that I can understand what they really do.
