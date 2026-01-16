# p8.py 
# Gautam Rao
# 1//15/26
# Python 3.13.9
# Program to print a multiplication table for float values  0.1, 0.2 and 0.3.

# Print header
print("%8s %8.1f %8.1f %8.1f" %("", 0.1, 0.2, 0.3))

# First row
print("%8.1f %8.2f %8.2f %8.2f" %(0.1, 0.1 * 0.1, 0.1 * 0.2, 0.1 * 0.3))

# Second row
print("%8.1f %8.2f %8.2f %8.2f" %(0.2, 0.2 * 0.1, 0.2 * 0.2, 0.2 * 0.3))

# Third row
print("%8.1f %8.2f %8.2f %8.2f" %(0.3, 0.3 * 0.1, 0.3 * 0.2, 0.3 * 0.3))

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p8.py
              0.1      0.2      0.3
     0.1     0.01     0.02     0.03
     0.2     0.02     0.04     0.06
     0.3     0.03     0.06     0.09
'''