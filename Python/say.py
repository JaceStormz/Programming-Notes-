# package is a third party libarary that the user/coder can install in our computer or cloud server that will allow more access to that other have created
# PyPi.org directory of all packages that can to be used in python
# pip is a package manager installer using a cammand called pip install "package name"
import cowsay
import sys

if len(sys.argv) == 2:
    print(cowsay.trex("hello, " + sys.argv[1]))
    
print("Hello World!")
   