import time


def cache(func, cache_obj={}):
    """
    If function is called with the same args as before

    Parameters:
        func (function)
        cache_obj (dict)

    Returns:
        inner (function)
    """

    def inner(*args):
        func_str = f"{str(func)}{args}"

        if func_str in cache_obj:
            print("Using the cache")
        else:
            print("Calculating")
            time.sleep(.8)
            cache_obj.update({func_str: func(*args)})

        return cache_obj[func_str]

    return inner


@cache
def sum_args(a, b):
    """Return the sum of two numbers."""
    return a + b


print(sum_args(1, 2))
print(sum_args(1, 2))
print(sum_args(3, 2))
print(sum_args(3, 2))
print(sum_args(2, 1))
