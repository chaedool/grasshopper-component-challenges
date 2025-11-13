import Rhino.Geometry as rg

def box_2pt_easy(x, y):
    """
    Box 2Pt (Easy)
    
    Args:
        x (Point3D): First corner.
        y (Point3D): Second corner.
    
    Retruns:
        (Box)
        Box with corner x, y, created in World XY.
    """

    return rg.Box(rg.BoundingBox(x, y))

a = box_2pt_easy(x, y)
