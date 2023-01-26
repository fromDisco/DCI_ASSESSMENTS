def swap(container, val1, val2):
    """
    Swap value of two given indices

    Parameters:
        container (list): list which should be changed
        val1 (int): first item to swap
        val2 (int): second item so swap

    Returns: 
        None
    """
    container[val1], container[val2] = container[val2], container[val1]


swap_list = [23, 65, 19, 90]
print("\n# swap_list: before")
print(swap_list)

swap(swap_list, 1, 3)

print("\n# swap_list: after")
print(swap_list)
