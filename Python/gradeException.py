# 08/06/2026
# gradeException.py
try:
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
except ValueError:
    print("Please enter a number. ")
finally:
    print("Thank you for using the Grade Calculator!")