import numpy as np
import matplotlib.pyplot as plt
grid_points = np.arange(0,2*np.pi,.1)
grid_points = [1,2,1,2,3,4,5,3,2,1]
print(grid_points)



def local_extreme(in_list):
    diff = np.diff(in_list)
    diff = diff > 0
    diff = diff.astype(np.int)
    diff = np.diff(diff)
    print(diff)
    idx = np.where(diff==-1)[0]
    return idx + 1


output = local_extreme(grid_points)
