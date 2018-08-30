# What went well

Mostly everything except for the final touches. I had trouble setting up the default database but the real problem came when I deployed and checked my endpoints. The error stated that my `ALLOWED_HOSTS` env variable was not set up to allow my heroku app to access the endpoint. After about 30minutes of investigating I realized that after bringing in the env variable I also had one later on in the script that reset the `ALLOWED_HOSTS` to an empty list. After removing this everything worked out just fine.

# What was tricky

The tricky part of figuring out how to set up the `dj_database_url` configuration as the documentation for `dj-database-url` module is not very thurough and leaves room for interpretation. Later I realized I was trying to use the `dj_database_url.config()` method incorrectly and supplying a default database as an argument worked.

# How far did you get

My app is completely deployed and works exactly as it should from local to live. Ends points such as `agile-gorge-99628.herokuapp.com/admin` and `agile-gorge-99628.herokuapp.com/api/notes` works as expected. Given the correct authentication credentials the user is returned with their data.

# Test Endpoint

In the terminal run `curl -H 'Authorization: Token b540a8814a2c537988dd575c1fc056f928d25bbb' https://agile-gorge-99628.herokuapp.com/api/notes/ | python -m json.tool`. This will allow you to view what the test users API is returning.