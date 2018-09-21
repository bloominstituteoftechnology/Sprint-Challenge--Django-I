Deployment to Heroko of a Django app

- my repo: https://github.com/tgreenhalgh/djangoDeploy
- the deployed app: https://lustyllamas.herokuapp.com/

A DeploymentExperiences.md file where you write summarizing how the process went for you, what went well and what was tricky, and how far you got
For the writing portion, this is meant to practice your skills at professional writing - in the tech world, that means writing things clearly, concisely, in a way to get the information across efficiently to an audience that may be pretty busy (most people only skim most emails). Suggested length ~1-2 paragraphs, and bullet lists can be extremely effective.

Deploying my Django app to Heroku was an exercise in patience. The directions were fairly straight forward, but either I didn't notice some things or they weren't particularly clear.

My biggest issue was that I tried to use the original repo for deploying, but as djorg was a sub-directory, that proved tricky. So, I ended up taking everything from the djorg directory and making a new repo (linked above).

The next issue was setting up the database. Heroku does not play nice with SQLITE3 and installs Postgres by default. I had to make the following changes:

```
DATABASE_URL = 'postgresql:///postgresql' # sqlite:///db.sqlite3" was in the repo
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
```

I glossed over the `Set the other Heroku config vars` because in my head this was covered by the `.env` file. After things didn't work, I realized and made the appropriate changes in the Heroku dashboard.
