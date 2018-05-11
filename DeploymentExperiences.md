# Deployment Experiences

### Heroku

#### https://djorg-fwcdga48i.herokuapp.com/

## Experience

My experiences deploying went well. The instructions in the sprint striked a good balance of help and challenge. The only problem I had during deployment was:

```
remote:  !     Error while running '$ python manage.py collectstatic --noinput'.
```

I read some SO articles and I made sure the static dirs had my bookmarks (this is what I believe the problem was). I used the `os` and `print`ed out the path to make sure they were correct.

This didn't fix the error, so I eventually just disabled static collection (per Heroku recommendation) with:

```
remote:           $ heroku config:set DISABLE_COLLECTSTATIC=1
```

With this, deployment was successful but when I checked my dynos on heroku web ui, I tried to check via cli. But I got an error:

```
$ heroku ps
Free dyno hours quota remaining this month: 550h 0m (100%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

No dynos on ⬢ djorg-fwcdga48i
$ heroku ps:scale web=1
Scaling dynos... !
 ▸    Couldn't find that process type.
```

At this point I went back to searching and found out that the problem was most likely because there was no `Procfile`. This perplexed me becuse I know I created it (per the sprint challenge instruction). Then I suspected it may have been because I disabled static collection. So I re-enabled it and debugged some more. Eventually it wasn't working, so I decided to do some quick changes on my local copy.

After I was finished with this, I decided to push it to heroku. But I had apparently forgotten it was using git because I kept getting the message that everything was up to date. It took me a minute or two, but I typed `git status` and it all became clear:

```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   Pipfile
	modified:   Pipfile.lock
	modified:   bookmarks/static/bookmarks/style.css
	modified:   bookmarks/templates/bookmarks/index.html
	modified:   bookmarks/urls.py
	modified:   djorg/settings.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	Procfile

no changes added to commit (use "git add" and/or "git commit -a")
```

Now, I could all the files static collection had missed (though setting that up would make dev->deploy a lot faster I suppose).

Then I set up dynos and everything ran fine.

## Conclusion

In general, deployment with `django` and `python` went **a lot** smoother then with `node`/`express` and `MongoDB`. I do appreciate the fact that adding a few `pip`s and `settings.py` configs (and small other changes) is all you need to deploy to heroku with `django`/`python` but I _dislike_ the "black box" nature of django and miss having `React` and `Redux`. This was especially painful because I'm trying to make an SPA but all `django` refs and searches resulted in passing the `id` to a URL for `django` to use. I was able to deploy but I wasn't able to deploy a _fully featured_ app. I would even daresay I wasn't able to deploy an _mvp_ app.

Regardless, **deployment** to heroku was rather successful. :cheers:
