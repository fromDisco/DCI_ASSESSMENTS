def harmonic_sum(n):
    """
    Return harmonic sum of n

    Parameters: 
        n (int)

    Returns:
        (int)
    """
    if n <= 1:
        return 1
    
    # 1/n + harmonic_sum(n-1)
    # returns 1 at base case
    # that result in:
    # 1/2 + 1 
    # in the function which did
    # the last function call, 
    # before base case. next is:
    # 1/3 + 1.5 -> 1/3 + 1/2 + 1 
    # ...
    return 1/n + harmonic_sum(n-1)


print(harmonic_sum(7))
print(harmonic_sum(4))