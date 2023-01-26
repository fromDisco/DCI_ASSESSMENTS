bart = {"name": "Bart Simpson"}
homer = {"name": "Homer Simpson"}
address = {"address": "742 Evergreen Terrace"}

bart.update(address)
homer.update(address)  # ups, forgot that.

print("\n# bart['address']:")
print(bart["address"])

print("\n# homer['address']:")
print(homer["address"])
