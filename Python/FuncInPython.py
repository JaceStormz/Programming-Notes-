# FuncInPython.py
# 08/04/2026
"Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. "
"Equation of an area of a triangle is. "


def calculate_area(height,base, shape):
    if shape == "triangle":
        return 0.5 * base * height
    elif shape == "rectangle":
        return base * height
    else:
        return "Invalid shape"

shape = input("What is the shape? ")
height = float((input("what is the height? ")))
base = float((input("what is the base? ")))

Total = calculate_area(height,base, shape)
print(f"The total area: {Total}")