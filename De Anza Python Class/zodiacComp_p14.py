# zodiacComp_p14.py 
# Gautam Rao
# 1//23/26
# Python 3.13.9
# Write a program that asks the user for day and month of a birthday. 

# input
day = int(input("Please enter your birth day: "))
month = input("Please enter your birth month: ").lower()

# zodiac and compatible checker
if (month == "march" and day >= 21) or (month == "april" and day <= 19):
    zodiac = "Aries"
    compatible = "Leo, Sagittarius, Gemini"
elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
    zodiac = "Taurus"
    compatible = "Virgo, Capricorn, Cancer"
elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
    zodiac = "Gemini"
    compatible = "Libra, Aquarius, Aries"
elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
    zodiac = "Cancer"
    compatible = "Scorpio, Pisces, Taurus"
elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
    zodiac = "Leo"
    compatible = "Aries, Sagittarius, Gemini"
elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
    zodiac = "Virgo"
    compatible = "Taurus, Capricorn, Cancer"
elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
    zodiac = "Libra"
    compatible = "Gemini, Aquarius, Leo"
elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
    zodiac = "Scorpio"
    compatible = "Cancer, Pisces, Capricorn"
elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
    zodiac = "Sagittarius"
    compatible = "Aries, Leo, Aquarius"
elif (month == "december" and day >= 22) or (month == "january" and day <= 19):
    zodiac = "Capricorn"
    compatible = "Taurus, Virgo, Scorpio"
elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
    zodiac = "Aquarius"
    compatible = "Gemini, Libra, Sagittarius"
elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
    zodiac = "Pisces"
    compatible = "Cancer, Scorpio, Capricorn"
else:
    zodiac = "Unknown"
    compatible = "N/A"

#output
print("A Birthday of:", month.capitalize(), day)
print("The Zodiac is:", zodiac)
print("Compatible Signs:", compatible)

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python zodiacComp_p14.py
Please enter your birth day: 18
Please enter your birth month: may
A Birthday of: May 18
The Zodiac is: Taurus
Compatible Signs: Virgo, Capricorn, Cancer

'''