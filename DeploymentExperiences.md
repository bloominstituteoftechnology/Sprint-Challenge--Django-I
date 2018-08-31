My deployment experience went as follows:
Setting up dependencies went smoothly
Deployment seemed to go smoothly as well until I tried to access the app itself.
Initially I ran into a 500 response, turns out I didn't set up my static storage correctly.
After disabling that, and confirming my app ran locally, I pushed and deployed again.
Then I ran into a 400 error, this just turned out to be a problem with my ALLOWED_HOSTS 
config vars, which I typed in incorrectly. This was easily fixed.
There were no more errors after that, the app is up and running.