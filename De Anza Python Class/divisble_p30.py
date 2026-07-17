# divisble_p30.py
# 2//14/26
# Python 3.13.9
# a program where a function returns True if N is evenly divisible by M, and False otherwise.

# function divisible
def is_divisible(N, M):
    if N % M == 0:
        return True
    else:
        return False


# user input
num1 = int(input("Enter N: "))
num2 = int(input("Enter M: "))

# output
print(is_divisible(num1, num2))

'''
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> Python divisble_p30.py
Enter N: 4
Enter M: 4
True
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> Python divisble_p30.py
Enter N: 2
Enter M: 3
False

'''