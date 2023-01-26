import re


def digit_filter(list_thing):
    """
    Delete all Strings that contain digits

    Parameters: 
        list_thing (list): list of strings

    Returns: 
         None
    """
    for word in list_thing:
        if re.search("[0-9]", word):
            list_thing.remove(word)

    # lists are changed globally, so no return needed

    # possible different Solution
    # ____________________________
    # new = []
    # for string in original:
    #     if any(char for char in string if char.isdigit()):
    #         continue
    #     else:
    #         new.append(string)
    # return new

    #    –––––––––––––––––––––––––––>>
    #   |                            |
    # char for char in string if char.isdigit()
    #   |  |                | |               |
    #   |  |    first part  | |  third part   |
    #   |  |________________| |_______________|
    #   |<<_________|

    # the whole line is like this:
    # if any(char for char in string if char.isdigit()):
    #     continue

    # any checks an iterable, but because we are looping ourselfs with loop,
    # any gets only one value at once.
    # the if char.isdigit() returns the True of False for any()


l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
print("\n# l33t: -> before")
print(l33t)

digit_filter(l33t)
print("\n# l33t: -> after")
print(l33t)
