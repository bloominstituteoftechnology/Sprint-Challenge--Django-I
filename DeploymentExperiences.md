- Summarize the key steps in the deployment process. 
  - What went well?

  The instructions for step 1 to step 5 were fairly clear. The only problem I was having is that I had to typed 'sudo' whenever I want to install dependencies, otherwise I would get a 'permission error' message. That was fixed after hopping in zoom with my PM and Brady. I was a little confused on the whether I need to create requirements.txt inside my pipenv shell or my project directory, turns out it doesn't really matter.

  - What challenges did you face? 

  When I was working on DATABASE_URL, I was getting an error saying 'DA' is not found. I doubled check to see if I had any syntax errors and reread the docs. I could not find anything wrong so I asked for help during after hours. The PM there helped me fixed the error I was getting. I was also confused about the Procfile. The directions for it was not clear to me. I did not know what the direction was asking. After asking for help during the after hours, I realized I had to make a new file called 'Procfile' and copy paste the example given and changed project name to 'djorg'. I was also getting an error when I tried pushing it to heroku master. I had to disable collectstatic before I can push to heroku master. 

  - How far did you get?

  I was able to deploy my app to heroku so MVP is completed. 

- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 

  I find all the docs provided helpful. The docs about the DATABASE_URL did confuse me a little. I had to look for outside resources for ALLOWED_HOSTS since it was not given in the repo. I had to look at a few docs until I found the one I understand and works. 

  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

  The docs were fairly clear to understand in terms of the directions. It tells you waht codes to type in your file and where. 

