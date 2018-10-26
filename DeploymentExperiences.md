# Link to all week project repo - Intro to Django
# https://github.com/DasGMA/Intro-Django

# Heroku link for deployed app - https://dasma.herokuapp.com/

# Deployment experience

- Django deployment to heroku wasn't complicated at all. The trickiest part was to install Heroku-CLI on OpenSuse Tumbleweed linux distribution. Downloaded tar.gz file and manually copied and pasted the files to /usr/local/lib and /usr/local/bin locations.
- After successful Heroku-cli installation, was a breeze to follow the deployement instructions.
- However i ran into one issue: i couldn't get into https://dasma.herokuapp.com/api due to authorization issue, despite the fact that token was created upon the creation of the new superuser. If i removed authorization - then i could access the links. Wll have to look more into this and update this file accordingly. 
- Ok the issue has been fixed. If anyone is running into the error 'BasicAuthentication' object has no attribute 'has_permission' the please make sure you have the code in settings.py as below:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

Also dont forgetto do imports in settings.py 
'from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication'