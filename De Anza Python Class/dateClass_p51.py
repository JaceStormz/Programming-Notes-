# dateClass_p51.py 
# Gautam Rao
# 3/20/26
# Python 3.13.9
'''
1) Create a Date class.

1a) The class should have 3 properties (instance variables):

    month
    day
    year

1b) The class should have 2 actions (functions / methods) :

    setDate()  - allows the user to enter a date in 12/31/02 format 
    showDate() - displays the date. 

2) Create an instance of the Date class.

3) Test the object's setDate() and showDate() methods.

4) Submit your program code, including the test run at the bottom of your code.
'''

class Date:
    def __init__(self):
        self.month = 0
        self.day = 0
        self.year = 0

    def setDate(self):
        date_str = input("Enter a date (MM/DD/YY): ")
        
        try:
            parts = date_str.split("/")
            self.month = int(parts[0])
            self.day = int(parts[1])
            self.year = int(parts[2])
        except (IndexError, ValueError):
            print("Invalid format. Please use MM/DD/YY.")

    def showDate(self):
        print(f"Date is: {self.month:02d}/{self.day:02d}/{self.year:02d}")


# 2) Create an instance of the Date class
my_date = Date()

# 3) Test the methods
my_date.setDate()
my_date.showDate()

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python dateclass_p51.py
Enter a date (MM/DD/YY): 03/20/26
Date is: 03/20/26

'''