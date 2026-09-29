# relearning regex through examples

import re 

text = """
Name: John Smith
Email: john.smith@example.com
Phone: 408-555-1234
Order: #48392
Price: $129.99
"""

result = re.search(r"\d{3}-\d{3}-\d{4}", text)

print(result.group())