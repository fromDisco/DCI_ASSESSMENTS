list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]


def intersection(list_1, list_2):
    """
    Returns the common elements of list_1 and list_2

    Parameters:
        list_1 (list)
        list_2 (list)

    Returns:
        in_common (list): common elements of both lists
    """
    in_common = set(list_1).intersection(set(list_2))

    return list(in_common)


print(intersection(list_1, list_2))
