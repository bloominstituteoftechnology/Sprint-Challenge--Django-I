[Project Repository](https://github.com/iAmAdamReid/Intro-Django)
[Live Site API](https://django-sprint-acr-new.herokuapp.com/api/)

- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

Before deploying an application to Heroku, we first have to create an application using the Django web framework. In order to do this, we need to initialize a project that will handle all of our applications. Django makes initialization easy, as the constructors handle the necessary directories and files for us via these commands:
`django-admin startproject project_name` initializes Django's settings, database configurations, and Django-specific options.
`python manage.py startapp app_name` initializes a directory structure that contains the basic files necessary to run an application.
You can see more about these commands and what files/directories they manage [by reading the documentation here.](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)

**What went well?**
The documentation provided in the project README.md was extensive, and allowed for a straightforward development process without diving too deep into the concepts. Additional information was provided to help us understand what is happening as we develop the server. The biggest difference in developing in Django is that much of the work happens in a virtual environment. I'm using `pip` and `pipenv shell` for the virtual environment, which manages all of our dependencies locally, rather than system-wide. 

**What challenges did you face?**
Adjusting to this new way of development took a little time, as I had to ensure I was running the right commands in the right shells. Django comes with a huge assortment of tools and addons that can give impressive functionality out of the box. Configuration is well-documented, but that doesn't mean you won't have to debug a few things. The largest challenges I faced were getting comfortable with virtual environments, and understanding what configurations were necessary for Heroku deployment, specifically using the `.env` and `Procfile` files. Thankfully, Heroku's documentation is extensive, and the Lambda instructors were helpful with any errors I encountered.

**How far did you get?**
I managed to complete the project MVP by deploying a token-authenticated RESTful API for a simple Notes application that serves Note data from a relational database using JSON. Additionally, this application has an administration panel that allows a superuser to create, edit, and delete users and notes from the database.

**Which docs did you think were the most helpful?**
The official Django documentation was very useful for a first-timer. They have an extensive documentation that can be as shallow or as deep as you choose. In addition to the docs, there is a large community of coders that contribute to community blog posts and mailing lists that can help further your understanding. Everything is laid out in a way that is accessible, and it is easy to find what you are looking for.

All in all, this project has given me a larger toolkit to consider when choosing to build web applications. Being able to deploy to the web using Python is a useful skill indeed, as Python is one of the most widely used languages [in the world](https://pypl.github.io/PYPL.html).

