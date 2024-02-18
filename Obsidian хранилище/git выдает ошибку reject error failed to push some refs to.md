#git #error #reject

! rejected     igorkrisin.github.io -> igorkrisin.github.io (non-fast-forward)
error: failed to push some refs to 'https://github.com/igorkrisin/SkillFactoryHW.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

что бы это исправить неободимо сделать rebase 
```terminal
git pull --rebase имя_репозитория  имя_ветки

и после этого сделать

 git pull
 ```


так же по теме статья со SOF:

I can't push now, though I could do it yesterday.

When I use `git push origin master`, I get an error:

```
$ git remote -v
origin  https://github.com/REDACTED.git (fetch)
origin  https://github.com/REDACTED.git (push)

$ git push origin master
Username for 'https://github.com': REDACTED
Password for 'https://REDACTED@github.com':
To https://github.com/REDACTED.git
! [rejected]         master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/REDACTED.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

What my working directory and remote repository looks like:

![Screenshot of Windows file folder with these directories: .git, css, js. And these files: index.php, readme, setsu.php. The word "local" with an arrow points to the css-folder. Below, screenshot with heading "github", and a css-folder and index.php-file](https://i.stack.imgur.com/Sz17u.png)




(Note: [starting Oct. 2020](https://github.blog/changelog/2020-08-26-set-the-default-branch-for-newly-created-repositories/), any new repository is created with the default branch `main`, not `master`. And you can [rename existing repository default branch from `master` to `main`](https://github.com/github/renaming).  
The rest of this 2014 answer has been updated to use "`main`")

(The following assumes `github.com` itself is _not_ down, as [eri0o](https://stackoverflow.com/users/965638/eri0o) points out in [the comments](https://stackoverflow.com/questions/24114676/git-error-failed-to-push-some-refs-to-remote/24114760#comment121465079_24114676): see [`www.githubstatus.com`](https://www.githubstatus.com/) to be sure)

If the GitHub repo has seen new commits pushed to it, while you were working locally, I would advise using:

```
git pull --rebase
git push
```

The full syntax is:

```
git pull --rebase origin main
git push origin main
```

[With Git 2.6+](https://stackoverflow.com/a/30209750/6309) (Sept. 2015), after having done (once)

```
git config --global pull.rebase true
git config --global rebase.autoStash true
```

A simple `git pull` would be enough.  
(Note: with [Git 2.27 Q2 2020](https://stackoverflow.com/a/61562652/6309), a `merge.autostash` is also available for your regular pull, without rebase)

That way, you would replay (the `--rebase` part) your local commits on top of the newly updated `origin/main` (or `origin/yourBranch`: `git pull origin yourBranch`).

See a more complete example in the [chapter 6 Pull with rebase](http://chimera.labs.oreilly.com/books/1230000000561/ch06.html#pull-rebase) of the [Git Pocket Book](http://chimera.labs.oreilly.com/books/1230000000561).

I would recommend a:

```
# add and commit first
#
git push -u origin main

# Or git 2.37 Q2 2022+
git config --global push.autoSetupRemote true
git push
```

That would establish a tracking relationship between your local main branch and its upstream branch.  
After that, any future push for that branch can be done with a simple:

```
git push
```

Again, with [Git 2.37+ and its global option `push.autoSetupRemote`](https://stackoverflow.com/a/72401899/6309), a simple `git push` even for the first one would do the same (I.e: establishing a tracking relationship between your local `main` branch and its upstream branch `origin/main`).

See "[Why do I need to explicitly push a new branch?](https://stackoverflow.com/a/17096880/6309)".

---

Since the OP already [reset and redone its commit](https://stackoverflow.com/a/18589043/6309) on top of `origin/main`:

```
git reset --mixed origin/main
git add .
git commit -m "This is a new commit for what I originally planned to be amended"
git push origin main
```

There is no need to `pull --rebase`.

Note: `git reset --mixed origin/main` can also be written `git reset origin/main`, since the `--mixed` option is the default one when using [`git reset`](http://git-scm.com/docs/git-reset).






Report this ad

254


Try:

```
git push -f origin master
```

That should solve the problem.

Based on @Mehdi‘s comment, a clarification about `—force pushing`: The Git command above works safely only for the first commit. If there were already commits, pull requests or branches in previous, this resets all of it and set it from zero. If so, please refer @VonC‘s detailed answer for a better solution.

ссылка на статью https://stackoverflow.com/questions/24114676/git-error-failed-to-push-some-refs-to-remote


