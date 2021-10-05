# Presentation notes

![](https://mk0osnewswb2dmu4h0a.kinstacdn.com/images/comics/wtfm.jpg)

# Introduction

As scientists, we are also software developers. We write code that we use and other people use. However, we have a different set of priorities from professional developers. We don't often need to write 'production ready' code to be used by millions. In fact, what we do is more exploratory and typically shared with only a small group of people (if any). However, while our livelihoods may not depend on the quality of our software, our time and energy is 'expensive' and should not be spent debugging code. Our software should facilitate the process of doing science, not bog it down!

Software development tools are highly under-utilised in the Earth sciences. Although, less so in the numerical modeling community, who have adopted some tools and are spearheading the development of awesome projects (like `xarray`). But definitely in the observational community. I'm not sure why... but it is high time that changed!

Ask yourself:

* How do we share data and software? Via email? Dropbox? On github?
* How often does this work when you hit run for the first time?
* What makes it more likely that the code will run without fuss? Good instructions, perhaps?

# Basic good practice (not exhaustive)

A prerequisite to sharing any code is to follow **good practice** when writing it.

We _all_ write bad code form time to time! Usually because we're under pressure or in a rush. This is not an exercise in finger pointing! A goal is to have good practice built into 'muscle memory' so that even when we're in a rush, we still write somewhat passable code. This tutorial goes over best practice for a variety of situations, and also introduces some tools that make our lives a lot easier (`git` and github). 

* Use comments extensively!
* Adopt a consistent style
* Use sensible variable and function names
* Use functions to isolate repeated elements (and write docstrings for them!!!)
* Don't reinvent the wheel, use existing modules and packages whenever possible (additionally, keep track of the modules and packages that your code relies on!)
* Use the latest tools (yes I'm looking at those of you who still run MATLAB 2007 or use the old seawater toolbox)

There are a lot of more points that are more relevant to software developers. For scientists the above list is a good minimum. Could we add any more? Any pet-peeves?

# Styling python code

Use opinionated auto-formatting tools, such as `black` and `isort`. Check your code is mostly consistent with standards e.g. `flake8`. 

I don't think standards even exist for MATLAB... so just, try and be consistent! (Look at the source code of built in functions for examples)

# Using more advanced tools

When code follows basic good practice, it is then a lot easier to make good use of more advanced tools like `git`, github, and `conda` environments. We will get practice using those in this tutorial.

# Even more advanced tools (for reference)

* Collaborating on github with pull requests and issues. 
* Using git for branching and merging new ideas. 
* Use `make` for build routines.
* Unit tests and testing frameworks like `pytest`.
* Documentation generators e.g. `sphinx`.
* Continuous integration e.g. `travis`.

The further down this list we go, the more we get into the realms of professional software development. Most scientists don't have the time or motivation to learn all these tools, but I think they *should* be aware they exist and what they aim to achieve. 

# After the tutorial comments

There are always trade-offs in time vs. usability. Creating a github repository and download scripts does take additional time. However, we can't quantify all the time that might be wasted in the future trying to debug problems. Given how many weeks (months?) I have spent debugging the code of other people, I work under the assumption that putting time in at the start is always worth it, unless in exceptional circumstances (like at sea or in the field under a time crunch - then there are other priorities like data collection). I can think of scenarios when sharing the 'better example' is perfectly acceptable, however, I cannot think of any time when sharing the 'bad example' is acceptable.

* Fluency with `git` and github takes time and practice. I only use a small fraction of their capabilities. 

# Open Access

It is possible to create a DOI for code and data.

* [Zenodo](https://zenodo.org/) - archiving data and code
* `pypi` - uploading your package for everyone (also conda-forge)