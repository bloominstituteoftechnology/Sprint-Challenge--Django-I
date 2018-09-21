Following is a list of my deployment experiences:
*Had no problems installing dependencies or preparing the project for deployment
*First deployment attempt results in Collectstatic error. I tired to #comment out the line throwing the error from settings.py, tried to re-deploy, but got the same error.
*After googling the error I found that the solution was to temporarily disable collectstatic during the deploy
*DEPLOYMENT SUCCESSFUL!
*Next I tried running migrations and got a syntax error, just a closing parantheses was missing in settings.py - easy fix.
*Again, an error while running migrations SECRET_KEY not found.