import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    p=0
    mx=0
    my=0
    for x,y in zip(a, b):
        p+=(x*y)
        mx+= x**2
        my+= y**2

    mx = mx**0.5
    my = my**0.5
    if mx==0 or my==0:
        return 0.0
    return p/(mx*my)