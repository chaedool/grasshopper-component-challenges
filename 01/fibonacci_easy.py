def fibonacci_easy(x, y, z):
    """
    Fibonacci (Easy)
    
    Args:
        x (float): First seed number for fibonacci sequence.
        y (float): Second seed number for fibonacci sequence.
        z (int): Number of values in the sequence.
    
    Retruns:
        (List[float])
        First N + 2 values of fibonacci sequnce generated with seed A and B. The sequence starts with [A, B].
        
    """

    fib = [x, y]
    for i in range(z):
        fib.append(fib[-1] + fib[-2])

    return fib

a = fibonacci_easy(x, y, z)
