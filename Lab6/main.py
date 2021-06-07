def is_perfect_cube(number) -> bool:
    """
    Indicates (with True/False) if the provided number is a perfect cube.
    """
    number = abs(number)  # Prevents errors due to negative numbers
    return round(number ** (1 / 3)) ** 3 == number

def isPerfectCube(number): 
	if round(number ** (1/3)) ** 3 == number:
		return number

# See if each number is a perfect cube and check whether a sum when cubed equals a cube
isSum = True
for i in range(1, 1000):
	is_cube = is_perfect_cube(i)
	isCube = isPerfectCube(i)
	if is_cube:
		print(i, "is a perfect cube!")
		for j in range(1, isCube):
			oneInt = isCube - j
			if (((oneInt ** 3) + (j ** 3)) == isCube):
				print(str(oneInt) + " and " + str(j) + " are sums to " + str(isCube))
			else:
				isSum = False
if not isSum:
	print("There are no two numbers when cubed equal to a cube.")