#Square and Power

def main():
    x= int(input("What is X? "))
    print("X squared is", square(x))

def square(n):
    return n * n # can use ** 2 or pow(n, 2)

main()
