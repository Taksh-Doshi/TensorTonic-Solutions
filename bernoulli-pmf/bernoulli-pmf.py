import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    f = 1-p
    temp = []

    for a in x:
        if a == 0:
            temp.append(f)
        else:
            temp.append(p)
    mue = float(p)
    var = float(p*f)
    pmf = np.array(temp)
    return{
        "pmf":pmf,
        "mean":mue,
        "variance":var
    }
    pass