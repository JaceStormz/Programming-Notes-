# Input_P3.py
# Gautam Rao
# 1//06/26
# Python 3.13.9
# Description: Program to take input in Python

name = input("Please enter Your Name: ")                        # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: "))  # a float
age = int (input ("Please enter your age (whole number): " ))   # an integer
weightKg= weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print ( weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ')                # end=' ' prevents new line
print ("kilograms ")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> Input_P3
Please enter Your Name: Gautam Rao
Please enter Your weight in lbs: 207.5
Please enter your age (whole number): 37
Hello Human Gautam Rao your weight is
207.5 lbs
which equals = 94.12 kilogram

'''