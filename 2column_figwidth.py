# In APS journals, columns have a width of 8.6cm or 3.375in.
# Fontsize is 12pt (not sure)
# It looks better if I use latex fonts

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

# Set fontsize and latex font (uses LaTeX)
mpl.rcParams.update({'font.size': 10})
plt.rcParams["text.usetex"] = True
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["font.serif"] = "STIX"
mpl.rcParams["mathtext.fontset"] = "stix"

fig, ax = plt.subplots(figsize=3.375*np.array([1, 0.5]))

