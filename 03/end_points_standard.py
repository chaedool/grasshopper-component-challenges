def end_points_standard(x):
    """
    End Points (Standard)
    
    Args:
        x (Curve): Curve
    
    Retruns:
        (Tuple[Point3d, Point3d])
        - Start point of curve x.
        - End point of curve x.
    """
    
    return x.PointAtStart, x.PointAtEnd

a, b = end_points_standard(x)
