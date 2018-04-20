### Deployment Experience
* Steps 1 - 3: Registering, installing, and logging into Heroku/Heroku CLI were all very straightforward. No issues there.
* Step 4. Again, navigating to my project/repo directory is muscle memory at this point.
* Step 5. Installation was, at first, very simple. I forgot to first `pipenv shell` but once I corrected that everything installed without issue.
* Step 6.
    > * i. We've worked with `.env` before so initializing was simple.
    > * ii. Everything looked fine here!
    > * iii. As suggested, running in a repl worked without issue.
    > * iv. This was where I got hung up the longest. For whatever reason, despite confirmation of successful installation, `python-decouple` and `dj-database-url` simply would not be recognized within my project. By updating `npm` and VSCode as well as installing Windows Update, I finally got it working properly although I'm still not sure what the correct fix was.
    > * v. Once `python-decouple` was working as intended, it was simple enough to config the SECRET_KEY and ALLOWED_HOSTS.
    > * vi. Procfile was about the easiest thing to create on here.
    > * vii. `whitenoise` has excellent documentation and seemed simple enough, too.
* Steps 7 - 9. `Heroku` is incredibly easy to use so the creation was a breeze.
* Step 10. The initial deployment was unsuccessful (followed by many more attempts) but I was able to `git push heroku master` eventually. Unfortunately, the app itself is still having some issues (seems to be entirely the `DATABASE_URL` at the moment), so some more debugging is still required.

#### Summary

I was able to make my way through the entire sprint and successfully deploy - but I have nothing on Heroku to actually show for the work. It was a great lesson in working through multiple docs simultaneously and troubleshooting while still making progress.

### Links 

* Git Repo: https://github.com/VinnieScalco/djorg
* Heroku Deployment: https://djorgbookmarksvs.herokuapp.com/ (unsuccessful so far)

