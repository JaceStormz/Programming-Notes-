i= 0
while i < 3:
    print("meow")
    i +=  1
#------------------------------------------------
for _ in range(3):    #-- use an underscore to replace an unused variable
    print("Meow")
#------------------------------------------------
print("meow\n" * 3, end="") #-- end="" resolves the extra line by (\n)next line syntax
#------------------------------------------------
#-- Induce an infinite loop so long the value of "n" is true
while True:
    n = int(input("What is n? "))
    if n > 0:
        break
    #-- after the value is true break then run the for loop
for _ in range(n):
    print("meow")
#---------------------------------------------------------
def main():
    number = get_number()
    meow(3)

    def get_number():
        while True:
             n = int(input("What is n? "))
             if n > 0:
                 break
             return n

            

    def meow(n):
        for _ in range(n):
            print("meow")

main()