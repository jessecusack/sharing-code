# The git example

Imagine you are attempting to replicate someone's analysis. They have shared their work which is contained in a git repository hosted on github.

https://github.com/jessecusack/example_research_project

## Instructions

* Clone the repository using the terminal `git clone https://github.com/jessecusack/example_research_project`
* Follow the **manual instructions** (don't use `setup.sh`) in the README to install the environment.
* Follow the instructions to run the analysis and look at the resulting figures.
* Did you convert the python code to a notebook and open it with Jupyter Lab? If not, try.
* After finishing the points above, look at `setup.sh`, what does it do?
* Answer the following questions:
  * How are prerequisite packages handled?
  * How is data handled?
  * Inspect the script in the `data/` directory, what is it doing?
  * Inspect the `environment.yml` file, what do you notice about the package specifications? What additional package is installed using `pip`?
  * Inspect the script in the `matlab_toolboxes/` directory, what is it doing?
    * What is contained at the top of the MATLAB analysis script that allows you to use the toolboxes?
