- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

### Summarize some steps with problems:

- Install pyscopg2-binary: throw error Could not find a version that satisfies the requirement pyscopg2-binary (from versions: )
No matching distribution found for pyscopg2-binary
[Solution](https://stackoverflow.com/questions/49811955/unable-to-install-psycopg2-pip-install-psycopg2)


- Create a django startproject with `$ django-admin startproject myproject .` will help eliminate nested project folder. With this command line, `manage.py` will be created in the root, not the new project folder.

- Deploy successfully but run app with error `No module django`
Solution: adding django to requirements.txt file

- Run app. Hit `500`
Solution: Allowed_hosts is mistakenly in array

- Run app. Hit `404`
Actually, I only have path `/admin`, so access root obviously return 404 :P. In path `/admin`, I can see the log in page

### Extra docs or command line I used

- I relied on heroku a lot for this Sprint [link](https://devcenter.heroku.com/articles/deploying-python)

- I used `heroku logss --tail` to view error detail