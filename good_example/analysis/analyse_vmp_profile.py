# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: vmp-proj
#     language: python
#     name: vmp-proj
# ---

# %% [markdown]
# # Analysis of an individual VMP profile
#
# Import packages.
# %%
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as io
from example_python_package import utils

# %% [markdown]
# Load data.

# %%
vmp_profile = io.loadmat(
    "../data/external/vmp_profile_SPAMEX_2014.mat", squeeze_me=True
)

# %% [markdown]
# Where is this profile located?

# %%
proj = projection = ccrs.Orthographic(vmp_profile["lon"], vmp_profile["lat"])

fig, ax = plt.subplots(subplot_kw=dict(projection=proj))
ax.set_global()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.plot(vmp_profile["lon"], vmp_profile["lat"], "ro", transform=ccrs.PlateCarree())
ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)

fig.savefig(
    "../figures/profile_location_python.png",
    dpi=180,
    bbox_inches="tight",
    pad_inches=0.1,
)

# %% [markdown]
# What does the data look like?

# %%
fig, ax = plt.subplots()
ax.plot(vmp_profile["temperature"], vmp_profile["depth"])
ax.set_xlabel("Temperature [deg C]")
ax.set_ylabel("Depth [m]")
ax.invert_yaxis()

# %%
fig, ax = plt.subplots()
ax.semilogx(vmp_profile["dissipation"], vmp_profile["depth"])
ax.set_xlabel(r"$\varepsilon$ [W kg-1]")
ax.set_ylabel("Depth [m]")
ax.invert_yaxis()

# %%
fig, ax = plt.subplots()
ax.plot(vmp_profile["N_squared"], vmp_profile["depth"])
ax.set_xlabel("N2 [s-2]")
ax.set_ylabel("Depth [m]")
ax.invert_yaxis()

# %% [markdown]
# Buoynacy frequency has some spikes! We need to get rid of those.

# %%
N2_clean = utils.despike_threshold(vmp_profile["N_squared"])

# %%
fig, ax = plt.subplots()
ax.plot(N2_clean, vmp_profile["depth"])
ax.set_xlabel("N2 [s-2]")
ax.set_ylabel("Depth [m]")
ax.invert_yaxis()

# %% [markdown]
# This looks a lot better.
#
# But there are negative values and it seems noisy so we should smooth.

# %%
N2_smooth = utils.convolve_hanning(N2_clean, win=60)

fig, ax = plt.subplots()
ax.plot(N2_clean, vmp_profile["depth"])
ax.plot(N2_smooth, vmp_profile["depth"])
ax.set_xlabel("N2 [s-2]")
ax.set_ylabel("Depth [m]")
ax.invert_yaxis()
ax.set_xlim(-0.2e-5, 1e-5)

# %% [markdown]
# Even better, but there are still a few negative values we want to exclude.

# %%
# Clean up negative values and small values of N2
N2_smooth[N2_smooth < 1e-7] = np.NaN

# %% [markdown]
# Calculate the turbulent diffusivity.

# %%
Krho = utils.calculate_diffusivity(vmp_profile["dissipation"], N2_smooth, 0.2)

# %% [markdown]
# Save the result.

# %%
fig, ax = plt.subplots()
ax.semilogx(Krho, vmp_profile["depth"])
ax.set_xlabel(r"$K_{\rho}$ [m2 s-1]")
ax.set_ylabel("Depth [m]")
ax.invert_yaxis()

fig.savefig(
    "../figures/diffusivity_python.png", dpi=180, bbox_inches="tight", pad_inches=0.1
)
