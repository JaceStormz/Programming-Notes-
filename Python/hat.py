import random
# class variable that one exist in that class they share the variable
class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Harry")
# python can use the cls to access the object.
# so a class method can be use to take class variable and use it with a classmethod or @Classmethod
# classes are used to represent real world entities
# instance method writing class of methods that are automatically pass a refer to self
# class can be used as a container for data that are conceptually related and a class method does just that.
