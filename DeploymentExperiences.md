This wasn't my first dance with deployment and it won't be my last.  I approached this sprint the same way that I approach every deployment - writing code that I thought would work, testing locally to see if it did, and then pushing the changes to the deployed version and seeing if it broke anything.

I was lucky in that my app was already fairly well-constructed before I got to the task of deployment, so there weren't very many hurdles that I had to get through.  

The majority of my confusion came with the misunderstanding of what was going to occur when I switched from my sqlite database to the postgres database - namely, that my data wouldn't magically port over.  I spent some time trying to figure out how to dump the data into the deployed database and then ultimately abandoned the pursuit in the interest of time.

Any issues that I came against were usually fairly easily remedied by reviewing materials on Django's website, StackOverflow responses, or tutorials that I found online throughout the process.

Integrating static files into a deployed app is somewhat fiddly.  Figuring out how to be able to change things locally and still be able to test them locally after deploying was an awesome bonus as it was something that I didn't manage to figure out during the backend project.

I never really had to examine deployment logs to get to the root of any of my problems on this deployment, though I did spend a good amount of time troubleshooting other peoples' deployment issues and that led me to read a lot of deployment logs.

Overall, the experience was rewarding and I feel like I learned a lot about how to troubleshoot.