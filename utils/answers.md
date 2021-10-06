### Bad example

List of issues:

* uninformative file names
* use of file name for versioning
* no comments or instructions
* uninformative variable names
* highly confusing variable name n for N^2
* (matlab) we dont know what variables are loaded
* hard coded path to the wrong place on someone elses computer
* uses a function that you don't have (which is also not informatively named)
* needs the m_map toolbox which we might not have
* needs cartopy/scipy etc. packages which we might not have installed

### Better example

List of improvements:

* more informative file names
* more informative data file name
* more informative variable names
* includes comments
* relative file path that works
* includes functions that you need as separate files

List of (now more subtle) issues:

* still assumes you have access to some non-standard packages like m_map and cartopy (the code only worked because we already installed them for the previous example)
* doesn't specify an environment (or versions) for python
* data file provided manually
* function name (`smooth`) conflicts with a built in MATLAB function
* why build your own smoothing function when it already exists! (there might be a good reason for this)
* provided functions and modules have no docstrings

### Good example

List of improvements:

* specifies a conda environment
* contains instructions and requirements
* version control with git, accessible via github
* automatic download of data and toolboxes
* Generate notebooks from python files using jupytext

List of (now very subtle) issues:

* Requires MATLAB version > 2013a for savefig function. 
