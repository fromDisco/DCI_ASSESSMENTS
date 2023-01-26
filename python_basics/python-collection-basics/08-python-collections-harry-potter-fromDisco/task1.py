
books = {
    'Harry Potter And The Sorcerer\'s Stone': 1241100000,
    'Harry Potter And The Chamber Of Secrets': 771300000,
    'Harry Potter And The Prisoner Of Azkaban': 65210000,
    'Harry Potter And The Goblet Of Fire': 645600000,
    'Harry Potter And The Order Of The Phoenix': 635600000,
    'Harry Potter And The Half Blood Prince': 661300000,
    'Harry Potter And The Deathly Hallows ': 652200000,
}


def top3(book_dict):
    """
    Return top 3 valueable items

    Parameters:
        book_dict (dict): dict with titles and values

    Returns:
        top3_books (str): contains a f-string with top3_books
    """
    output = ""
    counter = 1

    for title, value in book_dict.items():
        output += f"{counter}. {title}, {value}\n"
        counter += 1
        if counter >= 4:
            break

    return output


# what is top 3?
# is it really simple like this?
# at first i misunderstood, because i thought
# that the highest 3 values should decide
# about the top 3
print(top3(books))
