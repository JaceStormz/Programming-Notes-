# Lab2.py
# Gautam Rao
# 04/18/2026
# Python 3.13.9
'''
Write a program that plays a guess the number game with the user.
- The program asks the user for a range of numbers, and then it randomly chooses a target number within the range.
- Then the program keeps asking the user to guess the target number until the user gets the correct number.
- For each guess, the program prints "guess higher" if the guess is below target number, or "guess lower" if the guess
is above the target number.
- When the user guesses the correct number, the program prints the number of tries it took.

Requirements
• The program must have at least four functions, but you can add additional ones as you see fit.
• A getRange function:
• Ask the user to set the lower and upper ends of the range
• The lowest number possible is 1. If below 1, keep prompting the user until there is an acceptable number
• The highest possible number is 500. If above 500, keep prompting the user until there is an acceptable number.
• The user cannot enter a high number equal to or below the low number.
• A getGuess function:
• Ask the user for a guess. Prompt should include the range for user to enter between (i.e. "Guess a number
between 1 and 80, inclusive")
• Keep prompting the user until you get a number in the right range.
• A playOneGame function:
• Generate the target number, which is a random number within the user specified range.
• Keep calling getGuess to ask the user to guess, until the guess is correct.
• With the first guess, tell the user whether they're correct or not correct.
• With subsequent guesses, tell the user whether the guess should be higher or lower.
• When the user guesses correctly, print the number of tries it took.
• A main function:
• Ask the user if they want to play guess the number and let the user answer 'y' or 'n'
• If the answer is anything other than 'y', end the program.
• Otherwise, call the getRange function and then call the playOneGame function.
• When one game is done, ask the user whether to continue or to end the game. To continue, loop back for
another game.

Additional requirements
• Comment with your name and short description of the program at the top.
• Comment and explain above all functions what each function does (briefly, should be 2 lines or less) except main
• There should be at least 4 functions and each function should work as described above.
• No recursive functions

'''
import random

# Gets a valid integer from the user (digits only)
# Re-prompts until the user enters a valid number string
def getInt(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a number.")


# Gets a valid range (low and high) within constraints
# Ensures low >= 1, high <= 500, and high > low
def getRange():
    while True:
        low = getInt("Enter the LOW end of the range (>= 1): ")
        if low < 1:
            print("Low must be at least 1.")
            continue

        high = getInt("Enter the HIGH end of the range (<= 500): ")
        if high > 500:
            print("High must be at most 500.")
            continue

        if high <= low:
            print("High must be greater than low.")
            continue

        return low, high


# Gets a valid guess within the given range
# Keeps asking until the guess is between low and high
def getGuess(low, high):
    while True:
        guess = getInt(f"Guess a number between {low} and {high}, inclusive: ")
        if low <= guess <= high:
            return guess
        else:
            print("Guess out of range.")


# Plays one full game of guessing
# Keeps asking until the correct number is guessed and counts tries
def playOneGame(low, high):
    target = random.randint(low, high)
    tries = 0

    # First guess
    guess = getGuess(low, high)
    tries += 1

    if guess == target:
        print(f"Correct! You got it in {tries} try.")
        return
    elif guess < target:
        print("Guess higher.")
    else:
        print("Guess lower.")

    # Remaining guesses
    while guess != target:
        guess = getGuess(low, high)
        tries += 1

        if guess < target:
            print("Guess higher.")
        elif guess > target:
            print("Guess lower.")
        else:
            print(f"Correct! You got it in {tries} tries.")


def main():
    while True:
        play = input("Do you want to play Guess the Number? (y/n): ").lower()

        if play != 'y':
            print("Goodbye!")
            break

        low, high = getRange()
        playOneGame(low, high)

        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# Start the program
main()

# Example runs and output
"""
First Run 

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python lab2.py
Do you want to play Guess the Number? (y/n): y
Enter the LOW end of the range (>= 1): 50
Enter the HIGH end of the range (<= 500): 100
Guess a number between 50 and 100, inclusive: 55
Guess higher.
Guess a number between 50 and 100, inclusive: 58
Guess lower.
Guess a number between 50 and 100, inclusive: 57
Correct! You got it in 3 tries.
Do you want to play again? (y/n): y
Do you want to play Guess the Number? (y/n): y
Enter the LOW end of the range (>= 1): 1
Enter the HIGH end of the range (<= 500): 500
Guess a number between 1 and 500, inclusive: 250
Guess lower.
Guess a number between 1 and 500, inclusive: 200
Guess lower.
Guess a number between 1 and 500, inclusive: 150
Guess lower.
Guess a number between 1 and 500, inclusive: 100
Guess lower.
Guess a number between 1 and 500, inclusive: 50
Guess lower.
Guess a number between 1 and 500, inclusive: 25
Guess higher.
Guess a number between 1 and 500, inclusive: 30
Guess higher.
Guess a number between 1 and 500, inclusive: 35
Correct! You got it in 8 tries.
Do you want to play again? (y/n): n
Thanks for playing!

Second Run

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python lab2.py
Do you want to play Guess the Number? (y/n): y
Enter the LOW end of the range (>= 1): 1
Enter the HIGH end of the range (<= 500): 500
Guess a number between 1 and 500, inclusive: 250
Guess lower.
Guess a number between 1 and 500, inclusive: 200
Guess lower.
Guess a number between 1 and 500, inclusive: .
Invalid input. Please enter a number.
Guess a number between 1 and 500, inclusive: 150
Guess higher.
Guess a number between 1 and 500, inclusive: 170
Guess higher.
Guess a number between 1 and 500, inclusive: 180
Guess higher.
Guess a number between 1 and 500, inclusive: 190
Guess higher.
Guess a number between 1 and 500, inclusive: 195
Guess lower.
Guess a number between 1 and 500, inclusive: 194
Guess lower.
Guess a number between 1 and 500, inclusive: 193
Correct! You got it in 9 tries.
Do you want to play again? (y/n): n
Thanks for playing!
"""