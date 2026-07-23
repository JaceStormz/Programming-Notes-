""" items = ["bread", "fruits","fruits", "veggies"]
items [0] = "chips"
items.insert(1, 'butter')
items.append("drinks")
print(len(items))
print(items) """
############################
""" expenses = [
    ["January", 2200],
    ["February", 2350],
    ["March", 2600],
    ["April", 2130],
    ["May", 2190]

]

difference = expenses[0][1] - expenses[1][1]
total = expenses[0][1] + expenses[1][1] + expenses[2][1]
check = 2000 in expenses
expenses.append(["June", 1500])
expenses[3][1] += 200
print(difference)
print(total)
print(check)
print(expenses) """
########################################
heros=['spider man','thor','hulk','iron man','captain america']
heros.insert(3, 'black panther')
heros[1:3] = ['dr. strange']
heros.sort()
print(len(heros))
print(heros)