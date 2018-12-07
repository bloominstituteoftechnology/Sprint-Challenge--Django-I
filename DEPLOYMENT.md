# Heroku Deployment Document
## By Tom Tarpey (CS13)

# Synopsis
In this sprint I have rewrote the Django Project from the past 4 days and deployed it manually to heroku as per the project specs for this current sprint. This process has been an interesting experience and has not been to eventful by way of errors, as I have already done a few deployments to heroku for previous projects.

## Basic Tools
The basic tools are a set of tools that were needed to create and deploy a django app based upon my experience in this sprint and reading of external documents (will be cited in the apendix)

- python3 (base language and interpreter / repl)
- pip (package manager for python)
- pipenv (localized environmental creation utility and wrapper for pip)
- django-admin (python module set with administration functionality)
- heroku (the heroku-cli, for all deployment related commands)

## Methodology
The methodology that I have used to deploy this project can be summed up as follows:

- forked and cloned the sprint repository
- created and entered a python 3 virtual environment
- installed django and created a djorg (django project)
- created a notes (django app)
- wrote the models and migrated them to a local sqlite database
- tested the admin interface
- added modules imports and settings to facilitate the api creation
- created the rest api to allow personal notes to be used and created
- added in modules and imports to facilitate an auth token system
- implemented a basic auth token system and routes
- tested the auth system via the use of curl
- installed the heroku cli and django-heroku modules
- installed helper modules such as gunicorn and posgresql clients and helpers
- updated settings and url files accordingly
- abstracted config using the detatchment modules and config
- linked the current project in to heroku via heroku login and created a heroku app
- used the heroku cli to create a psgres instance
- added the vars in the heroku dashboard for SECRET_KEY, DEBUG, ALLOWED_HOSTS etc
- deployed the heroku app via a git push to the server
- used heroku cli to migrate the data to the new database
- used heroku cli to run superuser creation on the server
- logged in to the admin section of the heroku app and created some data
- went to the rest endpoints and tested CRUD operation on the server api


## Conclusions
In concluding this project I have a few sectional topics to address, all in all the overall process went fairly smothely although I do believe that if i had not had prior experience in deploying applications in general then this process could have posed a myraid of errors and issues, also leaving the DEBUG flag set to true would be the most helpful aspect when deploying as this will allow verbose debug information on any errors during deployment and testing. I faced a few challenges along the way. such as the general creation and migration of the data but by reading the instructions in the README and following them to the supplied documentation all possible issues were covered for the project in question. I managed to deploy fully to the heroku server with admin routes and the api enpoints all working for full CRUD operations. The documentation in the readme was very concise and the references to the external module and api docs was most helpful. This sets the bar in comparison to some of the development projects that I have worked on and has kept a clear and goal oriented documentation schema to allow students to follow along well with the project material. Failing tooling issues, the only time I could see a faliur in this project would be due to lack of reading the instructions and linked documentation.


# Appendix
Here you will find anything else that did not fit in to the previous sections. This section is a fluid part of the document that can be added to as I find more useful aspects of the deployment process.

## External Recources

Here is a list of external references that I have found useful when working on this project:

- [Heroku Devcenter](https://devcenter.heroku.com/)
- [Django Documentation](https://docs.djangoproject.com/en/2.1/)
- [Dev Hints Heroku Cheat Sheet](https://devhints.io/heroku)