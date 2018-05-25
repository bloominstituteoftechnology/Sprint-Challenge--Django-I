The deployment process in working with Heroku and Django is a seemingly simple process that actually proved to be quite tricky. Throughout most of the process, things seemed to be going smoothly, until the actual `git push heroku master` in which case, the push was rejected. 

Upon first investigation it would seem that the error had to do with the buildpack, but even after manually declaring it, the push continued to fail. The next idea was that perhaps it was due to a discrepancy in environment commands. I used `virtualenv env` as opposed to `pipenv` throughout the steps offered in the readme. 

However, the problem ended up being due to an improper initialization of the DATABASE object, undeclared language, creation of a static, and a too deeply nested file structure. Upon making these corrections the app was successfully pushed to Heroku and deployed. 



