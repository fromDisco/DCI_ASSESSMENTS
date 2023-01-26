def count_character(string):
    """
    Count chars and create dict with char as key 
    and count as value

    Parameters: 
        string (str): string to count

    Returns: 
        char_dict (dict): dict with counted chars
    """
    # set can only contain one of a kind
    char_set = set([*string.lower()])
    char_dict = {}

    for char in char_set:
        char_dict[char] = string.lower().count(char)

    return char_dict


give_string = "Elephant"
print(count_character(give_string))
