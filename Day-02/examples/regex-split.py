import re

text = "apple,banana,orange,grape"
pattern = r","                              #The r before a string in Python (e.g., r"quick") makes it a raw string literal

split_result = re.split(pattern, text)
print("Split result:", split_result)
print(type(split_result))       #to print data type