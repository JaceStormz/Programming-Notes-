# Lab4.py
# Gautam Rao
# 05/26/2026
# Python 3.13.9
'''
Write a program that lets customers at a cafeteria purchase food and drink

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