# Sharing Code

The examples in this repository illustrate both good and bad practise in sharing scientific code. They are written in python and MALTAB because both are extremely prevalent in the Earth science community.

## Requirements

Follow all the steps AND sub-steps.

* `conda` installed via miniconda or anaconda
* Jupyter Lab installed into fresh conda environment
  * Install using `conda create -n sharing-code -c conda-forge jupyterlab jupytext cookiecutter`
  * > If you want to see what this command would do without actually doing anything, add the `-d` option for dry-run.
* MATLAB installed on your computer. (A version from the last few years preferably)
  * Revert to the default MATLAB path (make sure you save your current path settings using `savepath folderName/pathdef.m` so that you can recover it later!!!)
* Git installed on your computer.
* An account on github.com.

## Goals

* Download a repository from github
* List some bad coding practises (in the context of sharing code, as well as more generally speaking)
* List some good coding practises
* Run (at least partially) the examples.
* Download a project template using cookiecutter
* Make your own person utilities package and publish it to github
* Install your package into a new environment

## Instructions

Imagine you are trying to understand and replicate someone's analysis of some oceanographic data. They send you their code and the data. Each example is self-contained and you should attempt follow the instructions within.

1) **Clone this repository**
1) **Attempt Example 1 - The bad example**
  1) More instructions are contained in the [README](bad_example/README.md) in the folder.
1) **Attempt Example 2 - The better example**
  1) More instructions are contained in the [README](better_example/README.md) in the folder.
1) **Attempt Example 3 - The good example**
1) More instructions are contained in the [README](good_example/README.md) in the folder.
1) **Start your own project from a cookiecutter**

Sorry MATLAB users, I didn't make a cookiecutter for you. Instead, try using the [example package](https://github.com/jessecusack/example_matlab_toolbox) as a template.
