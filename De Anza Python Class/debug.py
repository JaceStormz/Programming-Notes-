# debug.py 
# 2/28/26
# Python 3.13.9
# debug program provided by the instuctor and modified to match the output required for the project

def isEven(num):   # add parameter
    if num % 2 == 0:   # use == for comparison and add colon
        return True
    else:
        return False

def main():
    num = int(input("Enter a number: "))   # convert input to int
    print("The number %i is even: %s" % (num, isEven(num)))

main()   # must call the function

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python debug.py
Enter a number: 5
The number 5 is even: False

'''