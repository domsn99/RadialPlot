import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import imageio.v2 as imageio

def profile(op, data, center):
    switch={
        1: circular_profile(data, center),
        2: quadrant_profile(data, center, 1),
        3: quadrant_profile(data, center, 2),
        4: quadrant_profile(data, center, 3),
        5: quadrant_profile(data, center, 4),
    }
    return switch.get(op,'Invalid option')

def quadrant_profile(data, center, quadrant):
    # Checks data type. jpg and png have shape (y,x,misc)
    if (len(data.shape)>2):
        y, x, misc = np.indices((data.shape))
    else:
        y, x = np.indices((data.shape))

    # Creates an array of distances from the centre to the set radius of the profile. 
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)

    # Convert array data to integer.
    r = r.astype(int)

    # Chosen quadrant is used as the data points
    if (quadrant==1):
        quadrant_data = data[:center[1],:center[0]]
        quadrant_radius = r[:center[1],:center[0]]

    elif (quadrant==2):
        quadrant_data = data[:center[1],center[0]:len(x)]
        quadrant_radius = r[:center[1],center[0]:len(x)]

    elif (quadrant==3):
        quadrant_data = data[center[1]:len(y),:center[0]]
        quadrant_radius = r[center[1]:len(y),:center[0]]

    elif (quadrant==4):
        quadrant_data = data[center[1]:len(y),center[0]:len(x)]
        quadrant_radius = r[center[1]:len(y),center[0]:len(x)]
        

    # Count bins from 0 to r in data. ravel() returns single entries of the whole array.
    tbin = np.bincount(quadrant_radius.ravel(), quadrant_data.ravel())
    # Bincounting for normalizing the profile.
    nr = np.bincount(quadrant_radius.ravel())

    # Normalize quadrant profile and return.
    quadrantprofile = tbin / nr
    return quadrantprofile


def circular_profile(data, center):
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
    circularprofile = tbin / nr
    return circularprofile 