# Deployment Experiences for Sprint-Challenge--Django-I

After following the instructions for the Sprint Challenge within my **djorg** repo, I achieved a `400 Bad Request` for both the /api and /admin directories, which given the circumstances of the past week I will confidently file under "Triumph of the Human Spirit."

Although I was not able to fully deploy the app I became more acquainted with the various requirements of a Heroku deploy, including the Procfile and config var setup. I learned to use logs in the Heroku CLI to debug missing installs and incorrect setup values. These logs were invaluable to getting my app out of its initial "just mysteriously crashing" state. 

The migrations seemed to go through--but I would want to check the admin interface to be absolutely sure.

In order to get this app up and running as expected, I would run through an example Heroku deploy first and then work with my **djorg** repo in particular. Working from scratch would help sort out what may have gone awry during this Sprint Challenge.