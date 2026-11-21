import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    xbar = np.sum(x)/len(x)
    s = 0
    for xi in x:
        s+= (xi-xbar)**2

    s = (s/(len(x)-1))**0.5
    t = float((xbar - mu0)/(s/(len(x)**0.5)))
    return t
    pass