def unit_x_standard(x):
    """
    Unit X (standard)
    
    Args:
        x (float): Input value
    
    Retruns:
        Vector X multiplied by x
    """
    
    import Rhino.Geometry as rg
    
    return rg.Vector3d(x, 0, 0)

a = unit_x_standard(x)
