def make_bold(func):
    """
    Decorator: add <strong> tag around string

    Parameters:
        func (function)

    Returns:
        inner (function)
    """

    def inner(first=None, last=None):
        """
        Decorate function. Take arguments, or no arguments

        Parameters:
            first (str)
            last (str)

        Returns:
            (str)
        """
        # if args == None, no args are given
        # means, decorated functions takes no args
        # call func without args
        if first == None and last == None:
            return f"<strong>{func()}</strong>"

        # if args are given, call func with args
        return f"<strong>{func(first, last)}</strong>"

    return inner


def make_italics(func):
    """
    Wrap <em></em> around given args

    Parameters:
        func (function)

    Returns:
        inner (function)
    """

    def inner(first, last):
        return f"<em>{func(first, last)}</em>"

    return inner


def make_paragraph(func):
    """
    Wrap <p></p> around given args

    Paramaters:
        func (function)

    Returns:
        inner (function)
    """

    def inner(first, last):
        return f"<p>{func(first, last)}</p>"

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


@make_bold
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


@make_paragraph
@make_italics
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


print(get_html_greeting())
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
