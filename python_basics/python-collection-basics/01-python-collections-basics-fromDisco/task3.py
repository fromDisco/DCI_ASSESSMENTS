colors = ["cyan", "magenta", "green", "yellow", "black", "white"]
print("\n# colors:")
print(colors)

colors.remove("white")
colors.remove("green")

print("\n# colors after:")
for color in colors:
    print(color)
