
#--students = ["Hermione", "Harry", "Ron"]

""" 
this block of code is an example of a simple array list

print(students[0])
print(students[1])     
print(students[2])
"""
#--  the follow is the other ways of expessing that block of code in for loop
"""
for loop expressing loop array list and range takes a number

for student in students:
    print(student)
"""
#-- length or len takes a list of string
"""
for i in range(len(students)):
    print(i  + 1, students[i])
"""
#-- dictonary (dict) a data structure which allows to associate one value to another and is two dimensional
#-- list is a set of multiple values.
"""
students = {"Hermione": "Gyffindor",
            "Harry": "Gyffindor",
             "Ron" : "Gyffindor",
              "Draco": "Slytherin",
 }

"""

#-- simple dictonary example
"""
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""
#-- you will only the keys and values
"""
for student in students:
    print(student, students[student], sep=", ")
"""
students = [

    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Tarrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
