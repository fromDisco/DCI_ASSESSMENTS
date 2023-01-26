test_data1 = [1,
              [1, 2],
              [1, [2, 3]],
              [1, [2, [3, 4]]],
              [1, [2, [3, [4, 5]]]],
              ]
test_data2 = [
    [1, [[2, 6], [3, 4]]],
    [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    [1, [2, 3]],
    [1, 2],
    1,
]


def drill_sum(num_list):
    """
    Return sum of all integers in nested lists

    Parameters:
        num_list (list): list containing int and nested lists

    Returns:
        collected (int)
    """
    collected = 0

    if type(num_list) == int:
        # if num_list is an integer,
        # just return int and add to collected
        return num_list

    # because loop opens every item (list),
    # everything is covered
    for item in num_list:
        # if item is an integer,
        # it is covered by the base case
        # otherwise the item is looped again
        collected += drill_sum(item)

    return collected


print(drill_sum(test_data1))
print(drill_sum(test_data2))
