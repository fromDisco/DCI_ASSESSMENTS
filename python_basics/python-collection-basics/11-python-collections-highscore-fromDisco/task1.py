participants = ['Brian', 'Britney', 'Ben']
scores = {
    'brian': 25,
    'britney': 80,
    'ben': 50
}


def get_score(name, list_item, user_dict):
    """
    Checks if user participated: 
        If True return User and scored Points
        If False return a message, that user didn't participate

    Parameters:
        name (str): string with name to check
        user_dict (dict): participants and their scored points

    Returns:
        string
    """
    if name in list_item:
        return f"{name} scored {user_dict[name.lower()]}"
    else:
        return f"{name} did not participate points"


# i changed added the list and the dictionary to the arguments
# so the function gets a bit more versatile
print(get_score('Paul', participants, scores))
print(get_score('Britney', participants, scores))
