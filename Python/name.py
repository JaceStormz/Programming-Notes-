# In Python, sys.argv is a list that contains the command-line arguments 
# passed to a script when it is executed. The first element of the list, 
# sys.argv, is always the name of the script itself, 
# while subsequent elements represent the arguments provided after the script name. 
# This list is automatically populated by the Python interpreter when the script runs, 
# and it allows the script to access and 
# process user-supplied inputs directly from the command line.

"""
import sys

if len(sys.argv) <2:
    print("too few arguments")
elif len(sys.argv) >2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
"""
# sys.exit prematurely exist if the value does not match

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)
# to take a slice of a list is to take a subset. Slice is a key word in python
