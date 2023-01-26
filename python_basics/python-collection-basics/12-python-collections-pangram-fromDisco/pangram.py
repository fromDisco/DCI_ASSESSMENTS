import string

# create lowercase letter constant
LOWERCASE = string.ascii_lowercase

string_0 = 'Waltz, bad nymph, for quick jigs vex.'
string_1 = 'Glib jocks quiz nymph to vex dwarf.'
string_2 = 'Sphinx of black quartz, judge my vow.'
string_3 = 'How vexingly quick daft zebras jump!'
string_4 = 'The five boxing wizards jump quickly.'
string_5 = 'Jackdaws love my big sphinx of quartz.'
string_6 = 'Pack my box with five dozen liquor jugs.'

# wrong sentence
string_7 = 'How vexingly quick daft rebras jump!'


def is_pangram(to_check, abc):
    print(f"\n# {to_check}")
    for char in abc:
        if char not in to_check.lower():
            # if one char is not included in the string
            # its not a pangram
            return False

    return True


def is_pangram2(to_check, abc):
    set_of_arg = set(to_check.lower())
    set_of_abc = set(abc)
    in_common = set_of_arg.intersection(set_of_abc)

    return in_common == set_of_abc


# for i in range(8):
#     print(is_pangram(eval("string_" + str(i)), LOWERCASE))

for i in range(8):
    print(is_pangram2(eval("string_" + str(i)), LOWERCASE))
