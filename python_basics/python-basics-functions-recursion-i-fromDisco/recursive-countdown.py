def countdown(n):
    """
    Count down from n to 0

    Parameters:
        n (int): start of countdown

    Returns: 
        None
    """
    if n == 0:
        print(n)
        return
    
    print(n)
    countdown(n-1)

countdown(5)