import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    eigenvalues = np.linalg.eigvals(matrix)
    return np.sort(eigenvalues.real).astype(float)
    pass