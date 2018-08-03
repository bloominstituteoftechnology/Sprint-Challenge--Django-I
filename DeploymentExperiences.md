This deployment was difficult mainly because I am new to heroku. I had issues with the app itself that I needed to fix before deployment:
  * no secret key (had issues with python shell but was finally able to generate)
  * couldn't configure secret key to heroku (fixed it in heroku dashboard)
  * some issues configuring white noise and static files (fixed while troubleshooting with Beej)

Currently my app is deployed but doesn't load, I'm working on a fix.