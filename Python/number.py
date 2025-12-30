"""try:
    x = int(input("What's X?"))
    print(f"x is{x}")
except ValueError:
    print("x is not an integer")"""
# ValueError the value of the x doesn't match the type assigned
# NameError is a code error 
"""try:
    x = int(input("What's X?"))
except ValueError:
    print(f"x is{x}")
else:
    print("x is not an integer")
"""
# ---------------------
"""
while True:
    try:
        x = int(input("What's X?"))
    except ValueError:
        print("x is not an integer")
    else:    
        break

print(f"x is {x}")
"""
# ---------------------------------
"""
while True:
    try:
        x = int(input("What's X?"))
    except ValueError:
        print("x is not an integer")
    else:    
        break

print(f"x is {x}")
"""
#------------------------------
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's X?"))
        except ValueError:
            print("x is not an integer")
main()
"""
# Return is a stronger version of break so break statement is not need so long the return statement is called.
# if you want to handle an execption in python but want to pass on doing anything 
# you want to catch something by want to ignore it not print or exiting the program
# 

def main():
    x = get_int("what's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
# you don't need to ask in the input statement just the it in the method for reusabililty
# then setting the get_int() internally in the prompt 
# raise keyword can raise execptions
# import is a key word that allows you to retrieve codes and functions from a library/module