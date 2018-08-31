In overall it was challenging for me the implementation.

Is always hard to me read and follow the instructions in the Repos.
I do not understand all at first.

# TRAINING DEPLOYMENT:

- I started reading/following a [Heroku tutorial on Django deployment](https://devcenter.heroku.com/articles/getting-started-with-python)

  > My main goal was to get familiar with deployment steps and configuration needs.
  > This was a good exercise to start modeling my brain on what is neccesary to deploy.
  > The tutorial was no so difficult to follow, there were all the files needed to deploy, an instructions were very detailed with related links.

# REAL DEPLOYMENT:

- A mind challenging task.
  > Even though the core steps and setup are the same, the approach given in the Sprint Repo is another universe.

### Phases/Steps to follow:

1. ADD new dependencies.

   - A time and synapsys comsuming task: I was reading around to understand the purpose and function of each dependency installed.
   - I barely figured out how to wire _psycopg2-binary_, I understood form the docs that heroku set a PostgreSQL by default when we deploy. So i do not understand the purpose of this dependency.
   - _whitenoise_ : _Concept_ understood. _Functioning_: Still figuring out.
   - _requirements.txt_: Why do we need that? Isn't the Procfile enough?
   - _dj-database-url_: Hard to figure out how to configure it.

2. Heroku && Heroku CLI:
   - I found no real concerns with that.

# TRICKY PARTS:

1. Figure out how to set up _dj-database-url_, and how it is wire in the local repo and the heroku repo, mind challenging.
2. Structure and understand the steps that is neccesary to do before others. Some examples:

   > Deploy after setiing the _env variables_ in Heroku server. (Even though it is straight forward, I made this mistake)

   > Remember to make migrations in Heroku, before testing your APP/API.
