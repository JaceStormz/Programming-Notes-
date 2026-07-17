# groceries_p52.py 
# 3/20/26
# Python 3.13.9

'''
Create a class Item which has
- instance variables: itemName, itemCost
- class variable: numberItems (gets increased every time a new Item is created)
- a default constructor that allows the user to set itemName and itemCost
( the default constructor sets itemName="apple" itemCost=2.49 if the user does not specify them)
- function to show() the item name and cost
- function to get() and set() the item name and cost

Create a list named groceryBag to store the objects:
- Fill the list with several Item's such as eggs, milk, carrots, bread, apples, each with different price.
- use Item.numberItems to show how many items you have created.
- use a loop to calculate and show the totalCost for all the items in the bag

'''



class Item:
    # class variable
    numberItems = 0

    # constructor with default values
    def __init__(self, itemName="apple", itemCost=2.49):
        self.itemName = itemName
        self.itemCost = itemCost
        Item.numberItems += 1

    # show function
    def show(self):
        print(f"Item: {self.itemName}, Cost: ${self.itemCost:.2f}")

    # getters
    def getName(self):
        return self.itemName

    def getCost(self):
        return self.itemCost

    # setters
    def setName(self, name):
        self.itemName = name

    def setCost(self, cost):
        self.itemCost = cost


# Create list
groceryBag = []

# Add items
groceryBag.append(Item("A dozen eggs", 4.59))
groceryBag.append(Item("A gallon of milk", 2.89))
groceryBag.append(Item("Carrots", 1.49))
groceryBag.append(Item("A loaf of bread", 2.99))
groceryBag.append(Item("Bag of 12 apples", 4.25))

# Show all items
print("Items in grocery bag:")
for item in groceryBag:
    item.show()

# Show number of items created
print(f"\nTotal number of items created: {Item.numberItems}")

# Calculate total cost
totalCost = 0
for item in groceryBag:
    totalCost += item.getCost()

print(f"Total cost of grocery bag: ${totalCost:.2f}")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python groceries_p52.py
Items in grocery bag:
Item: A dozen eggs, Cost: $4.59
Item: A gallon of milk, Cost: $2.89
Item: Carrots, Cost: $1.49
Item: A loaf of bread, Cost: $2.99
Item: Bag of 12 apples, Cost: $4.25

Total number of items created: 5
Total cost of grocery bag: $16.21

'''