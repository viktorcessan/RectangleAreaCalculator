# Get user input for width, height, and unit
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
unit = input("Enter the unit (e.g., cm, inches): ")

# Calculate the area
area = width * height

# Print the area with the unit
print(f"The area of the rectangle is: {area} {unit}²")
