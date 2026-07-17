# isTriangle_p33.py 
# 2//14/26
# Python 3.13.9
# Write a function named isTriangle(a,b,c) that has three sides a,b,c  as parameters.

# function to check any one side is greater than the sum of the other two sides and return true or false 
def isTriangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        return False
    else:
        return True


# User input
side1 = float(input("Enter side a: "))
side2 = float(input("Enter side b: "))
side3 = float(input("Enter side c: "))

# output 
print(isTriangle(side1, side2, side3))


'''
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python isTriangle_p33.py
Enter side a: 10
Enter side b: 10
Enter side c: 10
True
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python isTriangle_p33.py
Enter side a: 23
Enter side b: 2
Enter side c: 2
False

'''