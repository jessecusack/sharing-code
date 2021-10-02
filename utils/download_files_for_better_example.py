# +
import requests
import os
from helpers import strip_comments, add_new_line_sep, remove_function_docstrings

save_dir = os.path.join("..", "better_example")

# +
url = "https://raw.githubusercontent.com/jessecusack/example_matlab_toolbox/main/jc_calculate_diffusivity.m"

text = requests.get(url).text.replace("jc_calculate_diffusivity", "rdiff")
new_text = strip_comments(text.splitlines())

with open(os.path.join(save_dir, "rdiff.m"), "w") as f:
    f.writelines(add_new_line_sep(new_text))

# +
url = "https://raw.githubusercontent.com/jessecusack/example_matlab_toolbox/main/jc_convolve_hanning.m"

text = requests.get(url).text.replace("jc_convolve_hanning", "smooth")
new_text = strip_comments(text.splitlines())

with open(os.path.join(save_dir, "smooth.m"), "w") as f:
    f.writelines(add_new_line_sep(new_text))

# +
url = "https://raw.githubusercontent.com/jessecusack/example_matlab_toolbox/main/jc_despike_threshold.m"

text = requests.get(url).text.replace("jc_despike_threshold", "despike")
new_text = strip_comments(text.splitlines())

with open(os.path.join(save_dir, "despike.m"), "w") as f:
    f.writelines(add_new_line_sep(new_text))

# +
url = "https://raw.githubusercontent.com/jessecusack/example_research_project/main/analysis/analyse_vmp_profile.m"

text = requests.get(url).text

# Mangle names
new_text = text.replace("jc_calculate_diffusivity", "rdiff").replace("jc_convolve_hanning", "smooth").replace("jc_despike_threshold", "despike")
# Use correct file location... 
new_text = new_text.replace("../data/external/vmp_profile_SPAMEX_2014.mat", "vmp_profile_SPAMEX_2014.mat")
# Change figure output dir
new_text = new_text.replace("../figures/", "")

# Cut out the toolboxes bit
new_text = strip_comments(new_text.splitlines(), "addpath")
new_text = strip_comments(new_text, "% Import toolboxes!")

with open(os.path.join(save_dir, "analyse_vmp_profile.m"), "w") as f:
    f.writelines(add_new_line_sep(new_text))

# +
url = "https://raw.githubusercontent.com/jessecusack/example_research_project/main/analysis/analyse_vmp_profile.py"

# Mangle names
text = requests.get(url).text.replace("calculate_diffusivity", "rdiff").replace("convolve_hanning", "smooth").replace("despike_threshold", "despike")
# Use correct file location... 
new_text = text.replace("../data/external/vmp_profile_SPAMEX_2014.mat", "vmp_profile_SPAMEX_2014.mat")
# Change figure output dir
new_text = new_text.replace("../figures/", "")
# Change import utils
new_text = new_text.replace("from example_python_package ", "")

tmp_file = "_tmp_.py"

with open(tmp_file, "w") as f:
    f.write(new_text)
    
save_to = os.path.join(save_dir, "analyse_vmp_profile.ipynb")
os.system(f"source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base && jupytext --set-formats .ipynb --from py:percent --to ipynb -k python3 -o {save_to} {tmp_file}")

os.remove(tmp_file)

# +
# The error above is not a problem I think

# +
url = "https://raw.githubusercontent.com/jessecusack/example_python_package/main/example_python_package/utils.py"

text = requests.get(url).text.replace("calculate_diffusivity", "rdiff").replace("convolve_hanning", "smooth").replace("despike_threshold", "despike").replace("_np", "np")

text = remove_function_docstrings(text)

# Remove module description
new_text = text.splitlines()[1:]

with open(os.path.join(save_dir, "utils.py"), "w") as f:
    f.writelines(add_new_line_sep(new_text))
