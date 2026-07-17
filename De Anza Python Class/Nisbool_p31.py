# Nisbool_p31.py 
# 2//14/26
# Python 3.13.9
# Write a function that has an integer N as parameter and returns true if N is even.

# function is even number check
def is_even(N):
    if N % 2 == 0:
        return True
    else:
        return False


# user input
num = int(input("Enter an integer: "))

#output
print(is_even(num))

'''
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python Nisbool_p31.py
Enter an integer: 2
True
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python Nisbool_p31.py
Enter an integer: 3
False

'''