# p9.py 
# 1//15/26
# Python 3.13.9
# program will convert the feet and inches into total_inches, and then print a message.

# Get user input
feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your height in inches: "))

# Convert height to total inches
totalInches = (feet * 12) + inches

# Print height message
print("Your height is %.0f inches." %totalInches )

if totalInches > 72:
    print("You're tall.")
elif totalInches >= 60:
    print("You are average.")
else:
    print("You are vertically challenged.")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p9.py
Enter your height in feet: 6
Enter your height in inches: 2
Your height is 74 inches.
You're tall.
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p9.py
Enter your height in feet: 5
Enter your height in inches: 6
Your height is 66 inches.
You are average.
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p9.py
Enter your height in feet: 4
Enter your height in inches: 11
Your height is 59 inches.
You are vertically challenged.
'''