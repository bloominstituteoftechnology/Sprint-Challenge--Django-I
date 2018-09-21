##LINKS:
App Deployed:  https://lambda-notes-django.herokuapp.com/
Project Repo:  https://github.com/LambdaSchool/Intro-Django/pull/56

##OVERVIEW OF SPRINT CHALLENGE:
I was able to deploy my django app to Heroku, but I did have several issues that prevented my success to make it show my api root page.
Overall, I did enjoy the process through all the wins, fails and trying to tweak to the app.  This really did make me use my mad skills at Google searching for an answers and keep practicing the "Trial and Error" methodologies.  And most importantly to be "okay" when it fails, just keep trying.


##ISSUES LOG:
1.  Heroku error code H10[status 503]:  Heroku logs indicated that "app crashed" with a error status H10[Heroku Router].  Not sure how to fix the routing?  I tried to changed procfile, changed Debug=true to false, and changed ALLOWED_HOST=['.herokuapp.com'], Looked over the Static[URL] Files but no success.

2.  Heroku Error Msg [decouple.UndefinedValueError: SECRET_KEY not found]:  This one really stumps me.  I generated a new secret key and added to both .env file and tried to add configs in the heroku dashboard/cofigs / key/value.  Not sure what's happening.  When I deployed its fine, but if I heroku run python migrate = secret key is undefined error always pops up.






