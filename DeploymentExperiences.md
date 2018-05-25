The deployment process was not as intense as I expected it to be, considering this was very first python app I have created. I was able to successfully deploy a live app with everything functioning as they should.

##### What went well
I made sure to follow the directions as slowly and carefully as possible. This created less errors than I was prepared for.


##### Tricky parts were
1. Trying to find out how to implement ALLOWED_HOSTS from .env
2. Implementing DATABASE_URL using dj_database
3. Debugging why heroku migrate was not working (I fixed this by disabling some static setting variable and changing configuration line for dj_database from utilizing SQLite to postgreSQL)

