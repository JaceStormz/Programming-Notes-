# Lab1.py

# 04/13/2026
# Python 3.13.9
'''
Part 1:
Write a python program that consists of the following steps:
- Create a constant named MAX and set it to 40.
- Prompt and read in the user’s name. The user can enter their name in any combination of upper and lower case.
- Ask the user for the number of previous programming classes they’ve taken, and read in the data as a number (what
data type should it be?)
- Ask the user for their goal when taking the CIS 41A class. The user can enter upper or lower case letters.
- Print a blank line
- Print the user’s name in a box, with the following format:
	 A line of MAX number of asterisks (*). Don’t hard code 40 here, when I run your code I could change MAX to
	 a different value and the code should still print MAX number of asterisks.
 	 A line with * at the beginning and end, and an appropriate number of spaces in between.
 	 A line with * at the beginning and end, and the user’s name centered within the 2 *’s.
	 The user’s first and last names should have the first letter in uppercase, and all other letters in lowercase.
 	 A line with * at the beginning and end, and an appropriate number of spaces in between.
 	 A line of MAX number of *’s

- Print the number of previous programming classes that the user has taken, with explanation text.
- Print a header line of text, then print the user’s goal for taking CIS 41A on a second line. The user’s goal should be in
all uppercase.
Your program should not have to use any if statement or loop or relational operators (<, >=, etc.)

Part 2:
Run your program, enter your name, the number of programming classes that you’ve taken before this CIS 41A class,
and your goal in taking this class. I’d like to get to know you better.

Part 3:
Run your program again, this time enter your name with one less character or one more character. You can either delete
the space between your first and last names, or add an extra space in between them. This is a test to see that your code
can print both an even and odd length for the name in the center of the box. When the name cannot be exactly in the
center, either one character off in front or in back is fine.
Don’t forget that you can’t use if statement or relational operators to compare. Instead, use arithmetic to
calculate how many spaces to print before and after the name.

'''


# Constant
MAX = 40

# Input
name = input("Enter your name: ")
previousNumberClasses = int(input("Enter number of previous programming classes: "))
goal = input("Enter your goal for CIS 41A: ")

# Format strings
formattedName = name.title()
goalUpper = goal.upper()

# Box components
border = "*" * MAX
emptyLine = "*" + " " * (MAX - 2) + "*"
nameLine = "*" + formattedName.center(MAX - 2) + "*"

# Output
print()
print(border)
print(emptyLine)
print(nameLine)
print(emptyLine)
print(border)

print()
print(f"You have taken {previousNumberClasses} programming class(es) before CIS 41A.")

print("\nYOUR GOAL FOR CIS 41A:")
print(goalUpper)

"""
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python lab1.py                                                                                                                         
Enter your name: Gautam Rao
Enter number of previous programming classes: 3
Enter your goal for CIS 41A: Practicing Pythonic Coding     

****************************************
*                                      *
*              Gautam Rao              *
*                                      *
****************************************

You have taken 3 programming class(es) before CIS 41A.

YOUR GOAL FOR CIS 41A:
PRACTICING PYTHONIC CODING 

"""