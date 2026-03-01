# split_p38.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
# a program that asks the user to enter a sentence


# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Assume the first word is the longest
longest_word = words[0]

# Loop through each word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Display the result
print(f"The longest word is: {longest_word} ")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python split_p38.Py
Enter a sentence: Hello Professor I hope you enjoy my project38
The longest word is: Professor

'''