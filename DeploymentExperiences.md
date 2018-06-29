## How far I made it:
The project is fully deployed and working at https://djorg-pa.herokuapp.com/ but there is not front end yet, so please use https://djorg-pa.herokuapp.com/admin/ instead.
The api can also be viewed at https://djorg-pa.herokuapp.com/api/.
The project repo is https://github.com/perryahern/djorg-cs8.

## What went well:
The instructions were generally clear and easy to follow. I was able to get through most steps fairly quickly. The ones that slowed me down a bit are listed below. In the end, though, the project is deployed and all four endpoints are working.

## What was tricky:
There were a few spots that raised questions or problems, such as:
- 5.iv seemed unnecessary as python-decouple was already installed, wasn't sure if there was a reason to run it again or if doing so could reset something that was already properly configured. I skipped this step.
- 6.iii also seemed unnecessary as we already had a secret key, again I wasn't sure if there was a reason to make a new one here. I skipped this step.
- 6.v configuring ALLOWED_HOSTS wasn't clear at first, but the existing declaration was for a list and the string we had put into .env contained two hosts separated by a comma. Researching turning a string into a list provided the solution of splitting it around the comma and enabled this to work.
- 10 The deploy step threw me as my initial deploy failed and I did not notice that initially, so my attempts to run heroku python manage.py commands all failed. When I realized the deploy failed and I tried it again it failed again, but a suggestion to disable collectstatic in the error provided the solution. Once I used that command and pushed to heroku again it worked.