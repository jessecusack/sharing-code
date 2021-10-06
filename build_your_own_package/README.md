# 1. Build The Package!
## MATLAB

Open a terminal and navigate somewhere you're happy to create a new folder. 

Create a folder with the name of your package, e.g.

```bash
mkdir my_package
```

Look at https://github.com/jessecusack/example_matlab_toolbox for an example of what files you can add. I added license and author files to mine, however, these are not mandatory. There is nothing special about a MATLAB package, it is just a folder with functions inside.

Create a simple MATLAB function and save it inside the folder. Check that it works, give it a docstring if you like!

```octave
function [s] = half_sum(x)
s = sum(x)/2
end
```

Now you can proceed to the git section.


## Python

Unlike MATLAB, python packages have some additional boilerplate which can be a bit tedious to create by hand. Fortunately, templates exist called cookiecutters, and we will use one to speed things up. I created this [really simple one](https://github.com/jessecusack/cookiecutter-bare-bones-python-package), but much better ones exist.

Open a terminal and navigate somewhere you're happy to create a new folder. 

Activate the `sharing-code` environment, since we installed `cookiecutter` into this environment.

```bash
conda activate sharing-code
```

Using cookiecutter, create the boilerplate for your package by following the prompts, e.g. 

```bash
cookiecutter gh:jessecusack/cookiecutter-bare-bones-python-package
```

Open Jupyter Lab and navigate to your new package folder. It is quite empty right now. Look inside the folder which is named like your package. It should only contain an empty file called `__init__.py`, which is required by python to understand that this is a package but otherwise does not need to contain any information. Create a new python module (say, `utils.py`) for example. Edit your module to add a function that does something very simple and makes use of an external package (like `numpy` for example). For example,

```python
import numpy as np

def half_sum(x):
    return np.sum(x)/2
```

Do a quick check of your function by opening up a python console (from the Jupyter Lab launcher), and copy past it into the terminal. Try and run your function, does it work?

Now, going back to the main directory, notice that there is a file called `setup.cfg`. Close to the bottom of this file is a line that starts with `install_requires =`. After the `=`, add your dependencies (in my case, just `numpy`). 

Now you've done everything you need to do to qualify this as a python package! You can now proceed to the git section. 

# 2. Git and github

Next, initialise the folder as a git repository. Within the main package directory, run `git init`. 

We must create a commit to save the state of our new package. In the terminal, run:

```bash
git add .    # This 'stages' *all* the files for the commit. You can specify files individually too.
git commit -m 'an informative commit message'  # This does the commit
```

We just used git to version control our code! If you make subsequent changes, you can add, then commit them in a similar way.

Now go to [github.com](github.com) and log in. On the website, create a new repository with the same name as your package. It may ask if you want to add a README or LICENSE, don't do this because you already have those. Make note of the URL of your repository. Next we need to 'add the remote', so git knows about this online repository. Going back to the terminal, do something like:

```bash
git remote add origin https://github.com/[your_user_name]/[your_repository_name]
```

Git now knows there is a remote repository (called 'origin') at the given URL.

Next, push your commits to the remote repository. You do this by:

```bash
git push origin main    # it might be `master` rather than `main`
```

You may have to create an authentication token for this to work. 

If all went well, you should now see your package on github.com! (Go see)

# 3. Bonus - install your package to a new environment

## MATLAB

Create a script to download your package from git, look at the `git_example` that we did earlier for an example.

Create another script that uses `addpath` to load your package and then makes use of your function. 

## Python

Create an environment file `environment.yml` which installs your package via `pip`. Look at the `git_example` for an example. Make sure it also installs `ipython`. 

Try running `conda env create -f environment.yml`. Did it install your package? To check if it worked, do something like:

```ipython
conda activate [your_environment_name]
ipython
>> import your_package_name.your_module_name as xyz
>> xyz.your_function([1, 2, 3, 4])
```