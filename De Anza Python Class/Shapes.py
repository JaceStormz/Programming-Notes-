# Shapes.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
'''
Write a program that lets the user enter 4 sides and 4 angles into LISTS.
The program checks if the type of quadrilateral is either: 
- Rhombus
- Square
- Rectangle
'''

def get_positive_input(prompt):
    value = float(input(prompt))
    while value <= 0:
        print("Value must be positive!", end=" ")
        value = float(input(prompt))
    return value


def main():
    repeat = 1

    while repeat == 1:

        # ----------- SIDES -----------
        print("=== Please enter Sides ===")
        sides = []

        for i in range(4):
            prompt = f"Please enter side {i+1}: "
            value = get_positive_input(prompt)
            sides.append(value)

        # ----------- ANGLES -----------
        print("\n=== Please enter Angles ===")
        angles = []

        for i in range(4):
            prompt = f"Please enter angle {i+1}: "
            value = get_positive_input(prompt)
            angles.append(value)

        print("=======================")

        # ----------- CLASSIFICATION -----------

        # Square
        if (all(side == sides[0] for side in sides) and
            all(angle == angles[0] for angle in angles)):
            print("This is a SQUARE!")

        # Rhombus
        elif (all(side == sides[0] for side in sides) and
              angles[0] == angles[2] and
              angles[1] == angles[3]):
            print("This is a RHOMBUS!")

        # Rectangle
        elif (sides[0] == sides[2] and
              sides[1] == sides[3] and
              all(angle == angles[0] for angle in angles)):
            print("This is a RECTANGLE!")

        else:
            print("This quadrilateral is not classified.")

        # ----------- REPEAT -----------
        repeat = int(input("\nWould you like to repeat? (1-Yes, 2-No): "))


if __name__ == "__main__":
    main()

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python Shapes.py
=== Please enter Sides ===
Please enter side 1: -1
Value must be positive! Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: -1
Value must be positive! Please enter side 3: 1
Please enter side 4: 1

=== Please enter Angles ===
Please enter angle 1: -1
Value must be positive! Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: -1
Value must be positive! Please enter angle 3: 90
Please enter angle 4: 90
=======================
This is a SQUARE!

Would you like to repeat? (1-Yes, 2-No): 1
=== Please enter Sides ===
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: 1
Please enter side 4: 1

=== Please enter Angles ===
Please enter angle 1: 120
Please enter angle 2: 60
Please enter angle 3: 120
Please enter angle 4: 60
=======================
This is a RHOMBUS!

Would you like to repeat? (1-Yes, 2-No): 1
=== Please enter Sides ===
Please enter side 1: 10
Please enter side 2: 20
Please enter side 3: 10
Please enter side 4: 20

=== Please enter Angles ===
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: 90
Please enter angle 4: 90
=======================
This is a RECTANGLE!

Would you like to repeat? (1-Yes, 2-No): 2


'''