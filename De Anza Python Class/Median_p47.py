# Median_p47.py 
# 3/07/26
# Python 3.13.9
'''
Write a program which :

    Writes a random number (50 to 55) of numbers (0 to 100) in a file
    Opens the file and reads the numbers from it into a list
    Sorts the list and Shows it.
    Calculates the median.

Note: You may NOT use the Python built in functions: sort(), sorted(), sum(), median()

'''

import random

file_name = "numbers.txt"

# Write random numbers to file
with open(file_name, "w") as f:
    for _ in range(random.randint(50, 55)):
        f.write(f"{random.randint(0,100)}\n")

# Read numbers into list
with open(file_name) as f:
    numbers = [int(line.strip()) for line in f]

# Selection sort
for i in range(len(numbers)):
    min_i = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_i]:
            min_i = j
    numbers[i], numbers[min_i] = numbers[min_i], numbers[i]

print("Sorted list:")
print(numbers)

# Median calculation
n = len(numbers)

if n % 2:
    median = numbers[n // 2]
else:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2

print("Median:", median)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python Median_p47.py
Sorted list:
[1, 1, 2, 5, 7, 8, 11, 12, 14, 15, 16, 23, 25, 27, 31, 33, 34, 36, 45, 46, 46, 48, 54, 55, 59, 59, 59, 60, 62, 69, 70, 70, 71, 73, 76, 80, 81, 83, 83, 84, 84, 85, 85, 86, 87, 87, 87, 91, 94, 94, 94, 97, 99]
Median: 59

'''