# import re


def convert_to_snake(dictionary):
    """
    Convert dict keys to snake case

    Parameters:
        dictionary (dict)

    Returns:
        dictionary (dict): updated keys
    """
    # keys cant be changed while looping the dict
    # so create another dict with new_name and key (old name)
    substitutes = {}
    for key in dictionary:
        # regex is nice but can be much slower
        # https://stackoverflow.com/questions/11258511/python-why-regular-expression-is-slower-than-replace-method
        # new_name = re.sub(" ", "_", key).lower()

        new_key = key.replace(" ", "_").lower()
        substitutes[new_key] = dictionary[key]

    return substitutes


natural_case1 = {
    'Company name': 'Digital Career Institute',
    'Street': 'Vulkanstraße',
    'House Number': 1,
    'City': 'Berlin'
}


natural_case2 = {
    'Movie name': 'James Bond 007: Skyfall',
    'Director': 'Sam Mendes',
    'Production Year': 2012,
    'Duration in minutes': 143,
    'Production countries': ['US', 'UK']
}

print("# convert natural_case1:")
natural_case1 = convert_to_snake(natural_case1)
print(natural_case1)

print("# convert natural_case2:")
natural_case2 = convert_to_snake(natural_case2)
print(natural_case2)
