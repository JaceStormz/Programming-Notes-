import re

name = input("What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2)+" "+ matches.group(1)
print(f"Hello, {name}")
# := is a walrus operated which also you ask a boolean experession and also assign a value