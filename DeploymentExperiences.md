Managed to deploy fully functional app. There were some obstacles. First major problem i encountered was some hiccups with Pipenv and Windows, lockfile would hang for years and i decided to add it manually as it will be used by Heroku anyway.

Then small typo in Procfile made it impossible for Heroku to launch dynos and run the server.

Had few troubles with Allowed Hosts (managed to finally solve it by adding "\*"), then with collecting static which i disabled to move forward.

I also forgot to properly configure dj_database_url at first, but then fixed that by properly putting conf in the settings.py.

Except small typos or errors everything went smoothly. Definetely the biggest obstacle was Windows itself acting weird on me.

Heroku's "heroku log --tail" command was great help.
