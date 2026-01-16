# inchCoverter_P6.py 
# Gautam Rao
# 1//15/26
# Python 3.13.9
# Program to convert height from feet and inches to inches only

# Get user input
feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your height in inches: "))

# Convert to total inches
totalInches = (feet * 12) + inches

# Display result
print("Your height in inches is: %.0f" %totalInches)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python inchCoverter.py 
Enter your height in feet: 5
Enter your height in inches: 11
Your height in inches is: 71

'''