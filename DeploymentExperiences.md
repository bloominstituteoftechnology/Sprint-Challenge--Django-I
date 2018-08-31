
The deployment experience was ok over all, I had issues with figuring out how to set up ALLOWED_HOSTS and DATABASE_URL in settings.py but figured that out. I came up with an H10 error in the end indicating that perhaps my environment was not set up properly. 

Other than this, I think I finished key aspects of the deployment process.

Below is a description of the error.

2018-08-31T19:49:42.460507+00:00 app[web.1]:     self.reap_workers()
2018-08-31T19:49:42.460538+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/gunicorn/arbiter.py", line 525, in reap_workers
2018-08-31T19:49:42.461004+00:00 app[web.1]:     raise HaltServer(reason, self.WORKER_BOOT_ERROR)
2018-08-31T19:49:42.461048+00:00 app[web.1]: gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
2018-08-31T19:49:42.569718+00:00 heroku[web.1]: Process exited with status 1
2018-08-31T19:49:42.590123+00:00 heroku[web.1]: State changed from starting to crashed
2018-08-31T19:52:38.878985+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=djorgappsagar.herokuapp.com request_id=63ba85f5-e7ad-44be-bd00-299c4b5b9734 fwd="73.211.233.215" dyno= connect= service= status=503 bytes= protocol=https
2018-08-31T19:58:35.617035+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=djorgappsagar.herokuapp.com request_id=6a8e965d-14a3-4d99-aecb-f6b1237f219c fwd="73.211.233.215" dyno= connect= service= status=503 bytes= protocol=https
2018-08-31T20:13:14.810720+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=djorgappsagar.herokuapp.com request_id=1ace9190-2095-40d7-9d29-9f272e46eaa1 fwd="34.226.200.251" dyno= connect= service= status=503 bytes= protocol=https
2018-08-31T20:14:30.144264+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=djorgappsagar.herokuapp.com request_id=a61aba92-0e90-45e6-b9c0-42509e075183 fwd="73.211.233.215" dyno= connect= service= status=503 bytes= protocol=https
