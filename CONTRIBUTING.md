Thank you for your interest in contributing to Bussard!

## Branches

While `main` is the default branch, please base your contributions on `dev`. `main` is the public face of the repository; `dev` is where we do the work, and it gets merged into `main` every week or so.

This will, I'm afraid, require you to manually rebase your PRs at the moment. I'm working on a solution to this.

## Virtual environments

This is not required, but probably a good practice. I use [virtualenv](https://virtualenv.pypa.io/en/latest/) to set up a virtual environment for installing Python modules; this allows me to silo all of the modules used in this project, which is especially useful if other projects - or your main environment - require or have different versions of these modules.

Once you're in the virtual environment - or if you don't care to use one - you can use

`pip install -r requirements.txt`

to get the modules necessary for `bussard` installed.

## pre-commit

I use [pre-commit](https://pre-commit.com/) to ensure that all of my contributions look a certain way, and I encourage you to do so as well. My full `.pre-commit-config.yml` is included in the repository; at the moment, the really important hooks to me are `black` (a strict Python code formatter), `isort` (keeps Python imports in a readable order), and `no-commit-to-branch` (makes sure you aren't trying to commit directly to `dev` or `main`), but I like to use the rest of the hooks to keep things tidy.

Once you've installed `pre-commit` and run `pre-commit install` in the `bussard` directory, it should run automatically whenever you `git commit`, and will give you a readout of what it finds - and won't let you proceed with the commit if any of them fail. Several of the hooks, including `black` and `isort`, will make the necessary changes for you, so all you have to do is `git add` the changed files - I prefer `git add -i` so I can review which files were changed - and then try the `git commit` again.
