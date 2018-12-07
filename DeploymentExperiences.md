- Summarize the key steps in the deployment process.
  - What went well?
  - What challenges did you face?
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past.


Deploying to Heroku requires a few key steps. First, one has to make an account with Heroku. This is as straightforward as signing up for any other service online. Then, from the command line, set a few key variables (these can also be reached online from the Heroku dashboard). Finally, the app has to be deployed by choosing a unique app name and pushing your repo to Heroku's git.

Pushing my preexisting project was quick and easy; the steps and guidance listed on the Lambda School repository for the assignment was helpful and straightforward. I did, however, have to both actually assign the default variables in Heroku (I had applied the instructions for this part to the secret .env file instead), including a COLLECTSTATIC variable that wasn't mentioned in the instructions. I persevered by carefully reading the instructions on the command line whenever something didn't work.

The result is a website that is at its bare minimum of functionality; it's even worse looking than the local deployment. I shouldn't be surprised; the assignment this week was to deploy a backend, not to make a pretty frontend.

The overall set of Lambda tutorial videos was very good and helpful. It was a clear implementation of our goals and was unambiguous. (I know this is low-hanging fruit, but the other docs I basically read as far as the installation instructions, which was a couple of paragraphs, and didn't have much trouble with troubleshooting them.) That said, I did appreciate the docs for e.g. CORS and dj_database_url which had the installation information right at the top of their' repos' front page.
