# Lab3.py
# Gautam Rao
# 05/07/2026
# Python 3.13.9
# Program to read country population data and allow user lookups

countryData = {}

try:
    # Open the file
    file = open("population_by_country_2020.txt", "r", encoding="utf-8")

    # Read all lines into a list
    lines = file.readlines()

    # Close the file
    file.close()

except IOError:
    print("Error: Could not open or read the file.")
    exit()

except Exception as e:
    print("An unexpected error occurred:", e)
    exit()

# Skip the header line and process the data
for line in lines[1:]:

    # Remove newline and split by tab
    fields = line.strip().split("\t")

    try:
        country = fields[0]
        population = int(fields[1])
        landArea = int(fields[5])

        
        # country = population, land area
        countryData[country] = [population, landArea]

    except (ValueError, IndexError):
        continue


# Country or Ranking Choice


choice = ""

while choice.lower() not in ["country", "ranking"]:
    choice = input("Do you want to see info based on a country or ranking?\n")


# Country Option

if choice.lower() == "country":

    countryName = ""

    while countryName not in countryData:
        countryName = input("Which country do you want to see?\n")

        if countryName not in countryData:
            print("Invalid country name. Try again.")

    population = countryData[countryName][0]
    landArea = countryData[countryName][1]

    print(f"The {countryName} has population {population} "
          f"and land area {landArea} sq km.")



# Ranking Option


elif choice.lower() == "ranking":

    rankingType = ""

    while rankingType.lower() not in ["population", "land area"]:
        rankingType = input(
            'Do you want ranking based on "population" or "land area"?\n'
        )

    # Sort based on user's selection
    if rankingType.lower() == "population":

        sortedData = sorted(
            countryData.items(),
            key=lambda item: item[1][0],
            reverse=True
        )

    else:  # land area

        sortedData = sorted(
            countryData.items(),
            key=lambda item: item[1][1],
            reverse=True
        )

    # Get ranking number
    while True:
        try:
            rank = int(input("Which ranking do you want to see?\n"))

            if 1 <= rank <= len(sortedData):
                break
            else:
                print("Please enter a valid ranking number.")

        except ValueError:
            print("Please enter a number.")

    # Retrieve ranked country
    country = sortedData[rank - 1][0]
    population = sortedData[rank - 1][1][0]
    landArea = sortedData[rank - 1][1][1]

    if rankingType.lower() == "population":
        print(f"Rank #{rank} in population is {country} "
              f"with population {population}.")
    else:
        print(f"Rank #{rank} in land area is {country} "
              f"with land area {landArea} sq km.")

# Output
"""
First run

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab3.py
Do you want to see info based on a country or ranking?
country
Which country do you want to see?
United States
The United States has population 331341050 and land area 9147420 sq km.

Second run

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab3.py
Do you want to see info based on a country or ranking?
ranking 
Do you want ranking based on "population" or "land area"?
land area
Which ranking do you want to see?
1
Rank #1 in land area is Russia with land area 16376870 sq km.

Third run for my fun

PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza CIS41A> python Lab3.py
Do you want to see info based on a country or ranking?
country
Which country do you want to see?
India 
The India has population 1382345085 and land area 2973190 sq km.

"""