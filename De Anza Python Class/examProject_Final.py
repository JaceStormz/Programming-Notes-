# examProject_Final.py 
# Gautam Rao
# 3/21/26
# Python 3.13.9
'''
You may not use the built-in python functions: sum(), average(), sort(), sorted(), median()
A) Use a loop to make 10 random numbers between 20 and 30, store them in a variable numList  .
( Hint: use numList.append(number), where number is a randomint between 20 and 30 )
B) Sort the list using the bubble sort you learned in this class.
C) Show the sorted list and the unsorted list.
D) Find the sum, and average of the numbers in numList . 
E) Find the median of the list.
( Hint for 10 numbers the median is the average of the two numbers in the middle)
F) Show how many numbers are evenly divisible by 2
G) Copy/paste the Output of your program (A-F) as a multiline comment at the bottom of your program .

'''
import random

# A) Generate 10 random numbers between 20 and 30
numList = []
for i in range(10):
    num = random.randint(20, 30)
    numList.append(num)

# Keep a copy of the original (unsorted list)
unsortedList = []
for x in numList:
    unsortedList.append(x)

# B) Bubble Sort
n = len(numList)
for i in range(n):
    for j in range(0, n - i - 1):
        if numList[j] > numList[j + 1]:
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

# C) Show lists
print(f"Unsorted List: {unsortedList}")
print(f"Sorted List: {numList}")

# D) Find sum and average
total = 0
for num in numList:
    total += num

average = total / len(numList)

print(f"Sum: {total}")
print(f"Average: {average}")

# E) Find median (for 10 numbers: average of middle two)
mid1 = numList[4]
mid2 = numList[5]
median = (mid1 + mid2) / 2

print(f"Median: {median}")

# F) Count numbers divisible by 2
count_even = 0
for num in numList:
    if num % 2 == 0:
        count_even += 1

print(f"Numbers divisible by 2: {count_even}")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python examProject_Final.py
Unsorted List: [24, 28, 27, 21, 23, 26, 29, 21, 23, 30]
Sorted List: [21, 21, 23, 23, 24, 26, 27, 28, 29, 30]
Sum: 252
Average: 25.2
Median: 25.0
Numbers divisible by 2: 4

'''
