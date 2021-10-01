### Bad example

List of problems:

* uninformative file names
* use of file name for versioning is bad practice
* no comments or instructions
* uninformative variable names
* (matlab) we dont know what variables are loaded
* hard coded path to the wrong place on someone elses computer
* uses a function that you don't have (which is also not informatively named)

### Better example

List of improvements:

* more informative file names
* more informative data file name
* more informative variable names
* includes comments
* relative file path that actually works
* includes functions that you need as separate files

List of (now more subtle) problems:

* assumes you have access to some non-standard packages like m_map and cartopy
* doesn't specify an environment
* data file provided manually
* overwrote a built in matlab function
* you now have the functions and modules, however, they don't have docstrings

### Good example

* specifies a conda environment
* contains instructions and requirements
* version control with git, accessible via github
* automatic download of data and toolboxes