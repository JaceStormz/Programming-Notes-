# absoluteFunction_p29.py 

# 2//14/26
# Python 3.13.9
# a program that calculates Absolute value with out using the Python function

# manually created absolute value 
def my_absolute_value(number):
    if number < 0:
        return -number
    else:
        return number


# user input
num = float(input("Enter a number: "))
result = my_absolute_value(num)

# output
print(f"Absolute value: {result}")

'''
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python absoluteFunction_p29.py
Enter a number: -12
Absolute value: 12.0
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python absoluteFunction_p29.py
Enter a number: 13
Absolute value: 13.0

'''