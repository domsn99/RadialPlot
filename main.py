# Modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image
import imageio.v2 as imageio

# Outsourced functions
from functions import *

# Set centre of the radial distribution. 
# ZLP radius can be set if centre beam is magnitudes higher than the rest and makes the plot confusing.
# Radi determines the radius which should be integrated.
center, zlp, radi = (478, 489), 0, 400

# If multiple plots should be overlapped, this can be set to the desired amount.
data_start, data_end = 1,1

# The plots are smoothed with a moving average, where the window can be variied.
average_window=6

# This sets the scale of the data points [e.g. urad/px].
scale=5.6e-2

# Setting the label of the plot.
plotlabel=" eV"

multiple_plots=False
sum_plot=False
save_plot=False
show_plot=True
data_path, data_format = "data\\",".tif"
save_path, save_name = "plots\\","plot"


for i in range(data_start,data_end+1):
    # Load data into array and create radial profile.
    data = np.array(imageio.imread(data_path+str(i)+data_format))
    rad = radial_profile(data, center)

    # If zlp is set, the first zlp data points are swapped with data from the outer array.
    for k in range(zlp):
        rad[k]=rad[radi-k]

    # Averaging of the plot.
    avg_y=[]
    for k in range(len(rad)-average_window+1):
        avg_y.append(np.mean(rad[k:k+average_window]))
    plt.plot(avg_y[0:radi],label=str(i)+plotlabel)

# Customizing the plot.
xscale = np.array(range(zlp,radi,50))
plt.xticks(np.round(xscale, 3),np.round(xscale*scale, 3))
plt.yscale("log")
plt.xlabel("Radius [urad]")
plt.ylabel("Counts")
plt.legend()

if (save_plot):
    plt.savefig(save_path+save_name+'.png',bbox_inches='tight', dpi=150)

if (show_plot):
    plt.show()
