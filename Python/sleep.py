# generator it can generate a massive amount of data but only create a little bit of it
# yield it generates one data at a time

def main(): 
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep" * i


if __name__ == "__main__":
    main()