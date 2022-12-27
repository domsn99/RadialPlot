import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import imageio.v2 as imageio

def radial_profile(data, center):
    # Checks data type. jpg and png have shape (y,x,misc)
    if (len(data.shape)>2):
        y, x, misc = np.indices((data.shape))
    else:
        y, x = np.indices((data.shape))

    # Creates an array of distances from the centre to the set radius of the profile. 
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)

    # Convert array data to integer.
    r = r.astype(int)

    # Count bins from 0 to r in data. ravel() returns single entries of the whole array.
    tbin = np.bincount(r.ravel(), data.ravel())
    # Bincounting for normalizing the profile.
    nr = np.bincount(r.ravel())

    # Normalize radial profile and return.
    radialprofile = tbin / nr
    return radialprofile 