import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    cent = X-np.mean(X, axis = 0)
    cv = (cent.T @ cent)/(cent.shape[0] - 1)

    return cv
    pass