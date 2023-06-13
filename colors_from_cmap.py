def color_dict_from_cmap(array, cmap, cmin=0, cmax=1):
  """Create dict of colors with color values linear on array data between cmin and cmax."""
    # Create list of color values according to the data
    cs = cmin + (array - np.amin(array))*(cmax-cmin)/(np.amax(array) - np.amin(array))
  
    # Create dict
    color_dict = {
            value : cmap(c)
            for c, value in zip(cs, array)}
    return color_dict
  
  
# Data array
array = np.array(...)

# Get colormap
import palettable.colorbrewer as cbrewer
cmap = cbrewer.sequential.Blues_9.mpl_colormap(c)
cmin = 0.4  # Maximum and
cmax = 1    # minimum color values

# Create color dict
color_dict = color_dict_from_cmap(
        array, cmap, cmin=cmin, cmax=cmax)
