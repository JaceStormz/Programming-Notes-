# lastWord_p39.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
# Ask the user to enter their own word, and count how many times their word appears in the sentence

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ").lower()

# Split the sentence into words
words = sentence.split()

# Show how many words are in the sentence
print("Number of words:", len(words))

# Show the last word of the sentence
print("Last word:", words[-1])

# Ask the user to enter their own word
user_word = input("Enter a word to count: ")

# Count how many times the word appears (without using count())
count = 0
for word in words:
    if word == user_word:
        count += 1

# Show the result
print(f"The word '{user_word}' appears {count} time(s) in the sentence.")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python lastWord_p39.py
Enter a sentence: The fox and the dog
Number of words: 5
Last word: dog
Enter a word to count: the
The word 'the' appears 2 time(s) in the sentence.

'''