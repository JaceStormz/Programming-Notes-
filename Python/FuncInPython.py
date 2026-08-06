# FuncInPython.py
# 08/04/2026
"Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. "
"Equation of an area of a triangle is. "
<<<<<<< HEAD

=======
shape = input("What is the shape? ")
height = float((input("what is the Hieght? ")))
base = float((input("what is the Hieght? ")))
>>>>>>> 40fc2da48b66f20685fc87402aae28ea0b8d23fb

def calculate_area(height,base, shape):
    if shape == "triangle":
        return 0.5 * base * height
    elif shape == "rectangle":
        return base * height
    else:
        return "Invalid shape"

<<<<<<< HEAD
shape = input("What is the shape? ")
height = float((input("what is the height? ")))
base = float((input("what is the base? ")))

=======
>>>>>>> 40fc2da48b66f20685fc87402aae28ea0b8d23fb
Total = calculate_area(height,base, shape)
print(f"The total area: {Total}")