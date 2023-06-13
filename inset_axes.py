# Several way of creating inset axes
from matplotlib import pyplot as plt

# 1 INSIDE FIG (Figure.add_axes)
# ================
# Create inset axes giving position in Figure coordinates
# Docs: https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.add_axes
fig, ax = plt.subplots()

rect = [0.1, 0.1, 0.4, 0.2]
axins = fig.add_axes(rect)

# 2 INSIDE AXES (Axes.inset_axes)
# ================
# Same idea using Axes coordinates
# Docs: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html
fig, ax = plt.subplots()

rect = [0.1, 0.1, 0.4, 0.2]
axins = ax.inset_axes(rect)
