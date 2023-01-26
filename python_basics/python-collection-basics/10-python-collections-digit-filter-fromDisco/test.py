# l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
l33t = ['Car33r', 'DCI']


def digit_filter(l33t):
    new_list = []

    for index in range(len(l33t)):
        print("\nindex of l33t:", index)
        print(f"outer loop -> list-item: {l33t[index]}")

        print(f"Inner loop: characters {l33t[index]}:")
        for char in l33t[index]:
            print(char)
            if char.isdigit():
                break
        else:
            new_list.append(l33t[index])

    return new_list


# print(digit_filter(l33t))


word = "Hel7o"

# set check variable to "True"
check = True
for char in word:
    # prints out every single character
    print("\n", char)
    if char.isdigit():
        # if a character is a number, then set check to "False"
        # because check was defined as "True" outside of the loop
        # it can't be reset to "True" as soon it is set to "False"
        check = False

    # so even the last char "o" in the word "Hel7o" is a real character
    # the check variable is still false
    print(check)
