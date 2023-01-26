def validate_numeric(func):
    """
    Check if any Argument is not int of float
    """

    def inner(*args, **kwargs):
        arg_collect = [*args, *kwargs.values()]

        for val in arg_collect:
            if not isinstance(val, (int, float)):
                kwargs["error"] = "The input arguments must be numeric"

        return func(*args, **kwargs)

    return inner


def debug(func):
    """
    Give information about the Arguments
    """

    def inner(*args, **kwargs):
        output = "**********"

        if len(args) > 0:
            output += f"\nPositional arguments: {', '.join(str(item) for item in args)}"
        else:
            output += "\nThere are no positional arguments."

        if len(kwargs) > 0:
            # if val didn't pass validate_numeric(), kwargs["error"] is present,
            # therefore filter it out
            kwargs_vals = [
                f"{key}={str(val)}" for key, val in kwargs.items() if key != "error"
            ]
            output += f"\nKeyword arguments: {', '.join(kwargs_vals)}"
        else:
            output += "\nThere are no keyword arguments."

        if "error" in kwargs:
            output += f"\nResult: {kwargs['error']}"
        else:
            # if all args are int of float, sum them
            output += f"\nResult: {sum(args) + sum(kwargs.values())}"

        output += "\n**********\n"

        return output

    return inner


@validate_numeric
@debug
def sum_args(a, b):
    """Return the sum of two numbers."""
    return a + b


print(sum_args(1, 2, b=3))
print(sum_args(1, "2"))
print(sum_args(a=1, b="a"))
print(sum_args(1, b=2))
print(sum_args(a=1, b=3.4))
