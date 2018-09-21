- [Live site](https://django-sprint-lambda.herokuapp.com/)

- [Djorg project repo](https://github.com/affordances/Intro-Django)

Deployment was not fun. I hope my experience was not representative. Are web frameworks so numerous that it's impractical for Heroku to make a menu of custom configurations for each? Are the designers of web frameworks so difficult to coordinate that it's unrealistic to expect them to streamline their configuration requirements so they're easier to plug into Heroku?

Anyway, here are some of the problems I ran into:

- Overall, it's difficult to intuit what Django is doing, because its "lifecycle" (in the React sense) is opaque. It's not clear how things connect, or in what order they run. This makes troubleshooting very difficult.

- There's no satisfaction associated with understanding how a Django thing works. It doesn't feel like "oh that makes sense", it feels like "...but why?".

- I don't know why the `DATABASES` declaration is correct, or why `dj_database_url` is needed. But it works, somehow. From their Github: `The dj_database_url.config method returns a Django database connection dictionary, populated with all the data specified in your URL.` Okay, where does it return that dictionary? What uses it?

- There is nothing intuitive about the static files configuration, but getting it right is crucial to deployment. What is the relationship between `STATIC_ROOT`, `STATIC_URL`, and `STATICFILES_DIRS`? Why does Heroku need them? Through trial and error and much googling, I eventually made them work, but I don't know WHY they work. Why, for example, do I need a `.keep` file inside the `static` folder for the build to work?

- Shouldn't it be bad that `djorg` and `notes` are only ambiguously connected within `Intro-Django`? Shouldn't `notes` be inside `djorg`? Again, the lack of clear pipelines between different pieces of the app makes everything a baffling ordeal.
