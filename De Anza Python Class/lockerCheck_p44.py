# lockerCheck_p44.py 
# Gautam Rao
# 2/21/26
# Python 3.13.9
# Write a program to determine which exact locker numbers are open, and total number that are open.


def main():
    lockers = [False] * 1000  # False = closed, True = open

    # Toggle lockers
    for step in range(1, 1001):
        for i in range(step - 1, 1000, step):
            lockers[i] = not lockers[i]

    # Collect open lockers
    open_lockers = []
    total_open = 0

    for i, is_open in enumerate(lockers, start=1):
        if is_open:
            open_lockers.append(i)
            total_open += 1

    print("Open lockers:")
    print(*open_lockers)
    print("Total open lockers:", total_open)


if __name__ == "__main__":
    main()

    '''
    PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python lockerCheck_p44.py                                                                                            
    Open lockers:
    1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961
    Total open lockers: 31

    '''