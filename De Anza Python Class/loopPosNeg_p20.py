# loopPosNeg_p20.py
# 1//24/26
# Python 3.13.9
'''
 A program that reads in X whole numbers and outputs the sum of all positive numbers.
 The sum of all negative numbers, the sum of all positive and negative numbers. 
'''

toContinue = 'yes'
# repeat funcitonality
while toContinue.lower() == 'yes':
    sumAll = 0
    sumNeg = 0
    sumPos = 0
    #user is entering the number of integers
    usernum = int(input("How many numbers would you like to enter? "))


    # user enters integers
    for num in range(usernum):
        enterednum = int(input(f'Enter a Number {num + 1}: '))
        # all negatives numbers are added
        if enterednum < 0:
            sumNeg += enterednum
        # all positives numbers are added 
        else: 
            sumPos += enterednum
        # adding values
        sumAll += enterednum
    #output of each value type
    print('------------------------------')
    print(f'The sum of all negative values: {sumNeg}')
    print(f'The sum of all positive values: {sumPos}')
    print(f'The sum of all values: {sumAll}')
    # strip the empty space and made the character to lower case to match the required values
    toContinue = input('Would you like to continue (yes or no): ').strip().lower()


'''
PS C:\Users\super\OneDrive\Desktop\Repo_Files\De Anza Python Class> python loopPosNeg_p20.py
How many numbers would you like to enter? 4
Enter a Number 1: 3
Enter a Number 2: -4
Enter a Number 3: -6
Enter a Number 4: 5
------------------------------
The sum of all negative values: -10
The sum of all positive values: 8
The sum of all values: -2
Would you like to continue (yes or no): no

'''