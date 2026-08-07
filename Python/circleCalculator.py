# 08/06/2026
# circleCalculator.py
import math

def circle_calc():
    radius = float(input("what is the radius?: "))

    area = math.pi * math.pow(radius, 2)
    circumference = 2 * math.pi * radius
    diameter = 2 * radius

    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    print(f"Diameter: {diameter}")

circle_calc()