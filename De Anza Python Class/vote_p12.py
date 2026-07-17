# vote_p12.py 
# 1//23/26
# Python 3.13.9
# This program checks checks if the user can vote.

#user input
age = int(input("Please enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()
registered = input("Are you registered to vote? (yes/no): ").lower()

# age citizen and is registered check and output
if age >= 18 and citizen == "yes" and registered == "yes":
    print("Great, you may vote!")
else:
    print("You may not vote because:")

    if age < 18:
        print("you are not old enough")
    if citizen != "yes":
        print("you are not a citizen")
    if registered != "yes":
        print("you are not registered to vote")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python vote_p12.py
Please enter your age: 20
Are you a citizen? (yes/no): yes
Are you registered to vote? (yes/no): no
You may not vote because:
you are not registered to vote
------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python vote_p12.py
Please enter your age: 20
Are you a citizen? (yes/no): no
Are you registered to vote? (yes/no): no
You may not vote because:
you are not a citizen
you are not registered to vote
-------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python vote_p12.py
Please enter your age: 17
Are you a citizen? (yes/no): no
Are you registered to vote? (yes/no): no
You may not vote because:
you are not old enough
you are not a citizen
you are not registered to vote
------------------------------------------------------------------------
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python vote_p12.py
Please enter your age: 20
Are you a citizen? (yes/no): yes
Are you registered to vote? (yes/no): yes
Great, you may vote!

'''