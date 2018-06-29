Followed the guide, am now deployed.

Remedies:

- in `settings.py`:

  - add `.split(',')` at end of `ALLOWED_HOSTS` line (see .env file as to why)
  - re-add original `DATABASES=` for local deployment prior to production deployment

- in heroku dashboard:

  - add ALLOWED_HOSTS and DEBUG to config vars
  - change deployment method to GitHub
  - connect app to GitHub repo
  - manual deploy

[Djorg: Repo](https://github.com/RedSkelly/djorg)

[Djorg: Live Deployment](https://rocky-garden-34376.herokuapp.com/admin/)
