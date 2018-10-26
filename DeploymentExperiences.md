Github repo: https://github.com/LambdaSchool/Intro-Django/pull/104

Heroku link: https://francis-t-intro-django-project.herokuapp.com/

1) Build failed. 
[ERROR] To https://git.heroku.com/francis-t-intro-django-project.git ! [remote rejected] master -> master (pre-receive hook declined) error: failed to push some refs to 'https://git.heroku.com/francis-t-intro-django-project.git'

2) Heroku logs show error while collectstatic was running.

3) Entered heroku config:set DISABLE_COLLECTSTATIC=1

4) App deployed.

5) App crashed upon launch. ALLOWED_HOSTS not found.

6) Typo in heroku env vars. ALLOWED_HOSTS vs ALLOW_HOSTS

7) CORS not found. Added CORS vars to heroku. Migration successful.

8) Heroku bad request (400) on open app.

9) Changed DEBUG to TRUE for now. new error DisallowedHost at /

10) Change DEBUG to FALSE. Updated ENV. Server runs at start but it says, "Not Found
The requested URL / was not found on this server." Changed ALLOWED_HOSTS to ['*'].

11) Imported django_heroku library.

12) reconfigured a lot of settings in settings.py (detailed in git commits)

13) Successfully deployed 10-25-2018 15:07 PDT