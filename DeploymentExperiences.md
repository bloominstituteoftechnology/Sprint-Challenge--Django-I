My attempt at deployment was a fiasco.  I don't understand (or only partially understand) what the majority of the steps in the
readme are meant to do.  Django is, to me, a huge confusing mess of things that I fiddle with to try to make work without
understanding what I'm actually doing or why.

While trying to deploy, I spent a lot of time making small changes to settings.py, especially those parts
involving python-decouple, and redeploying to see if it would successfully build.  It also took a few tries to get the
environment variables on heroku right.  Finally, I got a build to succeed and was able to view the /api screen.

I have the app working as intended when offline, but when deployed it fails to migrate.  The terminal output to migrate says everything succeded,
but then ./manage.py showmigrations still shows everything unchecked.  As a result of this, no superuser can be made
and no access to the /admin screen is possible.