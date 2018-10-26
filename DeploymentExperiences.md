Having not succeeded in my previous deployment experiences with Heroku, it was very satisfying to complete this Sprint and have a functional site with a database. Below you will find the key points where I either stumbled or had a revelation during the implementation process:

1. Initial phases went very smoothly as a result of the clear instructions.

2. 6vi threw me initially, and it wouldn't be until I began examinning the logs that I would solve this problem through tiral and error.

3. While initial deployment was successful, log-in to admin was not, which lead to many cycles of pushing heroku master and reading logs --tail.

4. When first interacting with the Heroku Logs --tail, I looked to the error codes for answers. After several iterations of this and basically spinning my wheels, I looked further up in the logs and found the true breakpoint in the code, which lead to much more useful feedback and allowed me to make progress in debugging.

5. I then became too focused on the logs and failed to step back and look at the bigger picture again once my wheels started spinning once more. I had a simply failed to create a new superuser after deploy, which I would have realized if my focus hadn't been so singular. I could have, instead, looked to the readme on the repo or simply thought about what deployment actually means from an infrastructural standpoint.
    - Key lesson learned here: If you stop making forward process, step back or try a different angle of approach.
        - I had a similar lesson occur with the .env file wherein I simply wasn't thinking about what the true puropse of a .env file was. Instaed, I was thinking only one level deep in that it connects to the Settings file, in this case, rather than thinking about the greater whole, which is to keep sensitive data from being exposed on your local files, meaning that my secret key was not being transfered up to Heroku.
        - I also believe that part of this distraction comes from the novelty of the code and, as a result, becoming wrapped up in syntax rather than meaning.
