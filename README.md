# Sharing Code Tutorial

The examples in this repository constitute an (opinionated) tutorial on the 'dos and donts' of sharing scientific code. It is written in python and MATLAB because both are extremely prevalent in the Earth science community. The idea is to work through the examples (following the instructions below and the README in each folder) in either (or both) programming languages. Each example progressively exposes practices and tools for sharing code and data in a way that is more reproducible. The final task involves making a personal package and hosting it on github.

## Requirements

### For *both* MATLAB and python users

* Git installed on your computer. Specifically, the command line interface.
    * For macOS users, it is probably already installed. To check, run `git --version` in a terminal and look for a sensible output. Nothing further is needed, but if you want a later version, I suggest installing via [homebrew](https://brew.sh/). First install homebrew. Then in the terminal run `brew install git`. 
    * For windows users you can download the installer from the [website](https://git-scm.com/downloads). You then have access to the `git bash` terminal as one of your applications.
* A [github.com](github.com) account.

### For python users

* `conda` installed via the [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [anaconda](https://docs.anaconda.com/anaconda/install/index.html) distributions.
* Jupyter Lab installed into fresh conda environment. First open a terminal and then install by:
  * Entering the command `conda create -n sharing-code -c conda-forge jupyterlab jupytext cookiecutter`
  * _If you want to see what this command would do without actually doing anything, add the `-d` option for dry-run._
  * Alternatively, copy paste the [environment specs](https://raw.githubusercontent.com/jessecusack/sharing-code/main/tutorial_environment.yml) and save into a file called `tutorial_environment.yml` on your computer. Then, using the terminal, run `conda env create -f tutorial_environment.yml`, or, from within the Anaconda GUI using the '[import environment](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#importing-an-environment)' feature.
  
### For MATLAB users

* MATLAB installed (Preferably a more recent version)
  * _Important_: Revert to the default MATLAB path (make sure you save your current path settings using `savepath folderName/pathdef.m` so that you can recover it later!!!)
  
## Objectives

* Download a repository from github
* List some bad coding practices (in the context of sharing code, as well as more generally)
* List some good coding practices
* Run the examples.
* Download a project template using cookiecutter
* Make your own personal package of functions in MATLAB/python, publish it to github and install it into a new environment
* List some ways of creating a DOI for your code and data

## Instructions

Imagine you are trying to understand and replicate someone's analysis of an oceanographic dataset (in this case, a single VMP profile). Further, assume that you have little to no knowledge of the standard tools and packages that we use in Earth sciences aside from a programming language. Each example is self-contained parcel of code which includes a `README` with further instructions.

Start by:

* Cloning this repository to a location on your computer e.g. `git clone https://github.com/jessecusack/sharing-code` _or_ `git clone git@github.com/jessecusack/sharing-code` if you have set up ssh key access to github.
* Open MATLAB (with your path reverted to default, see above) and/or Jupyter lab from the `sharing-code` conda environment and navigate to the repository.

Then go through:

1) [Attempt Example 1 - The bad example](bad_example)
2) [Attempt Example 2 - The good example](good_example)
3) [Attempt Example 3 - The git example](git_example)
4) [Build your own package](build_your_own_package)

# Additional Notes

Convert `presentation.txt` to a beamer pdf using pandoc:

```bash
pandoc -t beamer -s presentation.txt -o presentation.pdf
```