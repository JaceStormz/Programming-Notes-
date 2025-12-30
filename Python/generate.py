# from keyword allows you to import function from a module but allows you to be more specific
# import allows you retieve data from an entire library/module
# by adding the import one doesn't need to put random.choice but just choice
"""
from random import choice

coin = choice(["heads", "tails"])
print(coin)
"""
#-------------------------------------
# random.randint(x, y) selects a number between to the two varaibles evertime it is executed

"""
import random

number = random.randint(1,10)
print(number)
"""
# random.shuffle can shuffle (randomly selects values from a list/array)
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
