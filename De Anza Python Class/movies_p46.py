# movies_p46.py 
# 3/07/26
# Python 3.13.9
'''
Write a Python program to do the following:

    Let the user enter a file name (such as "myMovies.txt").
    Let the user enter the titles of 4 of their favorite movies using a loop.
    Write using a loop the 4 movie titles to a file, one per line, and closes the file.
    Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them in a list, and then shows the list.
    Write the titles in reverse order into a file "reverseOrder.txt"

'''

# Ask user for file name
file_name = input("Please enter a file name: ")

# Create a list to store movie titles
movies = []

# Ask the user for 4 movie titles using a loop
for i in range(1, 5):
    title = input(f"Please enter a movie title #{i}: ")
    movies.append(title)

# Write the movie titles to the file
print(f"... Writing the 4 movie titles to file '{file_name}'")
file = open(file_name, "w")

for movie in movies:
    file.write(movie + "\n")

file.close()

# Read the movie titles from the file
file = open(file_name, "r")
content = file.read()
file.close()

movie_list = content.splitlines()

print("... Reading the 4 movie titles from file into a list:", movie_list)

# Write the movie titles in reverse order to another file
print("... Writing the 4 movie titles in reverse to 'reverseOrder.txt'")
reverse_file = open("reverseOrder.txt", "w")

for movie in reversed(movie_list):
    reverse_file.write(movie + "\n")

reverse_file.close()

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python movies_p46.py
Please enter a file name: myMovies.txt
Please enter a movie title #1: Pride and Predujice
Please enter a movie title #2: Life of Pi
Please enter a movie title #3: Amadeus
Please enter a movie title #4: The Hobbit
... Writing the 4 movie titles to file 'myMovies.txt'
... Reading the 4 movie titles from file into a list: ['Pride and Predujice', 'Life of Pi', 'Amadeus', 'The Hobbit']
... Writing the 4 movie titles in reverse to 'reverseOrder.txt'

'''