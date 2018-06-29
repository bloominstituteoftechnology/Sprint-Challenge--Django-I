[Git hub repo](https://github.com/emukupa/djorg)
[Deployed djorg-cs8-app](https://djorg-cs8-app.herokuapp.com/admin/login)

I followed the steps as outlined in the instructions, but was stuck with this error:

(
raise ImproperlyConfigured("You're using the staticfiles app "
remote: django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having setthe STATIC_ROOT setting to a filesystem path.
remote:
remote: ! Error while running '$ python manage.py collectstatic --noinput'.
remote: See traceback above for details.
remote:
remote: You may need to update application code to resolve this error.
remote: Or, you can disable collectstatic for this application:
remote:
remote: $ heroku config:set DISABLE_COLLECTSTATIC=1
)

A classmate had the same issue and I asked him how he solved it, he added:

`STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`

in the settings and the site was deployed.
