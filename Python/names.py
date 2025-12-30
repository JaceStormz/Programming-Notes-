"""
names = []

for _ in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
"""
# how do you save the name use in the previous code well a File I/O does the trick.
 
"""name = input("What is your name? ")
# "w" is to write to the file
# "a" is to append to the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""
# ways to strip space between the lines
"""with open("names.txt","r" ) as file:
    lines = file.readline()

for line in lines:
    print("Hello,", line.rstrip())"""
# pythonic form of strip line
"""with open("names.txt","r" ) as file:
    for line in file:
        print("hello,", line.rstrip())"""
# print the lines save the names and sort them
"""names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {names}")"""
# just to sort a more effective way is:
with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())
# CSV file or Comma Seperated Value. It adds another dimension of data storage
