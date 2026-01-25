# loopPosNeg_p20.py
# Gautam Rao
# 1//24/26
# Python 3.13.9
'''
 A program that reads in X whole numbers and outputs the sum of all positive numbers.
 The sum of all negative numbers, the sum of all positive and negative numbers. 
'''

toContinue = 'yes'
# repeat funcitonality
while toContinue.lower() == 'yes':
    sum = 0
    sumNeg = 0
    sumPos = 0
    #user is entering the number of integers
    usernum = int(input("how many numbers would you like to enter? "))


    # user enters integers
    for num in range(0, usernum, 1):
        enterednum = int(input(f'Enter a Number {num}: '))
        # adding values and printig output
        sum += enterednum
        if(enterednum < 0):
            sumNeg += enterednum
        # all positives numbers are added 
        elif(enterednum > 0) or (enterednum == 0):
            sumPos += enterednum
    #output of each value type
    print(f'The sum of all values: {sum}')
    print(f'The sum of all negative values: {sumNeg}')
    print(f'The sum of all negative values: {sumPos}')
# user input to repeat
toContinue = input('Would you like to continue (yes or no)')