- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

Before deploying an application to Heroku, we first have to create an application using the Django web framework. In order to do this, we need to initialize a project that will handle all of our applications. Django makes initialization easy, as the constructors handle the necessary directories and files for us via these commands: django-admin startproject project_name initializes Django's settings, database configurations, and Django-specific options. python manage.py startapp app_name initializes a directory structure that contains the basic files necessary to run an application. You can see more about these commands and what files/directories they manage by reading the documentation here.

What went well? The documentation provided in the project README.md was extensive, and allowed for a straightforward development process without diving too deep into the concepts. Additional information was provided to help us understand what is happening as we develop the server. The biggest difference in developing in Django is that much of the work happens in a virtual environment. I'm using pip and pipenv shell for the virtual environment, which manages all of our dependencies locally, rather than system-wide.

What challenges did you face? Adjusting to this new way of development took a little time, as I had to ensure I was running the right commands in the right shells. Django comes with a huge assortment of tools and addons that can give impressive functionality out of the box. Configuration is well-documented, but that doesn't mean you won't have to debug a few things. Earlier in the week I was challenged with a bug that I was told to move on from. I tried to solve this bug more than I should have and it took away my time to actually finish the app.

How far did you get? I managed to deploy an app that isn't finished. The bugs that I faced earlier in the week took away my time to actually complete an app in django.

Which docs did you think were the most helpful? The official Django documentation was very useful for a first-timer. Everything is laid out in a way that is accessible, and it is easy to find what you are looking for.

Being able to deploy to the web using Pythhon is a useful skill, as Python is one of the most widely used languages in the development business.