import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)

    # Center each feature (column) by subtracting its mean
    X_centered = X - X.mean(axis=0, keepdims=True)

    # Number of observations
    n = X.shape[0]

    # Sample covariance matrix: divide by n - 1
    covariance = (X_centered.T @ X_centered) / (n - 1)

    # Standard deviation of each feature
    std = np.sqrt(np.diag(covariance))

    # Pairwise products of standard deviations
    denominator = np.outer(std, std)

    # Start with NaN everywhere
    correlation = np.full(covariance.shape, np.nan)

    # Compute correlations only where both standard deviations are nonzero
    valid = denominator > 0
    correlation[valid] = covariance[valid] / denominator[valid]

    return correlation
    pass