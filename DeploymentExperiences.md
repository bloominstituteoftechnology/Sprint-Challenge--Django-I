- A link to your [project repo](https://github.com/cassidyjamesw/Intro-Django)
- A link to your [Live site: admin](https://cassidy-djangosprint.herokuapp.com/admin/)

- Summarize the key steps in the deployment process.
  - What went well?
    The site got deployed, not many challenges.
  - What challenges did you face?
    Took me a bit to figure out that you need to set config files on heroku, since the .env file does not push. As well as allowing hosts.
    Ran into `Error while running '$ python manage.py collectstatic --noinput'` , solved by running `heroku config:set DISABLE_COLLECTSTATIC=1`, which disables running the collectstatic command when app is pushed/built.
  - How far did you get?
    I was able to deploy my site.
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
    The Heroku docs were very helpful in understanding my collectstatic issue.
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past.
    Well written with example code.
