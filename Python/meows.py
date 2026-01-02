import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")


"""import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")
"""

# argparse pass in configuration options or handles all the parsing.
# when n: datatype is a type hint telling python what type of variable it will accept rather than defaulting the value.
# mypy is a checker for instruct the issue found in the code.
# -> None: is returns none for the variable
"""def meow(n: int) -> None:
    return "meow\n" * n



number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
"""
# docstring is to document the functions and code how to use them with plus check errors """"


# Constants
"""class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
"""
# python is a dynamic language
#type hints
