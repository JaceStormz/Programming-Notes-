# randInt_p24.py
# 2/04/26
# Python 3.13.9
# Program that generates X random integers Num.
import random

# Number of random values
randnum = random.randint(10, 15)

# First number initializes everything
num = random.randint(20, 50)
smallest = largest = total = num

'''
ran with the two print statements only because 
it mess with the output format while generating numbers
'''
print("Generated numbers:")
print(num, end=" ")

# Generate remaining numbers also used "_" as variable i will only use once for the "for" loop
for _ in range(randnum - 1):
    num = random.randint(20, 50)
    print(num, end=" ")
    # smallest to largest calculation
    total += num
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

# Calculate average (rounded to 2 decimals)
average = round(total / randnum, 2)

# outputs result
print(f"\nCount: {randnum}")
print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")
print(f"Sum: {total}")
print(f"Average: {average}")


'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python randInt_p24.py
Generated numbers:
24 40 24 28 25 48 33 21 28 21 49 30 
Count: 12
Smallest number: 21
Largest number: 49
Sum: 371
Average: 30.92

'''