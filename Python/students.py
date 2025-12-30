import csv

# CSV file or Comma Seperated Value. It adds another dimension of data storage
students = []
with open("students.csv") as file:
# DictReader access dictonary but you have create the column "Name,Home" to avoid issues if the csv file orders get reversed
    reader = csv.reader(file)
    for name, home in reader:
         students.append({"name": name,"home": home})


    """for line in file:
        name, house = line.rstrip().split(",")
    """
# create a dictionary
"""
        student = {}
        student ["name"] = name
        student ["house"] = house
        """
# the same this in comment line can be written like this. instead of 3 line we get 1
"""student = {"name": name, "house": house}
        students.append(student)"""
# in a dictionary to add a string in a double quote "" you put a single quote '' to place a string in a string
# python can pass functions as arguments hence the keyword "Key"
"""def get_name(student):
     return student["name"]

for student in sorted(students, key=get_name, reverse=True):"""
# the keyword "lambda" is funtion that can replace as an anonymous funtion or has no name because the get_name funtion since the function is used only once thus replacing it because the equalilant of it.
for student in sorted(students, key=lambda student: ["name"]):

        print(f"{student['name']} is in {student['house']}")
        # the first row is the value and the second row is the comma seperated value
        """students.append(f"{name[0]} is in {house[1]}")"""
# sloppy want of sortting from a pythonic code
"""for student in sorted(students):
    print(student)"""

