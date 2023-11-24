# Get user input for width, height, and unit
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
unit = input("Enter the unit (e.g., cm, inches): ")

# Ask the user if they want to calculate area, perimeter, or both
choice = input("Do you want to calculate the Area (A), Perimeter (P), or Both (B)? ")

# Calculate the area
area = width * height

# Calculate the perimeter
perimeter = 2 * (width + height)


# Checks the value of the choice and print the perimeter or both area and perimeter if the user selects both
if choice == 'P' or choice == 'B':
    perimeter = 2 * (width + height)

# Displays results based on the users choice
if choice == 'A':
    print(f"The area of the rectangle is: {area} {unit}²")
elif choice == 'P':
    print(f"The perimeter of the rectangle is: {perimeter} {unit}")
else:
    print(f"The area of the rectangle is: {area} {unit}²")
    print(f"The perimeter of the rectangle is: {perimeter} {unit}")


