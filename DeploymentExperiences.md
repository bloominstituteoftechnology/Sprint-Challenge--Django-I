Installation of depends went well
Started having issues with environment variables and handled that one by one
Ran into issues with Procfile and ended up remaking Procfile/added --preload
Fixed issues with web scale and no dynos being present and white noise middleware, which was fixed by changing the order in middleware list
Deployed, and the only issue is that the path must be changed to /admin or /api and login seems to be having issues atm. Trying to figure those issues out atm

RepoLink: https://djangonotesdemo.herokuapp.com/admin
DeploymentLink: https://djangonotesdemo.herokuapp.com/api