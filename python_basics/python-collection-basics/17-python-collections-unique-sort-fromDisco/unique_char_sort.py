strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']


def unique_char_sort(words):
    """
    Count unique chars of words in list, 
    and sort them from less unique chars
    to more unique chars

    Parameters:
        words (list): list of words to compare

    Returns:
        sorted (list)
    """
    word_dict = {}

    for word in words:
        word_dict.update({word: 0})

        for char in word:
            if word.count(char) == 1:
                word_dict[word] += 1

    # 1. loop through sorted(word_dict...)
    # 2. but at first sorted sorts the elements
    # (values el[0]==key, el[1]==value) by value
    # 3. only use the word from for word, num in sorted()
    return [word for word, num in sorted(word_dict.items(), key=lambda el: el[1])]


print(unique_char_sort(strings))
