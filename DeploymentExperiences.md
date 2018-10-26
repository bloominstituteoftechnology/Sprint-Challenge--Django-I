I had an issue when trying to push to heroku with this error "You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path."

I tried rewriting BASE_DIR but it didn't work so I did heroku config:set DISABLE_COLLECTSTATIC=1 as
suggested by heroku to avoid the issue.

After the build succeeded and I tried opening the app, it showed an application error.
I checked the heroku logs and there were multiple errors with code=h14, status=503 and
desc="No web processes running"

I checked the code description and apparently it means no dynos are running. The heroku dashboard
shows "this app has no process types yet" and tells me to add a Procfile to define it so I'm guessing
heroku isn't detecting my procfile.

Turns out I didn't commit my changes through git before pushing to heroku.
The App now starts up but it gives me an error "Bad Request (400)".
The logs don't give me any helpful info. I give up for now.
