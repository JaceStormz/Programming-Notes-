# Lab5.py
# 05/26/2026
# Python 3.13.9
'''
Write a program that lets customers at a cafeteria purchase food and drink
Overview
The customer is presented with a menu of several items of hot food, packaged food, and drinks, along with their prices.
The customer chooses the food / drink, and then a receipt of all items, prices, and total price is printed for the customer.
Program Design Overview
The program has several classes:
• A UI class to interact with the user: print a menu, read in the user choices, and prints the receipt.
• An Inventory class that reads in all foods and drinks from an input file and store all items in containers. Each item is
an object of the sale item inheritance hierarchy.
• A sale item inheritance hierarchy of your choice, to support these types of sale items:
• Packaged food: food that are prepackaged (such as a bag of chips or a boxed salad)
with attributes: name, id number, price
Example: Granola Bar, 10, 2.50
• Hot food: food that are prepared and heated (like pizza)
with attributes: name, id number, price, tax
Example: Pizza, 20, 9.00
- The tax rate should be a constant and set to 9.13% (rate for SC county)
• Drink: bottled or canned drinks
with attributes: name, id number, price, size, tax, CRV
Example: Soda, 30, 1.50, S
- The CRV should be a constant and set to 0.05 for a small drink (S above) or 0.10 for a large drink (L). The CRV
will be added to the price when the customer buys the drink
- The tax rate should be a constant and set to 9.13% (rate for SC county). The tax applies to the CRV also.
The sale item inheritance hierarchy
Design:
• All shared attributes and methods should be pushed up into the superclass. Try not to duplicate a method or
attribute at the subclass level, when this attribute can appear one time in the superclass.
• A subclass is a specialization of its superclass, with specialized attributes / methods.
Conversely, if a subclass has no specialized attributes / methods, then there’s no need to create this subclass.
Requirements:
• The __repr__ method should return:
• For the packaged food: a string in the format name(id number):price
• For the hot food: a string in the format name(id number):price - heated
• For the drink: a string in the format name(id number):price
• Price calculation: each object is responsible for calculating its final price, whether with or without tax, with or
without CRV
The Inventory class
• The input file is items.csv. Each line of the file is for one food or drink item, in the format:
id number,name,price,optional size
• Example: 10,Granola Bar,3.50
• For the foods there is no size field. For the drinks the size field is either ‘S’ or ‘L’ (for small or large)
• A packaged food id number is in the 10-19 range, the hot food id number is 20-29, the drink id number is 30-39
• The __init__ method:
• reads each line of the input file
• creates and initializes an appropriate item object, based on the id number of the item. Don’t hard code the first 2
items to be one type, the next 2 items to be the next type, etc.
• stores the object in container(s) of your choice
• The __repr__ method returns the string with the number of each type of food or drink.
• Any other method to support the UI object
The UI class Version 1
• The __init__ method that:
• creates an Inventory object and prints the object
• or end the program if the input file can’t be opened (note that the UI object should not open files)
• A method to print the menu of food and drink for the user:
• Show a header for each food / drink type
• Print each item to see that the __repr__ of each item is in the correct format.
For each item that has tax and CRV, also print the final price of the item
• Sample output
2 packaged foods, 2 hot foods, 2 drinks # print of Inventory object
Packaged food # header
Granola Bar(10):3.5
Fruit(11):2.0
Salad(12):6.0
Hot food # header
Wings(20):9.5 - heated
10.37 # final price with tax
Pizza(21):7.0 - heated
7.64
Drink # header
Soda(30):1.5
1.69 # final price with CRV and tax
Juice(31):2.0
2.29
Water(32):1.0
1.15
UI class - Regular Expressions
Add code to the UI class V1 to create the final UI class
• Modify the method to print the menu so that instead of printing the __repr__ string of the food/drink object:
Granola Bar(10):3.5
The code uses regular expression to extract the name and price from the string and print them in a more user
friendly way: 1 Granola Bar $ 3.50
where the 1 is the menu choice for the item.
The entire menu should be printed as below:
Packaged food
1 Granola Bar $ 3.50
2 Fruit $ 2.00
3 Salad $ 6.00
Hot food
4 Wings $ 9.50
5 Pizza $ 7.00
Drinks
6 Soda $ 1.50
7 Juice $ 2.00
8 Water $ 1.00
Note that the name and price in the menu must be extracted from the __repr__ string of the food/drink object.
Don’t use a getter method to access the name and price from the object.
• Add a method for the user to order the food/drink by choosing one or more numeric choices from the menu.
The numeric choices are entered on one line of input, and there can be spaces or words or punctuations in between
the numbers. Hint: regular expressions can help here.
• Add code to use the input numbers to print each food/drink item and its final price (including optional tax and CRV)
in column format, with dollar signs where appropriate, and then print the total of all the items.
If the user input is not within range, print all the invalid numbers after printing the total (See sample output)
• Add code to ask the user whether to continue, and let the user buy more food/drink if the choice is ‘y’.

'''
import re

# ---------------------- Sale Item Classes ----------------------

class SaleItem:
    def __init__(self, name, itemId, price):
        self.name = name
        self.itemId = int(itemId)
        self.price = float(price)

    def finalPrice(self):
        return self.price

    def __repr__(self):
        return f"{self.name}({self.itemId}):{self.price}"


class PackagedFood(SaleItem):
    pass


class HotFood(SaleItem):
    TAXRATE = 0.0913

    def finalPrice(self):
        return self.price + (self.price * HotFood.TAXRATE)

    def __repr__(self):
        return f"{self.name}({self.itemId}):{self.price} - heated"


class Drink(SaleItem):
    TAXRATE = 0.0913
    SMALLCRV = 0.05
    LARGECRV = 0.10

    def __init__(self, name, itemId, price, size):
        super().__init__(name, itemId, price)
        self.size = size.upper()

    def getcrv(self):
        if self.size == "S":
            return Drink.SMALLCRV
        else:
            return Drink.LARGECRV

    def finalPrice(self):
        subtotal = self.price + self.getcrv()
        return subtotal + (subtotal * Drink.TAXRATE)


# ---------------------- Inventory Class ----------------------

class Inventory:
    def __init__(self, filename):
        self.packagedFoods = []
        self.hotFoods = []
        self.drinks = []

        try:
            file = open(filename, "r")

            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                itemId = int(parts[0])
                name = parts[1]
                price = float(parts[2])

                # Packaged Food
                if 10 <= itemId <= 19:
                    item = PackagedFood(name, itemId, price)
                    self.packagedFoods.append(item)

                # Hot Food
                elif 20 <= itemId <= 29:
                    item = HotFood(name, itemId, price)
                    self.hotFoods.append(item)

                # Drink
                elif 30 <= itemId <= 39:
                    size = parts[3]
                    item = Drink(name, itemId, price, size)
                    self.drinks.append(item)

            file.close()

        except IOError:
            raise IOError("Could not open items.csv")

    def __repr__(self):
        return (
            f"{len(self.packagedFoods)} packaged foods, "
            f"{len(self.hotFoods)} hot foods, "
            f"{len(self.drinks)} drinks"
        )

    def getAllitems(self):
        return self.packagedFoods + self.hotFoods + self.drinks


# ---------------------- UI Class ----------------------

class UI:
    def __init__(self):
        try:
            self.inventory = Inventory("items.csv")
            print(self.inventory)

        except IOError as e:
            print(e)
            exit()

    def printMenu(self):
        print("\nPackaged Food")

        menuItems = []
        choiceNumber = 1

        # Regex pattern
        pattern = r"(.+)\((\d+)\):([\d.]+)"

        # Packaged Foods
        for item in self.inventory.packagedFoods:
            text = repr(item)

            match = re.search(pattern, text)

            if match:
                name = match.group(1)
                price = float(match.group(3))

                print(f"{choiceNumber} {name} $ {price:.2f}")
                menuItems.append(item)
                choiceNumber += 1

        print("\nHot Food")

        for item in self.inventory.hotFoods:
            text = repr(item)

            match = re.search(pattern, text)

            if match:
                name = match.group(1)
                price = float(match.group(3))

                print(f"{choiceNumber} {name} $ {price:.2f}")
                menuItems.append(item)
                choiceNumber += 1

        print("\nDrinks")

        for item in self.inventory.drinks:
            text = repr(item)

            match = re.search(pattern, text)

            if match:
                name = match.group(1)
                price = float(match.group(3))

                print(f"{choiceNumber} {name} $ {price:.2f}")
                menuItems.append(item)
                choiceNumber += 1

        return menuItems

    def orderItems(self):
        menuItems = self.printMenu()

        print("\nSelect a number from the menu: ")
        userInput = input()

        # Find ALL integers including negatives
        numbers = re.findall(r"-?\d+", userInput)

        selectedItems = []
        invalidNumbers = []

        for num in numbers:
            choice = int(num)

            # Negative numbers are invalid
            if choice < 0:
                invalidNumbers.append(choice)

            # Valid menu choice
            elif 1 <= choice <= len(menuItems):
                selectedItems.append(menuItems[choice - 1])

            # Invalid positive numbers
            else:
                invalidNumbers.append(choice)

        print("\nReceipt")
        print("-" * 40)
        print(f"{'Item':20}{'Price':>10}")
        print("-" * 40)

        total = 0

        for item in selectedItems:
            final = item.finalPrice()
            total += final

            print(f"{item.name:20}$ {final:>7.2f}")

        print("-" * 40)
        print(f"{'TOTAL':20}$ {total:>7.2f}")

        # Print invalid numbers
        if invalidNumbers:
            print("\nInvalid selections:")
            for num in invalidNumbers:
                print(num)

    def run(self):
        while True:
            self.orderItems()

            choice = input("\nDo you want to buy more? (yes or no): ").lower()

            if choice != 'y':
                print("Thank you for visiting the cafeteria! :) ")
                break


# ---------------------- Main Program ----------------------

ui = UI()
ui.run()


# Outputs

"""
First Run:

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab5.py
3 packaged foods, 2 hot foods, 3 drinks

Packaged Food
1 Granola Bar $ 3.50
2 Fruit $ 2.00
3 Salad $ 6.00

Hot Food
4 Wings $ 9.50
5 Pizza $ 7.00

Drinks
6 Soda $ 1.50
7 Juice $ 2.00
8 Water $ 1.00

Select a number from the menu: 
I would like to have a 3 and a 5 plus a 6

Receipt
----------------------------------------
Item                     Price
----------------------------------------
Salad               $    6.00
Pizza               $    7.64
Soda                $    1.69
----------------------------------------
TOTAL               $   15.33

Do you want to buy more? (yes or no): y

Packaged Food
1 Granola Bar $ 3.50
2 Fruit $ 2.00
3 Salad $ 6.00

Hot Food
4 Wings $ 9.50
5 Pizza $ 7.00

Drinks
6 Soda $ 1.50
7 Juice $ 2.00
8 Water $ 1.00

Select a number from the menu: 
My profressor would like to have 1, 3, 4 and a 8

Receipt
----------------------------------------
Item                     Price
----------------------------------------
Granola Bar         $    3.50
Salad               $    6.00
Wings               $   10.37
Water               $    1.15
----------------------------------------
TOTAL               $   21.01

Do you want to buy more? (yes or no): y 

Packaged Food
1 Granola Bar $ 3.50
2 Fruit $ 2.00
3 Salad $ 6.00

Hot Food
4 Wings $ 9.50
5 Pizza $ 7.00

Drinks
6 Soda $ 1.50
7 Juice $ 2.00
8 Water $ 1.00

Select a number from the menu: 
I would like to try -1, 2, and a 7

Receipt
----------------------------------------
Item                     Price
----------------------------------------
Fruit               $    2.00
Juice               $    2.29
----------------------------------------
TOTAL               $    4.29

Invalid selections:
-1

Do you want to buy more? (yes or no): n
Thank you for visiting the cafeteria! :)

Second Run:

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab5.py
3 packaged foods, 2 hot foods, 3 drinks

Packaged Food
1 Granola Bar $ 3.50
2 Fruit $ 2.00
3 Salad $ 6.00

Hot Food
4 Wings $ 9.50
5 Pizza $ 7.00

Drinks
6 Soda $ 1.50
7 Juice $ 2.00
8 Water $ 1.00

Select a number from the menu: 
I would like to have 4, 5 and a 8

Receipt
----------------------------------------
Item                     Price
----------------------------------------
Wings               $   10.37
Pizza               $    7.64
Water               $    1.15
----------------------------------------
TOTAL               $   19.15

Do you want to buy more? (yes or no): y

Packaged Food
1 Granola Bar $ 3.50
2 Fruit $ 2.00
3 Salad $ 6.00

Hot Food
4 Wings $ 9.50
5 Pizza $ 7.00

Drinks
6 Soda $ 1.50
7 Juice $ 2.00
8 Water $ 1.00

Select a number from the menu: 
we would like to have a one, two, and five

Receipt
----------------------------------------
Item                     Price
----------------------------------------
----------------------------------------
TOTAL               $    0.00

Do you want to buy more? (yes or no): n
Thank you for visiting the cafeteria! :) 

"""