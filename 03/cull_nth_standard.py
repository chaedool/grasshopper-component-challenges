def cull_nth_standard(x, y):
    """
    Cull nth (Standard)
    
    Args:
        x (List[Any]): List to cull.
        y (int): Cull yth.
    
    Retruns:
        (List[Any])
        Culled list.
        
    """
   
    return [item for i, item in enumerate(x) if (i+1) % y != 0]

a = cull_nth_standard(x, y)
