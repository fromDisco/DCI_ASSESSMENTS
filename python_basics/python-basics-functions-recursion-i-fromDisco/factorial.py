def factorial(n):
    """
    Calculate the factorial of n

    Arguments: 
        n (int)

    Returns: 
        int
    """
    if n <= 1:
        return 1
    
    return n * factorial(n-1)


print(factorial(0))
print(factorial(1))
print(factorial(10))