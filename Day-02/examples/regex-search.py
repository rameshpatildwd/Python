import re

text = "The quick brown fox"
pattern = r"quick"              #The r before a string in Python (e.g., r"quick") makes it a raw string literal

match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match")