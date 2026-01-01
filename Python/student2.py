def main():
    student = Student.get()
    print(student)

class Student: 
    def __init__(self, name, house): 
        self.name = name
        self.house = house 

def __str__(self):
    return f"{self.name} from {self.house}"

@classmethod
def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name, house)

 

if __name__ == "__main__":
    main()
# you can instantiate an object by call cls without creating a new function