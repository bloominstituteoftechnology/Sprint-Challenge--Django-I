For the most part deployment went fairly well. There was only two parts that caused
issues.

-The first issue was due to a mistake with my database setup. I commented out the
setup that was in settings.py to begin with and placed in what was shown in the
documentation, not paying attention that it requires an object

-The second issue was when the build was successful it was returning
'Bad Request 400'. This was due to an improperly setup Allowed_Hosts config. Once
fixed by adding the missing config and then updating the settings.py file to use
the configurations.

Other than that, the deployment went fairly smoothly and testing via Postman and
the admin page shows it up and running.
