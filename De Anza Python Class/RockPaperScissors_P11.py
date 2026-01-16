# p11.py 
# Gautam Rao
# 1//15/26
# Python 3.13.9
# program to simulate rock-paper-scissors game.

# Get input from players
print("Enter Rock(1), Paper(2) or Scissors(3)")
player1 = int(input("Player 1: "))
player2 = int(input("Player 2: ")) 

# Determine result 
if player1 == player2:
    print("Tie!")
elif (player1 == 2 and player2 == 1): 
    print("Result: Player 1 wins, Paper covers Rock!")
elif (player1 == 1 and player2 == 3): 
    print("Result: Player 1 wins, Rock breaks Scissors!")
elif (player1 == 3 and player2 == 2): 
    print("Result: Player 1 wins, Scissors cuts Paper!")
elif (player1 == 1 and player2 == 2):
    print("Result: Player 2 wins, Paper covers Rock!")
elif (player1 == 3 and player2 == 1):
    print("Result: Player 2 wins, Rock breaks Scissors!")
elif (player1 == 2 and player2 == 3):
    print("Result: Player 2 wins, Scissors cuts Paper!")


'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p11.py
Enter Rock(1), Paper(2) or Scissors(3)
Player 1: 1
Player 2: 3
Result: Player 1 wins, Rock breaks Scissors!
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p11.py
Enter Rock(1), Paper(2) or Scissors(3)
Player 1: 3
Player 2: 2
Result: Player 1 wins, Scissors cuts Paper!
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p11.py
Enter Rock(1), Paper(2) or Scissors(3)
Player 1: 2
Player 2: 1
Result: Player 1 wins, Paper covers Rock!
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p11.py
Enter Rock(1), Paper(2) or Scissors(3)
Player 1: 3
Player 2: 3
Tie!

'''