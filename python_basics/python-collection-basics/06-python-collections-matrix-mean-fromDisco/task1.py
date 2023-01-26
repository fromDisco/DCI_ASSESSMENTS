# https://blog.prepscholar.com/how-to-find-the-mean
# i dont get the output in the readme. Mean should be average,
# like in the link above. But in the readme it not even near that value


def mean(two_d_list):
    collection = []

    for single in two_d_list:
        collection.append(sum(single))

    return collection


numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]

print(mean(numbers))
