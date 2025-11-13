def delete_consecutive_standard(x, y):
    """
    Delete Consecutive (Standard)
    
    Args:
        x (List[Any]): List to process.
        y (bool): Wrap list.
    
    Retruns:
        (List[Any], int)
        - New list with consecutive same items removed.
        - Number of removed Items.
        
    """

    L = [x[0]]
    C = 0

    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            C += 1
        else:
            L.append(x[i])

    if y == True and len(L) > 1 and L[0] == L[-1]:
        L = L[:-1]
        C += 1

    return L, C

a, b = delete_consecutive_standard(x, y)
