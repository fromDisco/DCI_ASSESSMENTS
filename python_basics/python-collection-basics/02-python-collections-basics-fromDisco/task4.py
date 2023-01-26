animals = {"Alligator": 19, "Tiger": 8,
           "Parrot": 38, "Hamster": 89, "Dolphin": 77}

keys = []
for animal in animals:
    if animal[-1] == "r":
        keys.append(animal)
        # animals.pop(animal) -> doesn't work, change dict size

for key in keys:
    animals.pop(key)

print(animals)
