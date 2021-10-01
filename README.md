# Sharing Code

The examples in this repository illustrate both good and bad practise in sharing scientific code. They are written in python and MALTAB because both are extremely prevalent in the Earth science community.

## Requirements

Follow all the steps AND sub-steps.

* `conda` installed via miniconda or anaconda
* Jupyter Lab installed into fresh conda environment
  * Install using `conda create -n reusable-code -c conda-forge jupyterlab jupytext cookiecutter`
  * > If you want to see what this command would do without actually doing anything, add the `-d` option for dry-run.
* MATLAB installed on your computer. (A version from the last few years preferably)
  * Revert to the default MATLAB path (make sure you know how to recreate or somehow save your old path settings!!!)
* Git installed on your computer.
* An account on github.com.

## Goals

* Download a repository from github
* List some bad coding practises (in the context of sharing code, as well as more generally speaking)
* List some good coding practises
* Run (at least partially) the examples.
* Download a project template using cookiecutter
* Make your own person utilities package and publish it to github

## Instructions

Imagine you are trying to understand and replicate someone's analysis of some oceanographic data. They send you their code and the data. Each example is self-contained and you should attempt to run

* **Clone this repository**

* **Attempt Example 1 - The bad example**
  * More instructions are contained in the [README](bad_example/README.md) in the folder.

* **Attempt Example 2 - The better example**
  * More instructions are contained in the [README](better_example/README.md) in the folder.
