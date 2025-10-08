def closest_point_easy(x, y):
    """
    Closest Point (Easy)
    
    Args:
        x (Point3d): Point to search from.
        y (List[Point3d]): List of points to search.
    
    Retruns:
        (Tuple[Point3d, int, float])
        - Closest point from P in C.
        - Index of closest point in C.
        - Distance from closest point in C to P.
        
    """

    closest_pt = None
    closest_idx = -1
    min_dist = float('inf')

    for i, pt in enumerate(y):
        dist = x.DistanceTo(pt)
        if dist < min_dist:
            closest_pt = pt
            closest_idx = i
            min_dist = dist
    
    return closest_pt, closest_idx, min_dist

a, b, c = closest_point_easy(x, y)
