def sum_series(n):
    """
    Return sum of n + (n-2) + (n-4) ...

    Parameters:
        n (int)

    Returns: 
        (int)
    """
    if n <= 0:
        return 0

    return n + sum_series(n-2)


print(sum_series(7))
