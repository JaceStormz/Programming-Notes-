# sumPosNeg_p15.py 
# Gautam Rao
# 1//23/26
# Python 3.13.9
# Write a program which calculates exactly how much more (or less) you can make with the penny on day 30
penny = 0.01
days = 30

# Calculation the number of pennies after 30vdays 
for day in range(1, days):
    penny *= 2

million = 1_000_000

difference = penny - million

# output
print(f"Value of the penny after {days} days: ${penny:,.2f}")
print(f"Million dollars: ${million:,.2f}")

if difference > 0:
    print(f"The penny gives you ${difference:,.2f} MORE than a million dollars.")
else:
    print(f"The penny gives you ${abs(difference):,.2f} LESS than a million dollars.")

'''
PS C:\\Users\\super\\OneDrive\\Desktop\\Repo_Files\\De Anza Python Class> python penniesMade_p21.py
Value of the penny after 30 days: $5,368,709.12
Million dollars: $1,000,000.00
The penny gives you $4,368,709.12 MORE than a million dollars.

'''