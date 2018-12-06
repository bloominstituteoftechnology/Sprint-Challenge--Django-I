[Djorg Project Repo](https://github.com/cornielleandres/Intro-Django)

[Live Site - Login](https://lambda-notes-python.herokuapp.com/admin/)

[Live Site - API](https://lambda-notes-python.herokuapp.com/api/) (*)

(*) Note: Without logging in, you will not be able to see notes or recipes, but you *will* be able to see ingredients for recipes([Click here](https://lambda-notes-python.herokuapp.com/api/ingredients/) for a list of all ingredients).

- Summarize the key steps in the deployment process. 
  - What went well?
    - Everything went smoothly for the most part.
  - What challenges did you face?
    - There was one part where upon deploying I got a `Bad Request (400)` error. I was able to find out that I was interpreting the directions wrong. Where it said to add the env variable `ALLOWED_HOSTS=.herokuapp.com`, I thought this implied including the site URL, so I made it `ALLOWED_HOSTS=lambda-notes-python.herokuapp.com`, which gave me the aforementioned error. Upon switching its value to `.herokuapp.com`, the site started working properly.
  - How far did you get?
    - I was able to fully deploy.
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
    -  I've always liked the documentation provided by heroku themselves.
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 
    - They guide you step by step through the process in an easy-to-understand way. I also often use the `heroku logs --tail` command to troubleshoot.
