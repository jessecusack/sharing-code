# +
import requests
import os
from helpers import strip_comments, add_new_line_sep, remove_function_docstrings

save_dir = os.path.join("..", "bad_example")

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
# -

print("I don't think the above error was a problem...")

# +
url = "https://raw.githubusercontent.com/jessecusack/example_python_package/main/example_python_package/utils.py"

text = requests.get(url).text.replace("calculate_diffusivity", "rdiff").replace("convolve_hanning", "smooth").replace("despike_threshold", "despike").replace("_np", "np")

text = remove_function_docstrings(text)

# Remove module description
new_text = text.splitlines()[1:]

with open(os.path.join(save_dir, "utils.py"), "w") as f:
    f.writelines(add_new_line_sep(new_text))
# -

load_dir = os.path.join("..", "bad_example")

# +
with open(os.path.join(load_dir, "analyse_vmp_profile.m"), "r") as f:
    text = f.read()
      
text = text.replace("vmp_profile = load('vmp_profile_SPAMEX_2014.mat');", "load('/Users/johnsmith/mydata/dat.mat');")
text = text.replace("vmp_profile.depth", "d")
text = text.replace("vmp_profile.temperature", "tmp")
text = text.replace("vmp_profile.salinity", "sal")
text = text.replace("vmp_profile.dissipation", "e")
text = text.replace("vmp_profile.N_squared", "n")
text = text.replace("vmp_profile.lat", "lat")
text = text.replace("vmp_profile.lon", "lon")
text = text.replace("N2_clean", "nc")
text = text.replace("N2_smooth", "ns")
    
new_text = strip_comments(text.splitlines())

with open(os.path.join(save_dir, "analyse_data_v2.m"), "w") as f:
    f.writelines(add_new_line_sep(new_text))

# +
with open(os.path.join(load_dir, "analyse_vmp_profile.ipynb"), "r") as f:
    text = f.read()
    
text = text.replace("vmp_profile_SPAMEX_2014", "dat")
text = text.replace("vmp_profile", "dat")
text = text.replace(""""depth""", """"d""")
text = text.replace(""""temperature""", """"tmp""")
text = text.replace(""""salinity""", """"sal""")
text = text.replace(""""dissipation""", """"e""")
text = text.replace(""""N_squared""", """"n""")
text = text.replace("N2_clean", "nc")
text = text.replace("N2_smooth", "ns")

with open(os.path.join(save_dir, "analyse_data_v2.ipynb"), "w") as f:
    f.write(text)
    
import nbformat as nbf
ntbk = nbf.read(os.path.join(save_dir, "analyse_data_v2.ipynb"), nbf.NO_CONVERT)
ntbk.cells = [cell for cell in ntbk.cells if cell.cell_type != "markdown"]
nbf.write(ntbk, os.path.join(save_dir, "analyse_data_v2.ipynb"), version=nbf.NO_CONVERT)
