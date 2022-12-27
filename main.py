import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image
import imageio.v2 as imageio
from functions import *

center, zlp, radi = (478, 489), 0, 400
data_start=1
data_end=1
average_window=6
scale=5.6e-2
plotlabel=" eV"
multiple_plots=False
sum_plot=False
save_plot=False
show_plot=True
data_path="data\\"
save_path="plots\\"
save_name="1"

for i in range(data_start,data_end+1):
    data = np.array(imageio.imread(data_path+str(i)+'.tif'))
    rad = radial_profile(data, center)
    for k in range(zlp):
        rad[k]=rad[radi-k]
    avg_y=[]

    for k in range(len(rad)-average_window+1):
        avg_y.append(np.mean(rad[k:k+average_window]))
    plt.plot(avg_y[0:radi],label=str(i)+plotlabel)

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
