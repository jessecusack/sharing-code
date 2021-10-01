# +
import requests


def strip_comments(lines, comment_str="%"):
    new_text = []
    for line in lines:
        if line.startswith(comment_str):
            continue
        else:
            # Include new line separator
            new_text.append(line + "\n")
    return new_text


# +
url = "https://raw.githubusercontent.com/jessecusack/example_matlab_toolbox/main/jc_calculate_diffusivity.m"

text = requests.get(url).text.replace("jc_calculate_diffusivity", "diff")
new_text = strip_comments(text.splitlines())

with open("../better_example/diff.m", "w") as f:
    f.writelines(new_text)

# +
url = "https://raw.githubusercontent.com/jessecusack/example_matlab_toolbox/main/jc_convolve_hanning.m"

text = requests.get(url).text.replace("jc_convolve_hanning", "smooth")
new_text = strip_comments(text.splitlines())

with open("../better_example/smooth.m", "w") as f:
    f.writelines(new_text)

# +
url = "https://raw.githubusercontent.com/jessecusack/example_matlab_toolbox/main/jc_despike_threshold.m"

text = requests.get(url).text.replace("jc_despike_threshold", "despike")
new_text = strip_comments(text.splitlines())

with open("../better_example/despike.m", "w") as f:
    f.writelines(new_text)

# +
with open("../good_example/analysis/analyse_vmp_profile.m", "r") as f:
    text = f.read()

new_text = text.replace("jc_calculate_diffusivity", "diff").replace("jc_convolve_hanning", "smooth").replace("jc_despike_threshold", "despike")
new_text = new_text.replace("../data/external/vmp_profile_SPAMEX_2014.mat", "vmp_profile_SPAMEX_2014.mat")  # Use correct file location... 

new_text = text.splitlines()

with open("../better_example/analyse_vmp_profile.m", "w") as f:
    f.write(new_text)
