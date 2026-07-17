# Xnumber_p40.py 
# 2/21/26
# Python 3.13.9
# Ask the user to enter X numbers into a list. Calculate and show the sum, average, min, max of those numbers.

# Ask how many numbers
count = int(input("How many numbers would you like to enter? "))

numbers = []

# Collect numbers
for i in range(1, count + 1):
    numbers.append(int(input(f"Enter number {i:2}: ")))

# Print list cleanly
print(f"List:  [ {', '.join(str(n) for n in numbers)} ]")

# Initialize values
total = 0
smallest = largest = numbers[0]

# Single clean loop
for num in numbers:
    total += num
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

average = total / count

# Output
print(f"Sum = {total}")
print(f"Average = {total} / {count} = {average:.1f}")
print(f"Smallest = {smallest}")
print(f"Largest = {largest}")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python Xnumber_p40.py
How many numbers would you like to enter? 11
Enter number  1: 26
Enter number  2: 23
Enter number  3: 48
Enter number  4: 32
Enter number  5: 44
Enter number  6: 21
Enter number  7: 32
Enter number  8: 20
Enter number  9: 49
Enter number 10: 48
Enter number 11: 34
List:  [ 26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34 ]
Sum = 377
Average = 377 / 11 = 34.3
Smallest = 20
Largest = 49

'''