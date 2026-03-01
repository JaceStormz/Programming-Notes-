# Starfunction_p41.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
# Write a function which outputs as many crosses as the parameter 'numCrosses' indicates.
def stars(numCrosses):
    for row in range(1, numCrosses + 1):   # outer loop (rows)
        for col in range(row):             # inner loop (columns)
            print("+", end=" ")            # print cross on same line
        print()                            # move to next line
stars(5)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python Starfunction_p41.py     
+ 
+ + 
+ + + 
+ + + + 
+ + + + +

'''