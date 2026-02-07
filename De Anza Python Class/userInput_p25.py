# randInt_p24.py
# Gautam Rao
# 2/04/26
# Python 3.13.9
# A program that asks the user to input a sentence

# user input for the sentence and letter to be counted. Upper case for the upper method
sentence = input("Enter a sentence: ").upper()
letter1 = input("Enter the first letter to count: ").upper()
letter2 = input("Enter the second letter to count: ").upper()

count1 = 0
count2 = 0

# Loop through the sentence
for chr in sentence:
    # checks for the first letter
    if chr == letter1:
        count1 += 1
    # checks for the second letter
    if chr == letter2:
        count2 += 1

# Output of results
print("---------------------------------------------")
print(f"Sentence: {sentence}")
print(f"Letter '{letter1}' appears {count1} times.")
print(f"Letter '{letter2}' appears {count2} times.")


'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python userInput_p25.py
Enter a sentence: HELLO WORLD
Enter the first letter to count: O
Enter the second letter to count: L
---------------------------------------------
Sentence: HELLO WORLD
Letter 'O' appears 2 times.
Letter 'L' appears 3 times.

'''