# randListgen_p26.py
# Gautam Rao
# 2/04/26
# Python 3.13.9
#  A program that generates a random list of numbers

from random import randint

# Start with an empty list
numbers = []

# Random length between 15 and 20
length = randint(15, 20)

# Generate random numbers between 2 and 5
for _ in range(length):
    numbers.append(randint(2, 5))

# Count how many times 3 appears (without using count())
count_3 = 0
for num in numbers:
    if num == 3:
        count_3 += 1

# Output
print(f"Generated list: {numbers}")
print(f"Number of times 3 appears: {count_3}")


'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> Python randListgen_p26.py                                 
Generated list: [5, 2, 4, 4, 2, 4, 5, 4, 5, 5, 2, 4, 3, 3, 3, 4, 5, 3]
Number of times 3 appears: 4

'''