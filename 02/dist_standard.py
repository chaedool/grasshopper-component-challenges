def distance_standard(x, y):
    """
    Distance (standard)
    
    Args:
        x (Point3D): First point
        y (Point3D): Second point
    
    Retruns:
        Distance between two input points (number)
    """

    import math

    return math.sqrt((y.X - x.X)**2 + (y.Y - x.Y)**2 + (y.Z - x.Z)**2)

a = distance_standard(x, y)
