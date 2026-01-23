# centconvert_p13.py 
# Gautam Rao
# 1//23/26
# Python 3.13.9
# Write a program to convert any given number of total cents

#user input
cents = int(input("Enter total cents (under 100): "))

#converting cents to quarters, dimes, nickels, pennies
quarters = int(cents / 25)
cents = cents % 25

dimes = int(cents / 10)
cents = cents % 10

nickels = int(cents / 5)
cents = cents % 5

pennies = cents

#output
print("Quarters:", quarters, "x 25c =", quarters * 25, "cents total")
print("Dimes:", dimes, "x 10c =", dimes * 10, "cents total")
print("Nickels:", nickels, "x 5c =", nickels * 5, "cents total")
print("Pennies:", pennies, "x 1c =", pennies * 1, "cents total")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python centconvert_p13.py
Enter total cents (under 100): 66
Quarters: 2 x 25c = 50 cents total
Dimes: 1 x 10c = 10 cents total
Nickels: 1 x 5c = 5 cents total
Pennies: 1 x 1c = 1 cents total
------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python centconvert_p13.py
Enter total cents (under 100): 16
Quarters: 0 x 25c = 0 cents total
Dimes: 1 x 10c = 10 cents total
Nickels: 1 x 5c = 5 cents total
Pennies: 1 x 1c = 1 cents total
------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python centconvert_p13.py
Enter total cents (under 100): 6
Quarters: 0 x 25c = 0 cents total
Dimes: 0 x 10c = 0 cents total
Nickels: 1 x 5c = 5 cents total
Pennies: 1 x 1c = 1 cents total
------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python centconvert_p13.py
Enter total cents (under 100): 4
Quarters: 0 x 25c = 0 cents total
Dimes: 0 x 10c = 0 cents total
Nickels: 0 x 5c = 0 cents total
Pennies: 4 x 1c = 4 cents total

'''