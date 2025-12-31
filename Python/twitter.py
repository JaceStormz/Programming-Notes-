# replace the value in the field "url.replace"
# removeprefix removes that prefix value from that field "url.removeprefix"
"""
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
"""
# re.sub(pattern, repl, string, count=0, flags=0)

import re

url = input("URL: ").strip()
# RE's can be nested to solve different problems
# re.sub is meant to clean data
"""
username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
"""
# (?:..) doesn't not capture that the first group so instead of group(2) use group(1) the first parenthesis is ignore
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):

    print(f"Username:", matches.group(1))