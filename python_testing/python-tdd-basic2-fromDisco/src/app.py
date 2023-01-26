from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end + 1)


# function should return the greatest number in a list
def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
