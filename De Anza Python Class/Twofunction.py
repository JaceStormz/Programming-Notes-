# Twofunction.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
# A program two function definitions, and call each function appropriately in order to test and show how each function works

def speed(distance, time):
    print(f"Speed is {distance / time:.2f}")


def middle(a, b, c):
    # Return the value that is neither the min nor the max
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c


def main():
    print("Testing speed function:")
    speed(150, 3)

    print("\nTesting middle function:")
    print(f"The middle value is: {middle(10, 25, 15)}")


if __name__ == "__main__":
    main()

'''

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python Twofunction.py
Testing speed function:
Speed is 50.00

Testing middle function:
The middle value is: 15

'''