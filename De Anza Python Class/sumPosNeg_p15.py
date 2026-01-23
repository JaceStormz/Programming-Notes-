# sumPosNeg_p15.py 
# Gautam Rao
# 1//23/26
# Python 3.13.9
# Sum of Numbers Program

# define variables
sumNeg = 0
sumPos = 0

#input
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))

# Check each number
if num1 < 0:
    sumNeg = sumNeg + num1
elif num1 > 0:
    sumPos = sumPos + num1

if num2 < 0:
    sumNeg = sumNeg + num2
elif num2 > 0:
    sumPos = sumPos + num2

if num3 < 0:
    sumNeg = sumNeg + num3
elif num3 > 0:
    sumPos = sumPos + num3

if num4 < 0:
    sumNeg = sumNeg + num4
elif num4 > 0:
    sumPos = sumPos + num4

sumAll = sumNeg + sumPos

#output
print("Sum of all numbers:", sumAll)
print("Sum of positive numbers:", sumPos)
print("Sum of negative numbers:", sumNeg)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python sumPosNeg_p15.py
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python sumPosNeg_p15.py
Enter number 1: 3
Enter number 2: 35
Enter number 3: -90
Enter number 4: -786
Sum of all numbers: -838.0
Sum of positive numbers: 38.0
Sum of negative numbers: -876.0
------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python sumPosNeg_p15.py
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python sumPosNeg_p15.py
Enter number 1: 0  
Enter number 2: 578
Enter number 3: -398
Enter number 4: -22
Sum of all numbers: 158.0
Sum of positive numbers: 578.0
Sum of negative numbers: -420.0

'''