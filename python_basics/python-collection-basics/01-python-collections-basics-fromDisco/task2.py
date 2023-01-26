cities = ["London", "Paris", "Berlin", "Amsterdam"]

berlin0 = cities[2][0]
berlin1 = cities[3][4]
berlin2 = cities[1][2]
berlin3 = cities[2][3]
berlin4 = cities[1][3]
berlin5 = cities[0][2]

collect = ""
collect = f"{berlin0}{berlin1}{berlin2}{berlin3}{berlin4}{berlin5}"

# for i in range(6):
#     # I KNOW: its too complicated, but was fun to test
#     collect += eval("berlin" + str(i))

string = f"\nThe capital city of Germany is: {collect}"
print(string)
