class ChainRestaurant:
    def __init__(self):
        self.menu = {
            "Burger": 8.99,
            "Pizza": 12.99,
            "Salad": 6.99,
            "Pasta": 10.99
        }

        self.cities = [
            "Los Angeles",
            "San Diego",
            "Sacramento",
            "San Francisco",
            "Fresno"
        ]

    def addCity(self, city):
        if city not in self.cities:
            self.cities.append(city)


class Franchise(ChainRestaurant):
    def __init__(self, tables, seatsPerTable, franchisePrice, location):
        super().__init__()
        self.tables = tables
        self.seatsPerTable = seatsPerTable
        self.franchisePrice = franchisePrice
        self.location = location

    def addMenuItem(self, item, price):
        self.menu[item] = price

    def takeOrder(self, orders):
        total = 0

        for item in orders:
            if item in self.menu:
                total += self.menu[item]

        return total


franchise = Franchise(15, 4, 250000, "Sacramento")

franchise.addMenuItem("Tacos", 7.99)
franchise.addCity("Oakland")

order = ["Burger", "Tacos", "Salad"]

print("Location:", franchise.location)
print("Total: $", format(franchise.takeOrder(order), ".2f"))