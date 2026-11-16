import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean_x = sum(x) / len(x)
    s = 0
    for xi in x:
        s += (xi-mean_x)**2

    var = s/(len(x)-1)
    std = var**0.5

    return {
        "variance":var,
        "standard_deviation":std
    }
    pass