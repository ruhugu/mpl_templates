from matplotlib import pyplot as plt

fig, ax = plt.subplots()

# Arrow with label
arrow_pos = np.array((0.68, 0.65))
arrow_size = -0.25*np.array((0.3, 1))
arrow_width = 0.01
arrow_color = "#A468ED"
ax.arrow(
        *arrow_pos, *arrow_size,
        head_width=3*arrow_width, width=arrow_width, linewidth=0, 
        color=arrow_color, alpha=1,
        length_includes_head=True, zorder=100)
ax.text(*((arrow_pos+1.03*arrow_size)), r"with label $uparrow$", va="top", ha="center")
