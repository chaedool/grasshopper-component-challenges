import math

def round_standard(x):
    """
    Round (Standard)
    
    Args:
        x (float): Input value
    
    Retruns:
        (Tuple[int, int, int])
        - Neareast integer to x.
        - Floor value of x.
        - Ceiling value of x.
    """
    
    return int(math.floor(x + 0.5)) if x >= 0 else int(math.ceil(x - 0.5)), int(math.floor(x)), int(math.ceil(x))

a, b, c = round_standard(x)
