Dear Colleagues, 

Deployment was a success; mostly straightforward with only a few issues. Configuration took place almost exclusively in my settings.py folder and I either omitted or mistyped the following things:
  * forgot to import the Csv type from the python-decouple package
  * fort to add the ```STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')``` variable when using white noise to cache static files
  * Tried to overwrite the DATABASES dictionaries default setting after accidentally deleting the dict.
  
Note: I resolved all these issues by closely reading error messages during heroku deployment
    
