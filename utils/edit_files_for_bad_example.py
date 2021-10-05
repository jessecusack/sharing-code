# +
import os
from helpers import strip_comments, add_new_line_sep

load_dir = os.path.join("..", "better_example")
save_dir = os.path.join("..", "bad_example")

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
