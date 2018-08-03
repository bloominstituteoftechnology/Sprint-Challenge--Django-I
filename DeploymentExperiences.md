Hello! The development of this project we called djorg has been great. It has been an extremely valuable learning experience, and has given us a great insight into the Django fundamentals. We started from the beginning, just getting the app off of the ground, and went all the way to creating some authentication, and a back end. I had many successes, as well as a few failures, that turned into valuable lessons. Lets chat about those for a moment. Some of the harder parts for me were in the final deployment stage of the building process. The largest issue of them all was a big error message that read "DisallowedHost at /". This error threw me off a bit, and I had to do some real digging in order to figure out what was wrong. After countless stops to the django docs, and stack overflow I finally came across what was causing the issue. I was missing some items from my ALLOWED_HOSTS list. I had previously tried to correct this in the settings.py file, as well as in my .env file to no avail. The reason for the error? I did not properly add the additional host options on the heroku dashboard. After correcting this, I was met with my second biggest set back, which was the inability to log in as an admin. In order to correct this, I needed to try and figure out how to create another super user. After diggin in the django docs, google, and the previously recorded lectures I finally came upon the solution, created a new super user and finally gained access to the app and verified that it was working. All in all, this was a really fun project, and definitely worth the time. I appreciate you stopping by to check out this message. Thank you again!

What went smooth:
- general development
- note creation
- endpoints
- general understanding of data flow, and proper tools

what went roughly (but ultimately was solved)
- Creation of new secret key. 
- Creation of super user
- Deployment
- "DisallowedHost at /" error.

Resources to corrcet these: 
- Overstack.com
- django docs
- lambda school recordings
- google.com
- youtube.com

