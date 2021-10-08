# Presentation notes

![](https://mk0osnewswb2dmu4h0a.kinstacdn.com/images/comics/wtfm.jpg)

# Introduction

As scientists, we are also software developers. We write code that we use and other people use. However, we have a different set of priorities from professional developers. We don't often need to write 'production ready' code to be used by millions. In fact, what we do is more exploratory and typically shared with only a small group of people (if any). However, while our livelihoods may not depend on the quality of our software, our time and energy is valuable and should not be spent debugging code. Our software should facilitate the process of doing science, not bog it down!

Recently journals have started demanding the code be shared. It is possible to create a DOI for code and data.

* [Zenodo](https://zenodo.org/) - archiving data and code
* `pypi` - uploading your package for everyone (also conda-forge)
* Data - NODC (NOAA), NCEI

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

# Styling code

In python there are community agreed 'de facto official' style guides. These can be enforced using opinionated auto-formatting tools, such as `black` and `isort`. Check your code is mostly consistent with guide e.g. `flake8`. However, these are not a replacement for good practice! (They won't write comments for you)

I don't think 'official' style guides exist for MATLAB... so just, try and be consistent! (Look at the source code of built in functions for examples)

# Keeping track of dependencies

* Python: make use of conda environments!
* MATLAB: (harder) Try to keep your path clean and make use of the `addpath` function. Keep good notes.

* Can specify commit of zip archive: https://github.com/{username}/{projectname}/archive/{sha}.zip
* Also can do this in the conda environment.

# Using more advanced tools

When code follows basic good practice, it is then a lot easier to make good use of more advanced tools like `git`, github, and `conda` environments. We will get practice using those in this tutorial.

# Before starting!

* Revert MATLAB path
* Start up Jupyter Lab from the sharing-code environment

Lets try and analyse some VMP data.

# Before the git example

* Very brief explanation of git as version control/backup system.
* Explain that we're doing to do everything that we already did, in an automated and reproducible way using git, conda environments and scripts that download things.
* Git doesn't play well with a lot of things, like data. We're going to explore ways to handle those things using scripts.
* The scripts pull toolboxes that we already used from the same website. The data is now hosted on dropbox. The extra functions are also git repositories. 
* For python users we're going to introduce a way of converting notebooks using jupytext. 

# Before building a package

* Explain the git example shared personal packages in a different way than we've seen before. For python, it was installed via a conda environment. For MATLAB it was downloaded by a script.
* We're going to try out those ideas. 

# After the tutorial comments

There are always trade-offs in time vs. usability. Creating a github repository and download scripts does take additional time. However, we can't quantify all the time that might be wasted in the future trying to debug problems. Given how many weeks (months?) I have spent debugging the code of other people, I work under the assumption that putting time in at the start is always worth it, unless in exceptional circumstances (like at sea or in the field under a time crunch - then there are other priorities like data collection). I can think of scenarios when sharing the 'good example' is perfectly acceptable, however, I cannot think of any time when sharing code lacking comments or instructions is acceptable.

* Fluency with `git` and github takes time and practice. It is an extremely comprehensive tool and I only use a small fraction of its capabilities. We didn't really dive into it all, just learned some basic commands. I would recommend doing the software carpentry tutorial on git.

# Even more advanced tools (for reference)

* Collaborating on github with pull requests and issues. 
* Using git for branching and merging new ideas. 
* Use `make` for build routines.
* Unit tests and testing frameworks like `pytest`.
* Documentation generators e.g. `sphinx`.
* Continuous integration e.g. `travis`.

The further down this list we go, the more we get into the realms of professional software development. Most scientists don't have the time or motivation to learn all these tools, but I think they *should* be aware they exist and what they aim to achieve. 

It would be nice to have a simple sketch of this.

