Deploying a Django app was a relatively smooth process, but I give much of that credit to the given guide _and_ to my development environment -- Linux.

The tricky parts were how to import multiple ALLOWED_HOSTS with proper formatting. It just required opening a python shell and experimenting with an end result of adding _.split(',')_ to the end of the _config()_ call for **ALLOWED_HOSTS**.

There were a few minor errors when trying to initially deploy that had to be figured out like how to set the database path but it just needed to be set to an empty dict first.

Once those issues were resolved and the heroku config options were set via the CLI it deployed with no issue.