import math
sides = int(input("number of sides: "))
length = int(input("length of a side: "))
area = (sides * length**2) / (4 * math.tan(math.pi / sides))
print("area is: ", area)
