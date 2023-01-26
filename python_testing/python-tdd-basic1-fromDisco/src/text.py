# function will convert string parameter to upper case
def to_upper(string):
    if type(string) != str:
        raise TypeError("Sorry, TypeError")
    return string.upper()


# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    if type(str_list) != list:
        raise TypeError("Please provide list")

    for word in str_list:
        if word.islower():
            return False
    return True


print(to_upper("abcd"))
