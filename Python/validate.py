
import re
email = input("What is your email? ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
# re.fullmatch(pattern,string,flags=0)
# re.match(pattern, string, flags=0)
# ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
# (\w+\.)?\w+\.edu option
# ? either or
# re.IGNORECASE ignore K sentive
# re. MULTILINE ignore mulitple lines
# re.DOTALL ignore any character and new lines
# A|B either A or B
# (...) a group
# (?:...) non= capturing version
# \d decimal digit (0-9)
# \D not a Decimal digit like punctuation and non letters
# \s whitespace characters 
# \S not whitespace
# \W not a word character
# \w is represents a word character or alphanumeric
# if i want to paste a range of character just "[a-zA-Z0-9_]" which includes lowercase upder case and numbers and characters
# [] set of characters
# [^] complementing the set (r"^[^@]+@[^@]+\.edu$"
# ^ matches the start of the string
# $ matches the end of the string or just before the newline at the of the string
# r in raw string want pasted in as is
# re.search(pattern, string, flags=0)