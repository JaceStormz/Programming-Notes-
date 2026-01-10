# output_P1.py
# Gautam Rao
# 1/06/26
# Python 3.13.9
# Description: Program show's output in Python

print('Hello World!')            # single quote
print("Hello World!")            # double quote
print("he\nllo")                 # \n insert a new line (same as pressing Enter)

# VARIABLES are named storage locations for numbers, strings, lists
# STRING is anything enclosed in quotes "Hello World", that's a string
# NUMBER can be either a FLOAT (Ex: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Alex", "Stoykov"]
myName = "Gautam Rao"               # declare/initialize string variable myName
Weight = 207.5                        # declare/initialize float variable Weight
Age = 37                            # declare/initialize int variable Age
Grades = [93.5,95.5]
Name = ["Gautam", "Rao"]

print ("Hello ", myName)
print ("Your weight is ", Weight, "and your age is ", Age)
print ("Your weight is %.2f and your age is %i" %(Weight, Age))
print ("Lists: grades =",Grades,"nameZ=",Name)
print ("This is how you print", end=' ')
print ("on the same line")


'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python output_P1.py
Hello World!
Hello World!
he
llo
Hello  Gautam Rao
Your weight is  205 and your age is  37
Your weight is 205.00 and your age is 37
Lists: grades = [93.5, 95.5] nameZ= ['Gautam', 'Rao']
This is how you print on the same line

'''
