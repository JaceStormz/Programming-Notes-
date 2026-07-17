# diceGame_p22.py
# 2/04/26
# Python 3.13.9
# Dice Game program that generates two random dice values between 1 and 6 for you, and 2 for the computer.

# imported function for random int 
from random import randint

print("Beat the computer!\n")

# is an infinite loop till user selects "y". This is for user input
while True:
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    player_total = die1 + die2
    # calculates random generated values for user.
    print(f"You rolled a {die1} and a {die2} (total = {player_total})\n")
    # provide option to quit. sets player input to lower case
    choice = input("Do you want to keep those? (y or n)\n").lower()
    # checks if user wants to continue before allowing the computer to roll
    if choice == "y":
        break
    else:
        print("\nRolling again....\n")

# Computer rolls once, randomly generated values
comp_die1 = randint(1, 6)
comp_die2 = randint(1, 6)
computer_total = comp_die1 + comp_die2
# calculates randomly generated values for computer
print(f"The computer rolled {comp_die1} and {comp_die2} (total = {computer_total})\n")

# Determines the result of the game with appropriate output.
if player_total > computer_total:
    print("Congratulations! You win!")
elif player_total < computer_total:
    print("So sorry. You lose.")
else:
    print("It's a tie!")


'''
-----You wins-------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python diceGame_p22.py
Beat the computer!

Rolling again....

You rolled a 2 and a 1 (total = 3)

Do you want to keep those? (y or n)
n

Rolling again....

You rolled a 6 and a 5 (total = 11)

Do you want to keep those? (y or n)
y
The computer rolled 6 and 4 (total = 10)

Congratulations! You win!

----You lose---------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python diceGame_p22.py
Beat the computer!

You rolled a 1 and a 2 (total = 3)

Do you want to keep those? (y or n)
y
The computer rolled 1 and 6 (total = 7)

So sorry. You lose.

-------Its a tie------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python diceGame_p22.py
Beat the computer!

You rolled a 3 and a 3 (total = 6)

Do you want to keep those? (y or n)
y
The computer rolled 2 and 4 (total = 6)

It's a tie!
'''