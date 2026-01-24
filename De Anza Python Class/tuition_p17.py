# tuition_p17.py
# Gautam Rao
# 1//23/26
# Python 3.13.9
# Program that computes the tuition in ten years and displays a table of the years and tuition costs.

tuition = 10000
rate = 0.05
year = 1

print("Year    Tuition")
print("----------------")

while year <= 10:
    tuition = tuition + (tuition * rate)
    print(year, "   $", round(tuition, 2))
    year += 1

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python tuition_p17.py                                                                                                
Year    Tuition
----------------
1    $ 10500.0
2    $ 11025.0
3    $ 11576.25
4    $ 12155.06
5    $ 12762.82
6    $ 13400.96
7    $ 14071.0
8    $ 14774.55
9    $ 15513.28
10   $ 16288.95

'''