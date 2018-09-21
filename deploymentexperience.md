## Favicon problems/Static Files

As I first step through this, I am struggling with static files. I keep getting errors related to the favicons, and I'm not sure why.

* Added static_root, and collected static files for deployment manually.

I figured out that I needed somewhere to collect the static files, and added that to settings.py. I'm not following the postgres instructions too well at this point...I'm not too sure how to change the db over to postgres, none of the tutorials make sense in relation to this project at this point.

* Able to get postgres db almost working: migrations now updated up until the notes migrations, with the following error:
---"django.db.utils.ProgrammingError: cannot cast type integer to uuid"
research this error now...not sure if it was an implementation problem with the way the code was written in models.py

i think we found a python bug, as it worked locally, but would not work after db was changed to postgres and uploaded to heroku. after going through stackoverflow, we found a solution that works, but it is a workaround. In order to get a functioning db, I had to manually change the migrations file to remove the primary key that was initially created, and then add a new one with a UUID...instead of altering the ID field, which was throwing errors.

DB now functions, but testing is needed on both endpoints to make sure only the users personal notes are showing up.
