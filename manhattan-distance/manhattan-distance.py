import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x,y=np.array(x,dtype=float),np.array(y,dtype=float)
    return np.linalg.norm((x-y),ord=1)
    pass