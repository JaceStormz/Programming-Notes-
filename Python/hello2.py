# Assignment, String Concatination
# Ask user for their name and Remove white space from string 
# and Capitalize user's name
#name = input("what's your name? ").strip().title()
# Say Hello to user
#print(f"Hello, {name} ")
#---------------------------------------------------
#---------------------------------------------------
# Parse/ converting values
'''
x = float(input("What is the value of X? "))
y = float(input("What is the value of Y? "))
z =x / y
print(f"{z:.2f}")
'''
#---------------------------------------------------
#---------------------------------------------------
#Defining Methods
'''
def main():
    name = input("what is your name? ")
    hello(name)
    

def hello(to="World"):
    print("Hello,", to)

main()
'''
#----------------------------------------------------
#Square and Power
'''
def main():
    x= int(input("What is X? "))
    print("X squared is", square(x))

def square(n):
    return n * n # can use ** 2 or pow(n, 2)

main()
'''
#----------------------------------------------------
#----------------------------------------------------
#Conditionals
'''
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("X is greater than Y")
if x == y:
    print("X is equal to Y")
'''
#-----------------------------------------------------
#elif
'''
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("X is greater than Y")
elif x == y:
    print("X is equal to Y")
'''
#------------------------------------------------------
#else
'''
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("X is greater than Y")
else:
    print("X is equal to Y")
'''
#---------------------------------------------------------
# or
'''
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y or x > y:
    print("x is not equal y")
else:
    print("X is equal to y")
'''
#----------------------------------------------------------
# not equal to / equal
'''
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x != y: # ==
    print("x is not equal y")
else:
    print("X is equal to Y")
'''
#---------------------------------------------------------
'''
score = int(input("score: "))

if score >= 90 and score <=100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
'''
#----------------------------------------------------------
#nesting
score = int(input("score: "))

if score >= 90 and score <=100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")