import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    s = 0.0
    for xi, pi in zip(x, p):
        s+= float(xi*pi)
    return s
    pass