# ui.py
# Gautam Rao
# 06/20/2026
# Python 3.13.9
from lab6 import Ranking


class UI:
    """User interface for ranking application."""

    def __init__(self):
        """Create Ranking object."""
        while True:
            try:
                filename = input(
                    "Input file (press Enter for lab6.txt): "
                ).strip()

                if filename == "":
                    filename = "lab6.txt"

                self.rankings = Ranking(filename)

                print(
                    f"\nLoaded {len(self.rankings)} languages "
                    f"from {self.rankings.getFilename()}\n"
                )

                break

            except FileNotFoundError:
                print("File not found. Try again.\n")

    def showRankings(self):
        """Display languages one at a time by ranking."""
        gen = self.rankings.languagesByRanking()

        count = 1

        while True:
            try:
                language, rating = next(gen)

                print(
                    f"{count:2}  "
                    f"{language:<25}"
                    f"{rating:>8}"
                )

                count += 1

                answer = input(
                    "Press Enter for next "
                    "or any key to stop: "
                )

                if answer != "":
                    break

            except StopIteration:
                print("\nNo more languages.\n")
                break

    def showChanges(self):
        """Display languages sorted by change."""
        while True:
            choice = input(
                "Positive or Negative changes? "
                "(p/n): "
            ).lower()

            if choice in ("p", "n"):
                break

            print("Invalid choice.")

        positive = choice == "p"

        print()

        for language, change in \
                self.rankings.languagesByChange(positive):
            print(f"{language:<25}{change}")

        print()

    def languageInfo(self):
        """Display information for selected languages."""
        names = input(
            "Enter language names separated by commas: "
        )

        names = [name.strip() for name in names.split(",")]

        print()

        for language, rating, change in \
                self.rankings.search(*names):

            if rating is None:
                print(f"{language}: Not found")

            else:
                if change is None:
                    print(
                        f"{language}: "
                        f"Rating={rating}"
                    )
                else:
                    print(
                        f"{language}: "
                        f"Rating={rating}, "
                        f"Change={change}"
                    )

        print()

    def run(self):
        """Run the application."""
        menu = {
            "r": self.showRankings,
            "c": self.showChanges,
            "l": self.languageInfo
        }

        while True:
            print("r. Languages by ranking")
            print("c. Languages by change")
            print("l. Language info")
            print("q. Quit")

            choice = input(
                "\nChoice: "
            ).lower()

            if choice == "q":
                print("Goodbye.")
                break

            action = menu.get(choice)

            if action:
                action()
            else:
                print("Invalid choice.\n")


UI().run()

"""
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python ui.py
Input file (press Enter for lab6.txt): 

Loaded 50 languages from lab6.txt

r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: r
 1  Python                     14.83%
Press Enter for next or any key to stop: 
 2  C                          14.73%
Press Enter for next or any key to stop: 
 3  Java                       13.56%
Press Enter for next or any key to stop: 
 4  C++                        13.29%
Press Enter for next or any key to stop: 
 5  C#                          7.17%
Press Enter for next or any key to stop: 
 6  Visual Basic                4.75%
Press Enter for next or any key to stop: 
 7  JavaScript                  2.17%
Press Enter for next or any key to stop: 
 8  SQL                         1.95%
Press Enter for next or any key to stop: 
 9  PHP                         1.61%
Press Enter for next or any key to stop: 
10  Go                          1.24%
Press Enter for next or any key to stop: 
11  Assembly language           1.11%
Press Enter for next or any key to stop: 
12  MATLAB                      1.08%
Press Enter for next or any key to stop: 
13  Delphi/Object Pascal        1.06%
Press Enter for next or any key to stop: 
14  Scratch                     1.00%
Press Enter for next or any key to stop: 
15  Classic Visual Basic        0.98%
Press Enter for next or any key to stop: 
16  R                           0.93%
Press Enter for next or any key to stop: 
17  Fortran                     0.79%
Press Enter for next or any key to stop: 
18  Ruby                        0.76%
Press Enter for next or any key to stop: 
19  Rust                        0.73%
Press Enter for next or any key to stop: 
20  Swift                       0.71%
Press Enter for next or any key to stop: 
21  SAS                         0.64%
Press Enter for next or any key to stop: 
22  (Visual) FoxPro             0.62%
Press Enter for next or any key to stop: 
23  COBOL                       0.58%
Press Enter for next or any key to stop: 
24  Perl                        0.58%
Press Enter for next or any key to stop: 
25  F#                          0.53%
Press Enter for next or any key to stop: 
26  Objective-C                 0.43%
Press Enter for next or any key to stop: 
27  Transact-SQL                0.42%
Press Enter for next or any key to stop: 
28  Ada                         0.42%
Press Enter for next or any key to stop: 
29  Lisp                        0.40%
Press Enter for next or any key to stop: 
30  Lua                         0.36%
Press Enter for next or any key to stop: 
31  Haskell                     0.34%
Press Enter for next or any key to stop: 
32  PL/SQL                      0.34%
Press Enter for next or any key to stop: 
33  Julia                       0.29%
Press Enter for next or any key to stop: 
34  Groovy                      0.29%
Press Enter for next or any key to stop: 
35  Kotlin                      0.27%
Press Enter for next or any key to stop: 
36  Dart                        0.24%
Press Enter for next or any key to stop: 
37  CFML                        0.23%
Press Enter for next or any key to stop: 
38  Scala                       0.23%
Press Enter for next or any key to stop: 
39  Prolog                      0.23%
Press Enter for next or any key to stop: 
40  RPG                         0.20%
Press Enter for next or any key to stop: 
41  OpenEdge ABL                0.19%
Press Enter for next or any key to stop: 
42  Bash                        0.19%
Press Enter for next or any key to stop: 
43  ABAP                        0.18%
Press Enter for next or any key to stop: 
44  Logo                        0.17%
Press Enter for next or any key to stop: 
45  Awk                         0.17%
Press Enter for next or any key to stop: 
46  TypeScript                  0.17%
Press Enter for next or any key to stop: 
47  Emacs Lisp                  0.16%
Press Enter for next or any key to stop: 
48  D                           0.16%
Press Enter for next or any key to stop: 
49  LabVIEW                     0.15%
Press Enter for next or any key to stop: 
50  PowerShell                  0.15%
Press Enter for next or any key to stop: r
r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: c
Positive or Negative changes? (p/n): p

C++                      +4.64%
Java                     +2.37%
C                        +1.67%
C#                       +1.25%
Python                   +0.57%
Scratch                  +0.47%
Fortran                  +0.40%
Classic Visual Basic     +0.38%
MATLAB                   +0.28%
Go                       +0.26%
Rust                     +0.22%
SQL                      +0.11%
Ruby                     +0.10%
JavaScript               +0.09%

r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: l
Enter language names separated by commas: C#

C#: Rating=7.17%, Change=+1.25%

r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: python
Invalid choice.

r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: Python
Invalid choice.

r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: l
Enter language names separated by commas: Python

Python: Rating=14.83%, Change=+0.57%

r. Languages by ranking
c. Languages by change
l. Language info
q. Quit

Choice: q
Goodbye.

"""