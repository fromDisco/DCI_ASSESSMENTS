import datetime


def isOdd(num):
    """
    Return True if num is odd else False

    Parameters: 
        num (int): to check if is odd

    Returns:
        bool
    """
    return num % 2 != 0


def isEven(num):
    """
    Return True if num is even else False

    Parameters: 
        num (int): to check if is even

    Returns:
        bool
    """
    return num % 2 == 0


print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))


print("\n# Task 2: getParity()")


def getParity(num, testCase):
    """
    Takes testCase, which should be "even" or "odd"
    If testCase is unknown, return "Parity is unknown"

    Parameters:
        num (int): to check for testCase

    Returns:
        (bool) if testCase isnt unknown else (str)
    """
    if testCase != "even" and testCase != "odd":
        return "Parity indicated is unknown"
    elif testCase == "even":
        return True if num % 2 == 0 else False
    else:
        return True if num % 2 != 0 else False


print(getParity(1, "odd"), getParity(1, "even"))
print(getParity(657842, "odd"), getParity(657842, "even"))
print(getParity(0, "odd"), getParity(0, "even"))
print(getParity(-2, 'number'))


print("\n# Task 3: greet()")


def greet(**kwargs):
    """
    Returns a string is a greeting including the actual daytime

    Parameters:
        kwargs["name"] (str): Name of the person, to be greeted
        kwargs["date"] (datetime-object): Time of the day

    Returns:
        str
    """
    print("KWARGS:")
    print(kwargs)

    now = kwargs["date"]
    print("NOW:")
    print(now)
    actual_hour = now.hour

    if actual_hour < 12:
        return f"Good morning, {kwargs['name']}"
    elif 12 <= actual_hour < 18:
        return f"Good afternoon, {kwargs['name']}"
    else:
        return f"Good night, {kwargs['name']}"


print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
))
print(greet(
    date=datetime.datetime(2021, 5, 7, 18, 0, 1),
    name="John"
))


print("\n# Task 4: sumAll()")


def sumAll(lists):
    """
    Returns the sum of all numbers given

    Parameters:
        lists (list): can include 1 or more lists with integers

    Returns:
        collected (int): summed numbers
    """
    collected = 0

    for single_list in lists:
        collected += sum(single_list)

    return collected


test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sumAll(test1))
print(sumAll(test2))


print("\n# Task 5: sumAll()")


def pic_latin(word_list, suffix="ay", single=False):
    """
    Returns list with changed strings

    Parameters:
        word_list (list): list with words

    Returns:
        word_list (list): changed words
    """

    vowels = "aeiouAEIOU"
    print(suffix)
    print(single)

    for index, word in enumerate(word_list):
        if vowels.find(word[0]) != -1:
            word_list[index] += suffix
        else:
            word_list[index] = word_list[index][1:] + \
                word_list[index][0] + suffix

    return word_list


test1_data = ["Word", "Apple"]
test1_config = {}
print(pic_latin(test1_data, **test1_config))


test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}
print(pic_latin(test2_data, **test2_config))

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": "True", "suffix": "ep"}

# test3_config = {"suffix": "ep"}
print(pic_latin(test3_data, **test3_config))
