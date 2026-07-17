# Lab4.py
# 05/17/2026
# Python 3.13.9
'''
Create a restaurant class that can perform the following operations as member functions:
• Add items to a menu.
• Make table reservations.
• Take customer orders.
• Print the menu.
• Print table reservations.
• Print customer orders.
To get full credit, your class should include the following data structures and functionalities:
    • Begin your program by inputting all of the items on the menu from the user prompt, one by one, and inserting
    them into the menu through a member function of the class
    • Menu should be stored as a key-value pairing of item and price
    • Tables should be stored as a key-value pairing of table number to number of seats. You may hard-code as many
    or as little tables as you want as the default value of the tables, as long as there's at least one table. This should
    be a stagnant value that doesn't get updated throughout the program.
    • Printing the menu should be a print member function and should be formatted to not be just a print out of a
    dictionary
    • Print table reservations should print out the current tables that are still available
    • To take customer orders, print out the menu and ask user for as many orders as user wants. Then the function
    should print out the total price for the user of all items ordered.
    • There should be a member function to make a reservation. The function should determine whether there is a
    table with the appropriate number of seats still available. There can be empty seats, but there cannot be more
    people than seats at a table.

'''

class Restaurant:


    def __init__(self):
        # Menu stored as item -> price
        self.menu = {}

        # Tables stored as table number -> number of seats
        self.tables = {
            1: 2,
            2: 4,
            3: 4,
            4: 6,
            5: 8
        }

        # Reserved tables
        self.reservations = {}

        # Customer orders
        self.orders = []

    # Add items to menu
    def addMenuItem(self, item, price):
        self.menu[item] = price

    # Print menu
    def printMenu(self):
        print("\n----- MENU -----")
        for item, price in self.menu.items():
            print(f"{item:<20} ${price:.2f}")

    # Print available tables
    def printAvailableTables(self):
        print("\n----- AVAILABLE TABLES -----")

        available = False

        for tableNum, seats in self.tables.items():
            if tableNum not in self.reservations:
                print(f"Table {tableNum}: {seats} seats")
                available = True

        if not available:
            print("No tables available.")

    # Make reservation
    def makeReservation(self, customerName, people):
        for tableNum, seats in self.tables.items():

            # Check if table is available and has enough seats
            if tableNum not in self.reservations and seats >= people:
                self.reservations[tableNum] = customerName

                print(f"\nReservation successful!")
                print(f"{customerName} reserved Table {tableNum} ({seats} seats)")
                return

        print("\nNo suitable table available.")

    # Print reservations
    def printReservations(self):
        print("\n----- CURRENT RESERVATIONS -----")

        if len(self.reservations) == 0:
            print("No reservations made.")
            return

        for tableNum, customerName in self.reservations.items():
            seats = self.tables[tableNum]
            print(f"Table {tableNum} ({seats} seats) reserved for {customerName}")

    # Take customer order
    def takeOrder(self):
        if len(self.menu) == 0:
            print("Menu is empty.")
            return

        total = 0
        customerOrder = []

        while True:
            self.printMenu()

            item = input("\nEnter item to order (or type 'done'): ").title()

            if item == "Done":
                break

            if item in self.menu:
                customerOrder.append(item)
                total += self.menu[item]
                print(f"{item} added to order.")
            else:
                print("Item not found on menu.")

        self.orders.append(customerOrder)

        print("\n----- ORDER SUMMARY -----")

        if len(customerOrder) == 0:
            print("No items ordered.")
        else:
            for item in customerOrder:
                print(item)

            print(f"Total Price: ${total:.2f}")

    # Print all customer orders
    def printOrders(self):
        print("\n----- CUSTOMER ORDERS -----")

        if len(self.orders) == 0:
            print("No customer orders.")
            return

        for index, order in enumerate(self.orders, start=1):
            print(f"\nOrder #{index}")

            for item in order:
                print(f"- {item}")


# ---------------- MAIN PROGRAM ----------------

restaurant = Restaurant()

# Input menu items from user
print("Enter menu items.")
print("Type 'done' when finished.\n")

while True:
    item = input("Enter item name: ").title()

    if item == "Done":
        break

    price = float(input(f"Enter price for {item}: $"))

    restaurant.addMenuItem(item, price)

print("\nMenu has been created!")

# Menu system
while True:
    print("\n===== RESTAURANT SYSTEM =====")
    print("1. Print Menu")
    print("2. Make Reservation")
    print("3. Print Reservations")
    print("4. Print Available Tables")
    print("5. Take Customer Order")
    print("6. Print Customer Orders")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        restaurant.printMenu()

    elif choice == "2":
        name = input("Enter customer name: ")
        people = int(input("How many people? "))
        restaurant.makeReservation(name, people)

    elif choice == "3":
        restaurant.printReservations()

    elif choice == "4":
        restaurant.printAvailableTables()

    elif choice == "5":
        restaurant.takeOrder()

    elif choice == "6":
        restaurant.printOrders()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")

# Each output is really long, so I am really sorry 
"""
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab4.py
Enter menu items.
Type 'done' when finished.

Enter item name: Pizza 
Enter price for Pizza: $20
Enter item name: Hamburger   
Enter price for Hamburger : $10
Enter item name: Ice Cream
Enter price for Ice Cream: $8
Enter item name: Burrito
Enter price for Burrito: $12
Enter item name: Donut
Enter price for Donut: $3
Enter item name: Hotdog
Enter price for Hotdog: $7
Enter item name: Soda
Enter price for Soda: $3.25
Enter item name: bottle Water
Enter price for Bottle Water: $1
Enter item name: Candy
Enter price for Candy: $3
Enter item name: Cookie
Enter price for Cookie: $3
Enter item name: Chips
Enter price for Chips: $2
Enter item name: done

Menu has been created!

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 1

----- MENU -----
Pizza                $20.00
Hamburger            $10.00
Ice Cream            $8.00
Burrito              $12.00
Donut                $3.00
Hotdog               $7.00
Soda                 $3.25
Bottle Water         $1.00
Candy                $3.00
Cookie               $3.00
Chips                $2.00

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 2
Enter customer name: Jeff Cloud
How many people? 6

Reservation successful!
Jeff Cloud reserved Table 4 (6 seats)

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 3

----- CURRENT RESERVATIONS -----
Table 4 (6 seats) reserved for Jeff Cloud

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 4

----- AVAILABLE TABLES -----
Table 1: 2 seats
Table 2: 4 seats
Table 3: 4 seats
Table 5: 8 seats

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 5

----- MENU -----
Pizza                $20.00
Hamburger            $10.00
Ice Cream            $8.00
Burrito              $12.00
Donut                $3.00
Hotdog               $7.00
Soda                 $3.25
Bottle Water         $1.00
Candy                $3.00
Cookie               $3.00
Chips                $2.00

Enter item to order (or type 'done'): burrito
Burrito added to order.

----- MENU -----
Pizza                $20.00
Hamburger            $10.00
Ice Cream            $8.00
Burrito              $12.00
Donut                $3.00
Hotdog               $7.00
Soda                 $3.25
Bottle Water         $1.00
Candy                $3.00
Cookie               $3.00
Chips                $2.00

Enter item to order (or type 'done'): Donut
Donut added to order.

----- MENU -----
Pizza                $20.00
Hamburger            $10.00
Ice Cream            $8.00
Burrito              $12.00
Donut                $3.00
Hotdog               $7.00
Soda                 $3.25
Bottle Water         $1.00
Candy                $3.00
Cookie               $3.00
Chips                $2.00

Enter item to order (or type 'done'): Hotdog
Hotdog added to order.

----- MENU -----
Pizza                $20.00
Hamburger            $10.00
Ice Cream            $8.00
Burrito              $12.00
Donut                $3.00
Hotdog               $7.00
Soda                 $3.25
Bottle Water         $1.00
Candy                $3.00
Cookie               $3.00
Chips                $2.00

Enter item to order (or type 'done'): Candy
Candy added to order.

----- MENU -----
Pizza                $20.00
Hamburger            $10.00
Ice Cream            $8.00
Burrito              $12.00
Donut                $3.00
Hotdog               $7.00
Soda                 $3.25
Bottle Water         $1.00
Candy                $3.00
Cookie               $3.00
Chips                $2.00

Enter item to order (or type 'done'): done

----- ORDER SUMMARY -----
Burrito
Donut
Hotdog
Candy
Total Price: $25.00

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 6

----- CUSTOMER ORDERS -----

Order #1
- Burrito
- Donut
- Hotdog
- Candy

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 7
Exiting program...

-----Indian restaurant ----------------------

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab4.py
Enter menu items.
Type 'done' when finished.

Enter item name: Roti 
Enter price for Roti: $5
Enter item name: Aloo Tikki
Enter price for Aloo Tikki: $10
Enter item name: Batat Vada
Enter price for Batat Vada: $5
Enter item name: Bhailia Papdi Chaat
Enter price for Bhailia Papdi Chaat: $9
Enter item name: Bhel Poori
Enter price for Bhel Poori: $8
Enter item name: Bombay Chaat
Enter price for Bombay Chaat: $11
Enter item name: North Indian Thaali
Enter price for North Indian Thaali: $20
Enter item name: South Indian Thaali
Enter price for South Indian Thaali: $23
Enter item name: Mango Lassi
Enter price for Mango Lassi: $7
Enter item name: Pav Bhaji
Enter price for Pav Bhaji: $13
Enter item name: Masala Dosa
Enter price for Masala Dosa: $15
Enter item name: done

Menu has been created!

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 1

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 2
Enter customer name: Narendra Modi 
How many people? 15

No suitable table available.

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 2
Enter customer name: Venkat Mechineni
How many people? 7

Reservation successful!
Venkat Mechineni reserved Table 5 (8 seats)

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: Siddu Rati
Invalid choice.

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 2
Enter customer name: Siddu Rati
How many people? 5

Reservation successful!
Siddu Rati reserved Table 4 (6 seats)

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 3

----- CURRENT RESERVATIONS -----
Table 5 (8 seats) reserved for Venkat Mechineni
Table 4 (6 seats) reserved for Siddu Rati

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 5

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

Enter item to order (or type 'done'): Pav Bhaji
Pav Bhaji added to order.

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

Enter item to order (or type 'done'): Bhel Poori
Bhel Poori added to order.

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

Enter item to order (or type 'done'): Masala Dosa
Masala Dosa added to order.

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

Enter item to order (or type 'done'): Mango lassi
Mango Lassi added to order.

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

Enter item to order (or type 'done'): South Indian Thaali
South Indian Thaali added to order.

----- MENU -----
Roti                 $5.00
Aloo Tikki           $10.00
Batat Vada           $5.00
Bhailia Papdi Chaat  $9.00
Bhel Poori           $8.00
Bombay Chaat         $11.00
North Indian Thaali  $20.00
South Indian Thaali  $23.00
Mango Lassi          $7.00
Pav Bhaji            $13.00
Masala Dosa          $15.00

Enter item to order (or type 'done'): done

----- ORDER SUMMARY -----
Pav Bhaji
Bhel Poori
Masala Dosa
Mango Lassi
South Indian Thaali
Total Price: $66.00

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 6

----- CUSTOMER ORDERS -----

Order #1
- Pav Bhaji
- Bhel Poori
- Masala Dosa
- Mango Lassi
- South Indian Thaali

===== RESTAURANT SYSTEM =====
1. Print Menu
2. Make Reservation
3. Print Reservations
4. Print Available Tables
5. Take Customer Order
6. Print Customer Orders
7. Exit
Choose an option: 7
Exiting program...

"""