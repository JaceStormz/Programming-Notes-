# tuition_p17.py
# Gautam Rao
# 1//23/26
# Python 3.13.9
# Program that computes the tuition in ten years and displays a table of the years and tuition costs.

# variable definied
tuition = 10000
rate = 0.05
year = 1

# print template for header
print("Year    Tuition")
print("----------------")

# to check if year is less than and equal to ten to execute
while year <= 10:
    # calculate tuition plus yearly interest rate
    tuition = tuition + (tuition * rate)
    # output of year total tuition with .2f is round to 2 decimal points and output 
    print(f"{year:<4} $ {tuition:.2f}")
    year += 1

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python tuition_p17.py                                     
Year    Tuition
----------------
1    $ 10500.00
2    $ 11025.00
3    $ 11576.25
4    $ 12155.06
5    $ 12762.82
6    $ 13400.96
7    $ 14071.00
8    $ 14774.55
9    $ 15513.28
10   $ 16288.95

'''