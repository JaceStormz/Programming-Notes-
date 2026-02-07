# randListgen_p26.py
# Gautam Rao
# 2/04/26
# Python 3.13.9
# A program that generates a random list of letters.

from random import randint
from random import choice

# start with an empty list
empty_list = []

# random length between 50 and 75
length = randint(50, 75)

# possible letters A to F
letters = ["A", "B", "C", "D", "E", "F"]

# generate the list of random letters
for _ in range(length):
    letter = choice(letters)
    empty_list.append(letter)

# count how many times "B" appears (no count())
b_count = 0
for letter in empty_list:
    if letter == "B":
        b_count += 1

# output
print("Generated list of letters:")
print(empty_list)
print(f"Number of times the letter B appears: {b_count}")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python randListletters_p27.py
Generated list of letters:
['A', 'F', 'A', 'A', 'F', 'A', 'C', 'C', 'F', 'E', 'D', 'A', 'E', 'C', 'E', 'F', 'D', 'C', 'F', 'E', 'A', 'A', 'D', 'A', 'A', 'B', 'A', 'C', 'E', 'C', 'A', 'C', 'F', 'C', 'F', 'F', 'A', 'E', 'F', 'F', 'D', 'E', 'F', 'B', 'A', 'E', 'A', 'A', 'B', 'A', 'C', 'D', 'A']
Number of times the letter B appears: 3

'''