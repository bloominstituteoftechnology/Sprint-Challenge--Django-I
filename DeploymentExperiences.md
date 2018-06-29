A DeploymentExperiences.md file where you write summarizing how the process went for you, what went well and what was tricky, and how far you got

# Deployment
Deploying to <u>Heroku</u> was no walk in the park. It's like waiting at a four way stop sign, knowing you have the ```right-of-way``` but still can never manage to get moving. Suddenly, you are left alone to make a very important decision and that is to ```Go(readMoreDocs)```

The trickiest part was having typos that weren't apparently easy to find. The ```DATABASE_URL``` was tough because as I deployed (with errors, of course), Heroku's configs had different <i>key:value</i> listed that stated postgres instead of db.sqlite3. ```I am still investigating this```

I was able to deploy. However the app is <i>not fancy</i> and I am hopeful to get the kinks worked out.