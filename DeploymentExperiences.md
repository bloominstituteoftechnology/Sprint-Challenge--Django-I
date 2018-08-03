# Axhon Ruiz

The deployment went pretty smoothly, thanks mostly to how well the heroku CLI runs. I was able to run most of the commands without fail on the first try.
One problem I am having, however, is with the ALLOWED_HOSTS and DEBUG env vars on my deployed instance.
Currently it shows that DEBUG=True so django is showing the rocketship. I ran `heroku run manage.py shell` so that I could run `from decouple import config` and then print the value of `config('DEBUG')`. From that shell it says the variable=False, so I am lost on what to do next.
