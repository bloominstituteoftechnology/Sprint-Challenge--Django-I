- Summarize the key steps in the deployment process. 
  - What went well?

    -   So many things went well as listed below while working on this Sprint Challenge.

        - Created new django project (djorg) and new django app (notes).
        - Modified urls.py and render notes app view when user runs django server locally using runserver command.
        - Created new heroku app and deployed django project to heroku.
        - Verified heroku app is accessible and displays same default view as local server.

            https://dashboard.heroku.com/apps/aqueous-woodland-66360

  - What challenges did you face?

    For many of the challenges I was able to find solutions very quickly and move forward. However, some problems were really challenging and I had to use my google-fu and refer to multiple sources to find the solution.

    One of the major hurdle I faced was heroku deployment. Although, I was able to run my project locally without any errors, when I tried to deploy on heroku it failed miserably. After, lots of research I found that for django project to work successfully on heroku, Pipfile should be inside the project folder (e.g. djorg in my case). Finally I moved Pipfile to djorg folder and everything worked fine from there. Although, problem looked very trivial in the end, I tried multiple things before I realized what was the problem.


  - How far did you get?

    I was able to run MVP for the project. My project is up and running on heroku and you can view it using following link.

        
    https://dashboard.heroku.com/apps/aqueous-woodland-66360


- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?

    To be very honest, I hardly looked at the project docs and mostly googled for answer when I was stuck.

    For me, [django official documentation](https://docs.djangoproject.com/en/2.1/) was very helpful for finding answers specific to django.

    Apart from that [stackoverflow](https://stackoverflow.com) was my go to resource for finding answers to open ended question and it did not disappoint me most of the time.

  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 

    [django official documentation](https://docs.djangoproject.com/en/2.1/) is huge, however it is very well organized. One thing I like about documentation is django tutorial where I can build working django application very quickly. It gives huge boost to my confidence when I see something I build is running even though it is very basic. Once I feel comfortable with my ability to build small app, I use this documentation to learn details about how django works to build more sophisticated app.

    This is different approach than what I used in past. I used to start with theroy first and once I understand concept, I will build something. The approach is good, however I will have to wait too long for the fun part and will become agitated after a while. I realized that if I work on fun part in the begining (e.g. implementation), I will be more interested in learning inner working and find out details.
