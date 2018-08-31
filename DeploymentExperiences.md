### Deployment Experience

Throughout the week, I was able to learn new things about django/sqlite. However personally I think todays sprint was more valuable since I had not been able to deploy or work on this side of web development before. I am currently having issue with the following. 

* Can't do migrations using heroku, hence the site is showing error. 

I have gone through the whole process of understanding different parts of every thing that was listed in the readme, and eventually figured it out via respective documentations. DATABASE_URL was slightly truicky to figure out. Initially I had a simillar implementation to the code in documentation however later I removed max_conn_age. 

I also had trouble using ALLOWED_HOSTS, when running offline. I had to use split to make it work. 

I still can't make the application to do migrations. Howwever it is deployed at 'https://notify931.herokuapp.com/'