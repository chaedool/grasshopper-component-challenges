def unit_vector_standard(x):
    """
    Distance (standard)
    
    Args:
        x (Vector3d): Vector to unitize.
    
    Retruns:
        Unitzed vector if x can be unitized, else x.
    """

    if x.IsValid and x.Length != 0:
        x.Unitize()

    return x

a = unit_vector_standard(x)
