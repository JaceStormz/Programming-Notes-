# Lab6.py
# 06/20/2026
# Python 3.13.9
"""
Assignment requirements
Lab6.txt file downloaded from Canvas

Write an app that lets the user look up the current top programming languages.
Overview
Lab 6 consists of 2 files:
ranking.py: the backend that reads in data from an input file and provides methods to search the data.
ui.py: the frontend that interacts with the user: let user look up programming languages and display the search
result.
Input file
The input data are from the first 2 tables on the TIOBE Index page. The 2 tables show the top 50 programming
languages in terms of usage for March 2023. If you want to see the html of the entire page, right click at the
page and select View Page Source, but to simplify the input for this lab, the html source of the first 2 tables is
stored in the file lab6.txt.
In the lab6.txt file:
    - There are multiple lines of htlm text. The lines contain 1 or more html tags in the format: < tag >
    - There are 2 lines of text that contain the data of the 2 tables. Both lines start with the 2 html tags:
    <tr><td>
    - In each of these 2 lines, buried in between the html tags are the input data for your app. Here’s the first part
    of the line of text for the 2nd table: <tr><td>21</td><td>SAS</td><td>0.64%</td></tr> …
    Comparing the green data above with the 2nd table on the web page, we see that SAS has a ranking of 0.64%
    and is at number 21 out of the 50 languages. This corresponds with the data of the first row of the 2nd table.
    ranking.py
Do the following steps to create a Ranking class that stores data from the input file and provides search
methods.
1. A method to initialize the Ranking object with data from the input file:
    • Accept a filename as input argument or use the default parameter of “lab6.txt”.
    • Read in from the file and use regex to extract all the language data (like the green data above) from the
    2 tables.
    • From the first table the data are: language, ranking, change
    • From the second table the data are: language, ranking
    • Your code should only access the file one time (one loop to read in each line).
    • Store the data in a container of your choice. Choose carefully and your code can be shorter.
When done the container should have data for all 50 languages: first 20 in 1st table, next 30 in 2nd table.
2. A method that allows for a search of languages, sorted by ranking:
    • Return a generator of languages and rankings, sorted by ranking.
    • You should not have to create any container in this method.
3. A generator method that yields languages, sorted by change:
    • Accept a boolean input argument to indicate positive change or negative change.
    • Based on the boolean, work with changes that are positive or negative in the top 20 languages, and yield
    one language and corresponding change at a time, in order of largest to smallest change.
• Use the “key” parameter of the sorted() function to sort by the change.
4. A method that allows for a search of one or more languages:
    • Accept one or more languages as input arguments. Note that the input arguments must be individual
    languages and not a container.
    • For each input language:
    - if found: output the language name as it appears in the table on the website, the rating, and the
    change if available
    - if not found: output a ‘not found’ indicator
    • The language search should be case insensitive.
    5. Additional methods as needed.
    6. Note that the backend and does not interact with the user.
ui.py
Create a UI class to interact with the user.
1. A method to create the Ranking object:
    • If there is file open exception, loop to let the user enter an input filename.
    Note that the UI should not open any file. Opening file is the job of the backend.
    • After the Ranking object is created, print the total number of languages and input filename that the
Ranking object has. See sample output.
2. A method to let the user view, by ranking order, one language at a time:
    • Call the appropriate method of the Ranking object.
    • Print: the count, language, ranking in column format.
    • Then wait for the user to: - press the Enter key to print the next language
    or - press any other key to end the printing
    • If the user keeps pressing the Enter key until there’s no more language, print an ending message. The
    code should not need to use the total number of languages to check that there’s no more language.
• See sample output.
3. A method to let the user view languages with positive or negative change, sorted by change order:
    • Ask the user to choose positive or negative change. Keep looping until you get a valid answer. It’s your
    choice what the valid answer is (1, 2 or ‘p’, ‘n’).
    • Call the appropriate method of the Ranking object.
    • Print all the languages and changes, in descending order of change.
    • See sample output.
4. A method to let the user view all info of one or more languages:
    • Ask the user for a list of language names, separated by comma.
    • Call the appropriate method of the Ranking object, passing to it individual language names (not a
    container of names).
    • Print all information of each language, one per line.
    • See sample output.
5. A run method that coordinates all the interactions with the user:
    • Print a menu with 3 choices: r. Languages by ranking
    c. Languages by change
    l. Language info
    q. Quit
    • Read the user choice (case insensitive) and process the user choice until the user chooses ‘q’.
    • Do not use an if else statement to process the user choice. Instead, create a look up table to quickly
determine the method to process the user choice and to print an error message if the choice is not valid.
6. Other methods as needed.
7. At the end ui.py, use the following code to start the UI object:
UI().run()
Additional requirements
    • Handle exceptions, such as file open error and user input error, as needed.
    • Put your name at the top of each file
    • Have a docstring for all public methods

"""
import re


class Ranking:
    """Stores programming language ranking information."""

    def __init__(self, filename="lab6.txt"):
        """
        Read ranking data from the input file.

        Args:
            filename (str): Input filename.
        """
        self.filename = filename
        self.languages = {}

        with open(filename, "r", encoding="utf-8") as infile:
            for line in infile:

                # First table (Top 20)
                if line.startswith("<tr><td>1</td>"):
                    pattern = (
                        r'<td>([^<]+)</td>'
                        r'<td>([\d.]+%)</td>'
                        r'<td>([+-][\d.]+%)</td></tr>'
                    )

                    matches = re.findall(pattern, line)

                    for language, rating, change in matches:
                        self.languages[language.lower()] = {
                            "name": language,
                            "rating": rating,
                            "change": change
                        }

                # Second table (21-50)
                elif line.startswith("<tr><td>21</td>"):
                    pattern = (
                        r'<tr><td>\d+</td>'
                        r'<td>([^<]+)</td>'
                        r'<td>([\d.]+%)</td></tr>'
                    )

                    matches = re.findall(pattern, line)

                    for language, rating in matches:
                        self.languages[language.lower()] = {
                            "name": language,
                            "rating": rating,
                            "change": None
                        }

    def __len__(self):
        """Return number of languages."""
        return len(self.languages)

    def getFilename(self):
        """Return input filename."""
        return self.filename

    def languagesByRanking(self):
        """
        Generator yielding languages sorted by ranking.

        Yields:
            tuple: (language, rating)
        """
        return (
            (info["name"], info["rating"])
            for info in sorted(
                self.languages.values(),
                key=lambda x: float(x["rating"].rstrip("%")),
                reverse=True
            )
        )

    def languagesByChange(self, positive=True):
        """
        Yield languages sorted by change.

        Args:
            positive (bool): True for positive changes,
                             False for negative changes.

        Yields:
            tuple: (language, change)
        """
        items = [
            info
            for info in self.languages.values()
            if info["change"] is not None
            and (
                float(info["change"].rstrip("%")) > 0
                if positive
                else float(info["change"].rstrip("%")) < 0
            )
        ]

        items = sorted(
            items,
            key=lambda x: abs(float(x["change"].rstrip("%"))),
            reverse=True
        )

        for info in items:
            yield info["name"], info["change"]

    def search(self, *languages):
        """
        Search for one or more languages.

        Args:
            *languages: Individual language names.

        Returns:
            list
        """
        results = []

        for language in languages:
            key = language.strip().lower()

            if key in self.languages:
                info = self.languages[key]
                results.append(
                    (
                        info["name"],
                        info["rating"],
                        info["change"]
                    )
                )
            else:
                results.append((language, None, None))

        return results