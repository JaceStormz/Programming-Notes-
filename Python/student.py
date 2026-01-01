class Student: # the blueprint of the object
    def __init__(self, name, house): # the init method is the initializer must be build before use.
        self.name = name
        self.house = house # the self.house no underscore allowing it to fire the getter when this funtion is called


def __str__(self):
    return f"{self.name} from {self.house}"

@property
def name(self):
    return self._name

@name.setter
def name(self, name):
    if not name:
        raise ValueError("Missing name")
    self._name = name

@property #decorator getter takes only one arguement
def house(self):
    return self._house

@house.setter #decorator setter takes two arguements for setters
def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
    self._house = house

def main():
    student = get_student()
    print(student) 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()
# you use underscore or _house to in front of your instance variable 
# ***** in python you can NOT have a function and instance variable with the same name*****
# decorators a function that modifies other function
# __str__ it allows the program to see it at a string
# raise - the programmer can bring an error to python as an expection
# class Student: # the blueprint of the object
# def __init__(self, name, house): # the init method is the initializer must be build before use.
# self gives you access to the current object just created
# self is a argument that helps store the values of the object and must be used during in initialization of the object
# __init__ is an instance method if you want to initialize the contents the object of a class you define this code
# methods these describe a behavior of a funtion
# Objects can be both immutable and mutable based on how they are created byt user.
# Objects you create from class, an object use that class to instants of the object
# Class have attributes and syntax for it "." to add attributes of object
# Class is a blue print for pieces of data or like mold that is a data that you can design
# Tuple is a collection of values like a list but immutable just by using a coma
# example return name, house
# tuples are used for defensing programming because values can not be changed
# print(f"{student[0]} from {student[0]}") executing a tuple and indexing