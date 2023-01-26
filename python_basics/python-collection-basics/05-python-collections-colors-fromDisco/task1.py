color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000', '#00FF00', '#0000FF']


colors = {}
for i in range(len(color_names)):
    colors[color_names[i]] = color_hex[i]


print("\n# colors (dict):")
print(colors)

print("\n# colors['blue']:")
print(colors['blue'])
