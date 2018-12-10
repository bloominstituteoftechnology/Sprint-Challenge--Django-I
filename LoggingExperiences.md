I was able to retrieve logs via the command `heroku logs`. You can also retrieve a max
number of logs with `heroku logs -n <number>` so -> `heroku logs -n 100` to get 100 logs.

I could have used `heroku logs --tail` to get a real-time display of recent logs that leaves
the session open to get more logs.

I can filter using `heroku logs -s` or `-d`. Ex, `heroku logs -s app` or `heroku logs -d router`

![Logs](/imgs/heroku_logs_01.png)
![Logs_Router](/imgs/heroku_logs_router.png)
![Logs_Source](/imgs/heroku_logs_source.png)