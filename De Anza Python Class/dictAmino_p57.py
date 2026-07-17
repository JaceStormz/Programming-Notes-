# dictAmino_p57.py 
# 3/14/26
# Python 3.13.9
'''
write a program that:
1) The mass of each possible amino acid is given in the file
2) Ask the user to enter an amino acid string consisting of only the letters shown in file aa.txt
- if the user enters an incorrect letter, then the program asks for another string
3) Ask the user to enter an amino acid string consisting of only the letters shown in file aa.txt
- if the user enters an incorrect letter, then the program asks for another string
'''


# 1) Put contents of file (aa.txt) into a dictionary
weights = {}

file = open("aa.txt")

for line in file:
    letter, value = line.split()
    weights[letter] = float(value)

file.close()

# 2) Ask the user to enter an amino acid string
while True:
    amino_string = input("Enter an amino acid string: ").upper()

    valid = True
    for ch in amino_string:
        if ch not in weights:
            valid = False
            break

    if valid:
        break
    else:
        print("Invalid letter detected. Please enter only letters from aa.txt.")

# 3) Calculate total weight
total_weight = 0

for ch in amino_string:
    total_weight += weights[ch]

print("Amino acid string:", amino_string)
print("Total weight =", total_weight)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python dictAmino_p57.py
Enter an amino acid string: SKADYEK
Amino acid string: SKADYEK
Total weight = 821.3919199999999

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python dictAmino_p57.py
Enter an amino acid string: abc
Invalid letter detected. Please enter only letters from aa.txt.
Enter an amino acid string: ajc
Invalid letter detected. Please enter only letters from aa.txt.
Enter an amino acid string: aoc
Invalid letter detected. Please enter only letters from aa.txt.
Enter an amino acid string: auc
Invalid letter detected. Please enter only letters from aa.txt.
Enter an amino acid string: axc
Invalid letter detected. Please enter only letters from aa.txt.
Enter an amino acid string: azc
Invalid letter detected. Please enter only letters from aa.txt.
Enter an amino acid string: skadyek
Amino acid string: SKADYEK
Total weight = 821.3919199999999
'''