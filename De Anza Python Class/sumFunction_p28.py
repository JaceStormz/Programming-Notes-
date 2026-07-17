# sumFunction_p28.py 
# 2//14/26
# Python 3.13.9
# write a programm that takes the sum of two numbers in a function

# function sum which doubles
def sum_or_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b


# User input
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# output
result = sum_or_double(num1, num2)
print(f"Result: {result}")
'''
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python sumFunction_p28.py 
Enter first integer: 3
Enter second integer: 8
Result: 11

PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python sumFunction_p28.py
Enter first integer: 6
Enter second integer: 6
Result: 24

'''