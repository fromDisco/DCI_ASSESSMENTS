def make_bold(func):
    """
    Decorator: add <strong> tag around string

    Parameters:
        func (function)

    Returns:
        inner (function)
    """

    def inner():
        return f"<strong>{func()}<strong>"

    return inner


@make_bold
def get_html_greeting():
    """
    Return a string

    Parameters:
        None

    Returns:
        (str)
    """
    return "Hello guys"


print(get_html_greeting())
