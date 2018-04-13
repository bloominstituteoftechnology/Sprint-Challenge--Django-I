# My Deployment Experience

Well first off I had Heroku working before, but it was giving me an "EPERM: operation not permitted error" pertaining to _netrc
which stores my CLI credientials. According to the troubleshoot on Heroku, I need to try moving it. Windows wouldn't show it, so now i'm waiting to allow the hidden files to come in view which says I have another 20 minutes. 

After struggling a bit and not being able to get my hidden folders to show, I was able to do a /A:H /B, then rm _netrc. I was able to login with the Heroku login after. 

I had some struggles with documentation and had to dig deeper on Google to find exactly what I was suppose to put, and the first attempt at a push failed. 

After many failed attempts it seems that perhaps I'm having an issuing with using static files. I set a STATIC_ROOT and was able to collect static locally, but not after I pushed to Heroku. I will attempt to get this right after I answer the questions, or see what hapepened during the solution lecture.
