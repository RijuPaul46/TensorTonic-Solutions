import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    a=np.array(A)
    det=np.linalg.det(a)
    if det==0:
        return 
    return np.linalg.inv(a)
    pass
