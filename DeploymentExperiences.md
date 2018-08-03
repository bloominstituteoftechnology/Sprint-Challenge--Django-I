Log Entry -- 12:07PM (EST)

My initial attempt at deployment went well with regard to the installation of dependencies, the preparation of the project, and the creation of the app on Heroku via the CLI.

Where I initially ran into issues in my first deployment attempt was an error I was getting which said, "ModuleNotFoundError: No module named 'rest_framework'." 

I triple-checked that the rest_framework was properly installed, and tried to redeploy, but again, I got the same error. When I read through the error log more carefully, I saw that the initial error that triggered the "ModuleNotFoundError" was:

" !     Error while running '$ python manage.py collectstatic --noinput'. "

The error log mentioned that one way to potentially resolve this was to disable collectstatic for the application. Rather than just following that advice, I did some research on StackOverflow, and found that another developer had done this because of the same "ModuleNotFound" error, and it cleared things up and the app worked.

I then disabled collectstatic via the CLI, and re-ran deployment. 

The deployment worked! However, the app is not working. I am still troubleshooting, but am unsure what the issue is at the moment.