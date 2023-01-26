dict1 = {
    'a': 4,
    'b': 16,
    'c': 3
}

dict2 = {
    'a': 8,
    'b': 2,
    'c': 3
}

collection = 0

for key in dict1:
    collection += dict1[key] * dict2[key]

print("\n# collection")
print(collection)
