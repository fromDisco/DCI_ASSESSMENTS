def wrap_with(tag):
    """
    Wrap any given tag around given args

    Parameters:
        tag (str)
        func (function)
        first (str)
        last (str)

    Returns:
        inner (function)
    """

    def inner(func):
        def inner_inner(first, last):
            return f"<{tag}>{func(first, last)}</{tag}>"

        return inner_inner

    return inner


@wrap_with(tag="strong")
def get_full_name(first, last):
    """
    Return the full name "first last"

    Arguments:
        first (str)
        last (last)

    Returns:
        (str)
    """
    return f"{first} {last}"


@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    """
    Return a greeting with given args

    Argumens:
        first (str)
        last (str)

    Returns:
        (str)
    """
    return f"Hello, {get_full_name(first, last)}"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
