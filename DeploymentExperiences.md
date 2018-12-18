- Summarize the key steps in the deployment process. 
  - What went well?
  - What challenges did you face? 
  - How far did you get?
- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 



Installing the dependencies required reading up on documentation in order to see what we're downloading and how it works together. During the documentation reading, there is alot of guessing and testing how things fit in and for what uses we need the specific installtion for. Following the documentation required me to slowly read through documentation and really think.
It's not always about following the instructions. On one of the instructions, it tells us the generate a new SECRET_KEY, but we already had one. That step was completely unnecessary. In step 7, the documentation's example of setting the config variable was a bit different than the provided example in the READ ME, where we needed to initialize DATABASES_URL as a Dictionary. 

A specific Problem I am currently stuck on is deplying the Heroku app.
I've created the App, but I hit with an error telling me my pip.lock is out of date and it's expecting another version.
There is not much on this specific problem on google or stack overflow.
I am currently taking a look at my pip.lock file and trying to understand what exactly it is.
I am wondering if it needs to have all of the dependencies I downloaded inside of it. They are inside of the Pipfile, and not int he Pipefile.lock.

Finding out the corrupted file, I was left with only two options. To either keep trying to google this and dig deep, or to restart the project. I decided that after debugging with Brady, I should just go ahead and just try to restart the project since it wouldn't be worth the deep dive.

I am familiar with CORS, from using it with Javascript. This is one of my favorite dependencies that I downloaded. I love the protection it gives for HTTPS user. The installation was very simple just as it was with Javascript.

I noticed some documenttaions have their own website while others are simply posted on Github.
The ones posted on Github seem to have the simplest shorter documentation with I enjoy since its straight forward. But there are others that come more in detail.

I've restarted the project 4 times now.
I've followed the instructions to get a grasp of the workflow of what it takes to make a project.

After successfully installing all dependencies and having the right set up I am still running into an error on the final heroku push
