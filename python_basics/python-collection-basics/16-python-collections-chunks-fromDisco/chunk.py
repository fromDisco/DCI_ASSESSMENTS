data = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4,
    'key5': 5,
    'key6': 6,
}


def chunk(data, size):
    """
    Convert a dictionary into a list with chunks of dictionaries in the given size

    Parameters: 
        data (dict): to be chunked
        size (int): size of chunks

    Returns:
        chunklist (list): list with dictionaries in given size
    """
    chunklist = []
    dict_chunks = {}
    counter = 0

    for item in data.items():
        dict_chunks.update([item])
        counter += 1

        if counter >= size:
            # here i experienced some weird behaviour
            # i can understand what causes it, but the
            # output was strange nevertheless

            # there are two lines, the original, and an alternative
            # this appends a dict to the list
            # printing "chunklist" right after this line gave the correct results
            # then, i clear the "dict_chunks"
            # printing "chunklist" now showed, that it only contained empty dicts
            # thats ok, because, the dict and not only the data of it was stored in the list

            # the weird thing was, that in a new loop, the first print of "chunklist"
            # showed again, the correct dictionaries in the list. Even those,
            # who have been added in previous loops. But again, after clearing "dict_chunks"
            # "chunklist" was empty again
            # ---> so i appended a copy of "dict_chunks"
            # or another solution:
            # instead of dict_chunks.clear() -> dict_chunks = {}
            # creates a new dict and discards the old one

            ##########################################
            chunklist.append(dict_chunks)  # original

            # chunklist.append(dict_chunks.copy()) # alternative
            # print("# chunklist: before clearing dict_chunks")
            # print(chunklist)
            # dict_chunks.clear()

            dict_chunks = {}
            counter = 0

            # print("# chunklist: after clearing dict_chunks")
            # print(chunklist)

    return chunklist


print(chunk(data, 2))
