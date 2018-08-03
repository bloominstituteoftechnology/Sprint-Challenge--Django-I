# DJorg Notes Live Deploy

---

## App development

see [Code repo](https://github.com/jayyargh/Hello-Django)

> All of the code above represents the back-end of DJorg Notes. There are no views or static files. There are three endpoints you can access.

1.  admin/
2.  api/
3.  api-token-auth/ <-- only post

---

## Deploy

1.  The deploy was not a success. The push to heroku worked, the build was accepted and the migrations via heroku's Python CLI went through, but each page merely provides a 400 error. I enjoyed the experience and had a lot of time spent reading documentation and testing different commands and modules to see what would work. This was a valuable learning experience.

2.  The trickiest parts for me were figuring out how config() worked with the databases and what DATABASES dict was supposed to look like in [settings.py](https://github.com/jayyargh/Hello-Django/blob/master/djorg/settings.py). I also struggled with what to use for ALLOWED_HOSTS, but left it empty in the repo and merely added a variable in heroku var configs console.

---

## Changelog / PR

- 7/30/18 --> 8/02/18 django app dev
- 03-Aug-2018 django deploy to heroku
- PR found [here](https://github.com/LambdaSchool/Hello-Django/pull/115)
