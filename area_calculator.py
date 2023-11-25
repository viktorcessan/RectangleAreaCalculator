import math

print("Calculate area, and/or perimeter of triangles, circles, and rectangles.")

# Ask the user what they want to measure
shape_choice = input("What shape are you measuring? A circle (C), rectangle (R), or triangle (T)? ")

# Define variables for both shapes
radius_circle = width_rectangle = height_rectangle = base_triangle = height_triangle = hypotenuse_triangle = 0.0
unit_circle = unit_rectangle = unit_triangle = ""

# Conditional prompt for dimensions (width, height, base, hypotenuse, radius) based on the choice of shape
if shape_choice == 'R':
    width_rectangle = float(input("Enter the width of the rectangle: "))
    height_rectangle = float(input("Enter the height of the rectangle: "))
    unit_rectangle = input("Enter the unit (e.g., cm, inches): ")

elif shape_choice == 'T':
    base_triangle = float(input("Enter the base of the triangle: "))
    height_triangle = float(input("Enter the height of the triangle: "))
    hypotenuse_triangle = float(input("Enter the hypotenuse of the triangle: "))
    unit_triangle = input("Enter the unit (e.g., cm, inches): ")

elif shape_choice == 'C':
    radius_circle = float(input("Enter the radius of the circle: "))
    unit_circle = input("Enter the unit (e.g., cm, inches): ")

# Ask the user if they want to calculate area, perimeter, or both
calc_choice = input("Do you want to calculate the Area (A), Perimeter (P), or Both (B)? ")

# Calculate the area or perimeter of the shapes
area_circle = math.pi * (radius_circle ** 2)
perimeter_circle = 2 * math.pi * radius_circle
area_rectangle = width_rectangle * height_rectangle
perimeter_rectangle= 2 * (width_rectangle + height_rectangle)
area_triangle = 0.5 * base_triangle * height_triangle
perimeter_triangle = base_triangle + height_triangle + hypotenuse_triangle

# Calculate area or perimeter based on shape
if calc_choice == 'A':
    if shape_choice == 'R':
        print(f"The area of the rectangle is: {area_rectangle} {unit_rectangle}²")
    elif shape_choice == 'T':
        print(f"The area of the triangle is: {area_triangle} {unit_triangle}")
    elif shape_choice == 'C':
        print(f"The area of the triangle is {area_circle} {unit_circle}")
elif calc_choice == 'P':
    if shape_choice == 'R':
        print(f"The perimeter of the rectangle is: {perimeter_rectangle} {unit_rectangle}")
    elif shape_choice == 'T':
        print(f"The perimeter of the triangle is: {perimeter_triangle} {unit_triangle}")
    elif shape_choice == 'C':
        print(f"The perimeter of the triangle is: {perimeter_circle} {unit_circle}")

else:
    if shape_choice == 'R':
        print(f"The area of the rectangle is: {area_rectangle} {unit_rectangle}²")
        print(f"The perimeter of the rectangle is: {perimeter_rectangle} {unit_rectangle}")
    if shape_choice == 'T':
        print(f"The area of the triangle is: {area_triangle} {unit_triangle}²")
        print(f"The perimeter of the triangle is: {perimeter_triangle} {unit_triangle}")
    if shape_choice == 'C':
        print(f"The area of the circle is: {area_circle} {unit_circle}")
        print(f"The perimeter of the circle is: {perimeter_circle} {unit_circle}")