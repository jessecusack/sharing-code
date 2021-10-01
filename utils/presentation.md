# Presentation notes

![](https://mk0osnewswb2dmu4h0a.kinstacdn.com/images/comics/wtfm.jpg)

## Introduction

* How do we share data and code? Via email? Dropbox? On github?
* How many times does this work when you hit run for the first time?

A prerequisite to sharing any code is to follow **good practice** when writing it.

## Basic good practice (not exhaustive)

* Include comments and docstrings
* Adopt a consistent style
* Use functions to isolate repeated elements
* Use sensible variable and function names
* Don't reinvent the wheel, use existing modules and packages when possible

There are a lot of more points that are more relevant to software developers. For scientists the above list is a more reasonable minimum. Could we add any more? Any pet-peeves?

## Styling python code

Use opinionated auto-formatting tools, such as `black` and `isort`. Check your code is mostly consistent with standards e.g. `flake8`. 

I don't think standards even exist for MATLAB... so just, try and be consistent! (Look at the source code of built in functions for examples)

## Using more advanced tools

When code follows basic good practice, it is then a lot easier to make good use of more advanced tools like `git`, github, and `conda` environments.

## Even more advanced tools (for reference)

* Collaborating on github with pull requests and issues. 
* Using git for branching and merging new ideas. 
* Use `make` for build routines.
* Unit tests and testing frameworks like `pytest`.
* Documentation e.g. `sphinx`.
* Continuous integration e.g. `travis`.

The further down this list we go, the more we get into the realms of professional software development. Most scientists don't have the time or motivation to learn all these tools, but I think they *should* be aware they exist and what they aim to achieve. 

## Open Access

It is possible to create a DOI for code and data.

* Zenodo - archiving data and code
* `pypi` - uploading your package for everyone (also conda-forge)