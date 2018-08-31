## Deployment Experiences

My deployment experience was relatively pain-free. I encountered a few bugs, but I was able to fix them quickly. The trick was to just stick to the steps laid out in the README. At first, however, the README appeared to me to be not very organized and explicit, so in my Task List (in the Pull Request), I broke the steps down into general categories. This helped clarify things in my mind. After that, implementation was faster.

When deploying to Heroku, I forgot to run "heroku run python manage.py migrate". Hence, the bugs. I then went and ran "heroku run python manage.py showmigrations" so I could see all the things that I needed to migrate, and migrated them accordingly.

Finally, I created the super user with "heroku run python manage.py createsuperuser". That successfully deployed my application.