# p10.py 
# 1//15/26
# Python 3.13.9
# Program which asks the user for a student's grade as a percent, and then returns their letter grade.

# Keep asking until a valid grade is entered
while True:
    grade = float(input("Enter the student's grade (0–100): "))

    # Validate input
    if grade < 0 or grade > 100:
        print("ERROR")
    else:
        break

# Determine letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Display result
print("Letter grade: ", letter)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python p10.py
Enter the student's grade (0–100): -1
ERROR
Enter the student's grade (0–100): 75
Letter grade:  C

'''