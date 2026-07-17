# pracMath_p23.py
# 2/04/26
# Python 3.13.9
# Program to let a child practice arithmetic skills.
# import random number
from random import randint

print("Arithmetic Practice Program")
print("Choose an option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
# select the operator
choice = int(input("Enter your choice (1-3): "))

# Keep practicing until the user decides to stop
keep_going = "y"

while keep_going == "y":

    # Generate two random numbers (0–9)
    num1 = randint(0, 9)
    num2 = randint(0, 9)

    # Determine the which operator was selected and asks the question.
    if choice == 1:
        correct_answer = num1 + num2
        question = f"{num1} + {num2} = "
    elif choice == 2:
        correct_answer = num1 - num2
        question = f"{num1} - {num2} = "
    elif choice == 3:
        correct_answer = num1 * num2
        question = f"{num1} * {num2} = "
    else:
        # to make sure user doesn't select incorrect choice 
        print("Invalid choice.")
        break

    # (infinite loop) Ask the same question until answered correctly
    while True:
        # user enters answer
        answer = int(input(question))
        # checks answer and informs user of result
        if answer == correct_answer:
            print("Correct! Great job! ")
            break
        else:
            print("Oops! Try again.")
    # ask to continue
    keep_going = input("Do you want another problem? (y or n): ").lower()

print("Thanks for practicing! ")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python pracMath_p23.py
Arithmetic Practice Program
Choose an option:
1. Addition
2. Subtraction
3. Multiplication
Enter your choice (1-3): 1
6 + 5 = 10
Oops! Try again.
6 + 5 = 11
Correct! Great job! 
Do you want another problem? (y or n): y
8 + 6 = 14
Correct! Great job! 
Do you want another problem? (y or n): n
Thanks for practicing! 

'''