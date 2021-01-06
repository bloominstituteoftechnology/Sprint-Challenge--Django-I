Heroku provides a simple and functional logging protocol for applications. To view the logs, all you have to do is type `heroku logs` and it will generate a list of logged actions. This was especially useful when debugging the deployment process, as the logs are informative as to what was missing or going wrong.

What I found most useful, however, was the `heroku logs --tail` functionality, which gives a real-time log of all incoming requests to the server. This allows you to debug every step of the way, and to check the web status responses as they happen. 

You can see an example of a heroku log output here, which shows the startup of the dyno, as well as some HTTP GET requests.
![Heroku Logs Tail](/imgs/heroku-logs-1.jpg)

In addition to Heroku's logging capabilities, they also have the ability to congifure [custom Webhooks](https://devcenter.heroku.com/articles/app-webhooks) that can send notifications for events that happen in an application or dyno. By using Webhooks, you can stay aware of major application changes even while you're away from your development machine. Or, you could even deploy your own site-monitoring application that receives Webhooks from multiple applications, and monitor all of your development activity from one place.

Heroku's architecture is very developer focused, as all of these impressive features come standard with every account. I was a bit hesitant about Heroku at first, as I'm so used to managing everything when it comes to server deployment, but their integration with Git and their extensive list of features make Heroku an attractive platform for the hobbyist or professional developer.