# 08/05/2026
# LibraryD.py



def country_adder(dictionary):

    country = input("Enter country: ").upper().strip()
    

    if country in country_population:
            print("Country exist")
    else:
        population = int(input("Enter Population (in millions): "))
        country_population[country] = population
        print("Country Added!")
def country_remover(dictionary):
     check = input("Do you wish to remove a country (Y/N): ").strip().upper()
     

     if check == 'Y':
         country = input("What country would you like to remove?: ").strip().upper()
         if country in dictionary:
          
          dictionary.pop(country)
          print("Country removed!")
         else:
            print("Country not found.")      

def country_query(dictionary):
    country = input("what country would you like to query?: ").strip().upper()
    if country in dictionary:
        print(country_population)
    else:
        print("Country not found/exist.")

# the population is in millions
country_population = {
    "CHINA": 1343, 
    "INDIA": 1536, 
    "USA": 332, 
    "PAKISTAN": 21,
    "JAPAN": 150, 
    "CANADA": 252, 
    "GERMANY": 171
 }
query = input("What is your task (Add, Remove, or Query) a Country?: ").strip().lower()
if query == "add":
    country_adder(country_population)
elif query == "remove":
    country_remover(country_population)
elif query == "query":
    country_query(country_population)
else:
    print("Invalid Input")
