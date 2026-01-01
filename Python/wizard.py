class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...        

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry","Gyffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")    

# Inheritance is define mulitple call that relate to one other. 
# super is a way to access the properties of the parent class Example:
# the perenthesis in front of the class helps call the parent class 
# the super() helps bring the attributes of the parent class
"""
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
"""