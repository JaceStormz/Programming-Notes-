students = ["hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i+1, student)

# enumerate iterating of over value and its index
# dictionary comprehension
# filter but a functions that returns true or false or boolean question
# list comperhensions
"""
Docstring for enumerate

students = ["hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i+1, student)


"""

"""
Docstring for dictionary comprehension
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "RavenClaw"},
]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

"""
"""
Docstring for list comperhensions

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "RavenClaw"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

----------------------------------------------------------------------------------
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "RavenClaw"},
]

gryffindors = [
    student ["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

"""
"""
list comprehension

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "RavenClaw"},
]
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]



"""