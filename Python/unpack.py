def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25, 5)
# args is the numbered arguments in a list
# kwargs is a dict all the named that is passed to a dictionary
# unpack  * to pass the individual members of a list
# **coins is the same as *coins as unpacking data.
# *args, **kwargs
"""
Docstring for unpack
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")


"""
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons" : 100, "sickles" : 50, "knuts" : 25}

print(total(**coins), "Knuts")

"""


