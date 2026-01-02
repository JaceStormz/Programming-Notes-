#map is to apply every element to evry function 
"""
Docstring for maps
uppercased = map(str.upper, words)
"""
# list comperhensions to allow to create a list on the fly (in one line).

def main():
    yell("this", "is", "cs50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()