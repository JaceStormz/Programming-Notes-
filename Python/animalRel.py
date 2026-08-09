# 08/07/2026
# animalRel.py

class Cat:
    def  __init__(self, name, legs, whiskers):
        self.name = name
        self.legs = legs
        self.whiskers = whiskers

    def eat(self):
        return self.name + " is eating"

    def sleep(self):
        return self.name + " is sleeping"
        
class PersianCat(Cat):
    def __init__(self, name, legs, whiskers, fur_type):
        super().__init__(name, legs, whiskers)
        self.fur_type = fur_type
        
class SiameseCat(Cat):
    def __init__(self, name, legs, whiskers, fur_type):
        super().__init__(name, legs, whiskers)
        self.fur_type = fur_type

class BengalCat(Cat):
    def __init__(self, name, legs, whiskers, fur_type):
        super().__init__(name, legs, whiskers)
        self.fur_type = fur_type

cats = [
     PersianCat("Milo", 4, True, "Long"),
     PersianCat("Luna", 4, True, "Long"),
     SiameseCat("Simba", 4, True, "Short"),    
     BengalCat("Leo", 4, True, "Short")
]

for cat in cats:
    print(cat.sleep())

    