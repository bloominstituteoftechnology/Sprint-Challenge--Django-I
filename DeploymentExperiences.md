- Summarize the key steps in the deployment process.
  - What went well?
  - What challenges did you face?
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past.

## Experience
Deployment was tricky at first. I challenged myself this project by buiding using a docker container. After reading many ways to deploy a container on Heroku, I concluded that deploying from git would be the faster, less headache inducing choice. I simply had to move a couple of config files to the root directory, eg. `Procfile`, `Pipfile`, `Pipfile.lock` and commit and push to the heroku remote.

I ran into an issue where I was forgetting to update my DATABASE_URL, so all my migrations would not transfer to the correct the postgres db. API routes would fail due to `table_name` does not exist. This was fixed by using the `django-heroku` package, which set this configuration for me automatically.

## Docs
The Django docs are some of the most aesthetically pleasing to read docs I've come across. Both Django and Django Rest Framework docs are sublime and the tutorials are awesome.


### Deployment
Heroku: https://django-alex.herokuapp.com/api/
