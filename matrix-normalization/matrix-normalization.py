import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    a = np.array(matrix, dtype=float)

    if norm_type == "l1":
        norms = np.sum(np.abs(a), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norms = np.sqrt(np.sum(a * a, axis=axis, keepdims=True))
    elif norm_type == "max":
        norms = np.max(np.abs(a), axis=axis, keepdims=True)
    else:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")

    # Avoid division by zero: zero-norm slices remain all zero.
    safe_norms = np.where(norms == 0, 1.0, norms)
    return a / safe_norms
    pass